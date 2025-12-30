📈 NSE Stock Price Prediction – ML Web Application
A full-stack Machine Learning web application that predicts the next-day closing price of NSE-listed stocks using historical market data, and presents results through a clean, professional web interface.


**🔍 Project Overview**

This project allows users to:
Enter an NSE stock symbol (e.g., IDEA.NS)
View company details, market capitalization, and current price
Get a machine learning–based next-day closing price prediction
Read recent company-related news
Understand prediction limitations through clear financial disclaimers
The application is fully deployed on the web and accessible via a public URL.



**🧠 Machine Learning Details**
Algorithm Used: Linear Regression
Prediction Target: Next-day closing stock price
Training Data: From IPO date to present
Features Used:
Closing Price
10-Day Moving Average
30-Day Moving Average
Daily Return
Trading Volume


**📊 Evaluation Metric**
Mean Absolute Error (MAE)
Measures the average prediction error in ₹ (rupees), making results interpretable and business-friendly.


**🖥️ Application Architecture**
Frontend (HTML + CSS)
        ↓
FastAPI Backend
        ↓
Machine Learning Model
        ↓
Prediction + Company Info + News


**🌐 Tech Stack**
**Backend**
Python
FastAPI
Uvicorn
Machine Learning
scikit-learn
pandas
numpy
Data Sources
Yahoo Finance (historical stock data)
News API (recent company news)
**Frontend**
HTML (Jinja2 templates)
CSS (clean, minimal styling)
Deployment
Hosted on a cloud platform (Render)


**⚠️ Disclaimer**
Investments in securities market are subject to market risks.
Read all the related documents carefully before investing.
**Additionally:**
Stock price prediction is inherently uncertain.
This application is for educational and informational purposes only.
The developer is not responsible for any financial loss incurred.


**Live Demo**
**🔗 Live Application URL:**
https://stock-price-prediction-p57c.onrender.com/

**🛠️ Installation (Local Setup)**
1️⃣ Clone the repository
git clone https://github.com/your-username/stock-price-prediction-ml.git
cd stock-price-prediction-ml
2️⃣ Install dependenciespip install -r requirements.txt
pip install -r requirements.txt
3️⃣ Run the application
python -m uvicorn app:app --reload


**📂 Project Structure**
StockpricePrediction_ML/
│
├── app.py                  # FastAPI backend
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── model/
│   └── predictor.py        # ML logic
│
├── templates/
│   └── index.html          # HTML frontend
│
└── static/
    └── style.css           # CSS styling

In Help contact2310080070@klh.edu.in
