from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from model.predictor import predict_stock

app = FastAPI(title="NSE Stock Price Prediction")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None, "error": None}
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, symbol: str = Form(...)):
    symbol = symbol.upper()

    if not symbol.endswith(".NS"):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Invalid format. Please use STOCKNAME.NS",
                "result": None
            }
        )

    try:
        result = predict_stock(symbol)
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": result,
                "error": None
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": str(e),
                "result": None
            }
        )
