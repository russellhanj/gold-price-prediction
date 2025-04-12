# Gold Price Prediction

This project forecasts daily gold prices using multiple modeling strategies — including traditional time series models, machine learning, and deep learning.

## 📌 Objectives

- Analyze macroeconomic and sentiment-based factors influencing gold prices
- Build forecasting models using:
  - ARIMA, SARIMA, SARIMAX
  - Prophet (with/without exogenous variables)
  - Random Forest, XGBoost
  - LSTM
- Create an ensemble model for improved prediction accuracy
- Forecast gold prices for January to March 2025

## 👥 Authors
- Russell Han Josef
- Dev Nguyen

## 📊 Dependencies

```bash
pip install pandas==2.2.3
pip install numpy==1.24.4
pip install matplotlib==3.10.1
pip install seaborn==0.13.2
pip install scikit-learn==1.3.2
pip install xgboost==2.1.1
pip install statsmodels==0.14.4
pip install prophet==1.1.6
pip install tensorflow==2.12.0
pip install vaderSentiment==3.3.2
pip install requests==2.32.3
pip install selenium==4.20.0
pip install python-dotenv==1.1.0
```

## 📊 Data Sources

- **Gold Price (daily)**  
  [https://finance.yahoo.com/quote/GC%3DF/history/?period1=1388534400&period2=1735603200](https://finance.yahoo.com/quote/GC%3DF/history/?period1=1388534400&period2=1735603200)

- **USD Index (DXY)**  
  [https://finance.yahoo.com/quote/DX-Y.NYB/history/?period1=1388534400&period2=1735603200](https://finance.yahoo.com/quote/DX-Y.NYB/history/?period1=1388534400&period2=1735603200)

- **The Guardian News API** (for financial headline sentiment)  
  [https://content.guardianapis.com/search](https://content.guardianapis.com/search)

- **CPI (Consumer Price Index)** – FRED  
  [https://fred.stlouisfed.org/series/CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)

- **10-Year Treasury Yield (DGS10)** – FRED  
  [https://fred.stlouisfed.org/series/DGS10](https://fred.stlouisfed.org/series/DGS10)
