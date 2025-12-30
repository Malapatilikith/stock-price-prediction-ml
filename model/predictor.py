# model/predictor.py

import yfinance as yf
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from newsapi import NewsApiClient


NEWS_API_KEY = "4e944e4a13374c0bbd74dba9194e54d5"


def predict_stock(stock_symbol: str) -> dict:
    stock_symbol = stock_symbol.upper()

    # ------------------------------
    # FETCH STOCK DATA
    # ------------------------------
    stock = yf.Ticker(stock_symbol)
    hist_data = stock.history(period="max")
    info = stock.info

    if hist_data.empty:
        raise ValueError("Invalid NSE symbol or data not available")

    # ------------------------------
    # COMPANY DETAILS
    # ------------------------------
    company_name = info.get("longName", "N/A")
    summary = info.get("longBusinessSummary", "N/A")

    market_cap_cr = info.get("marketCap", 0) / 1e7
    current_price = info.get("currentPrice", hist_data['Close'][-1])
    listed_date = hist_data.index.min().date().isoformat()

    # ------------------------------
    # FEATURE ENGINEERING
    # ------------------------------
    data = hist_data.copy()
    data['MA_10'] = data['Close'].rolling(window=10).mean()
    data['MA_30'] = data['Close'].rolling(window=30).mean()
    data['Daily_Return'] = data['Close'].pct_change()
    data.dropna(inplace=True)

    # ------------------------------
    # TARGET VARIABLE
    # ------------------------------
    data['Target'] = data['Close'].shift(-1)
    data.dropna(inplace=True)

    X = data[['Close', 'MA_10', 'MA_30', 'Daily_Return', 'Volume']]
    y = data['Target']

    split = int(len(data) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # ------------------------------
    # TRAIN MODEL
    # ------------------------------
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    # ------------------------------
    # NEXT DAY PREDICTION
    # ------------------------------
    latest_features = X.iloc[-1].values.reshape(1, -1)
    next_day_price = model.predict(latest_features)[0]

    # ------------------------------
    # NEWS FETCH
    # ------------------------------
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    news_data = newsapi.get_everything(
        q=company_name,
        language="en",
        sort_by="publishedAt",
        page_size=5
    )

    news_list = []
    for article in news_data.get("articles", []):
        news_list.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "date": article["publishedAt"][:10]
        })

    # ------------------------------
    # FINAL RESPONSE
    # ------------------------------
    return {
        "company_name": company_name,
        "stock_symbol": stock_symbol,
        "listed_since": listed_date,
        "market_cap_cr": round(market_cap_cr, 2),
        "current_price": round(current_price, 2),
        "summary": summary,
        "algorithm": "Linear Regression",
        "mae": round(mae, 2),
        "predicted_next_close": round(next_day_price, 2),
        "news": news_list
    }
