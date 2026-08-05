

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import joblib
import os

st.set_page_config(page_title="Stock Price Prediction", page_icon="📈", layout="wide")

# -----------------------------
# Load Model
# -----------------------------
model_path = os.path.join("model", "stock_prediction_model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Project Information")
st.sidebar.write("""
**Model:** Linear Regression

**Dataset:** Apple (AAPL)

**Features**
- Open
- High
- Low
- Volume
- MA10
- MA20
- Daily_Return
- Prev_Close
""")

st.title("📈 Stock Price Prediction")

mode = st.radio(
    "Choose Prediction Mode",
    ["Live Market Data", "Custom Input"],
    horizontal=True
)

# ====================================================
# LIVE MODE
# ====================================================
if mode == "Live Market Data":

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()

    if st.button("Fetch & Predict"):

        try:
            stock = yf.download(ticker, period="3mo", progress=False)

            if stock.empty:
                st.error("No data found.")
                st.stop()

            if isinstance(stock.columns, pd.MultiIndex):
                stock.columns = stock.columns.get_level_values(0)

            stock["MA10"] = stock["Close"].rolling(10).mean()
            stock["MA20"] = stock["Close"].rolling(20).mean()
            stock["Daily_Return"] = stock["Close"].pct_change()
            stock["Prev_Close"] = stock["Close"].shift(1)

            stock.dropna(inplace=True)

            latest = stock.iloc[-1]

            X = pd.DataFrame({
                "Open":[latest["Open"]],
                "High":[latest["High"]],
                "Low":[latest["Low"]],
                "Volume":[latest["Volume"]],
                "MA10":[latest["MA10"]],
                "MA20":[latest["MA20"]],
                "Daily_Return":[latest["Daily_Return"]],
                "Prev_Close":[latest["Prev_Close"]]
            })

            prediction = model.predict(X)[0]

            st.success(f"Predicted Next Day Close : ${prediction:.2f}")

            c1,c2,c3,c4 = st.columns(4)

            c1.metric("Open",f"${latest['Open']:.2f}")
            c2.metric("High",f"${latest['High']:.2f}")
            c3.metric("Low",f"${latest['Low']:.2f}")
            c4.metric("Close",f"${latest['Close']:.2f}")

            st.metric("Volume", f"{int(latest['Volume']):,}")

            if prediction > latest["Close"]:
                st.success("📈 Expected Increase")
            elif prediction < latest["Close"]:
                st.warning("📉 Expected Decrease")
            else:
                st.info("➡️ No significant change")

            st.subheader("Last 3 Months Closing Price")
            st.line_chart(stock["Close"])

            result = pd.DataFrame({
                "Ticker":[ticker],
                "Current Close":[latest["Close"]],
                "Predicted Close":[prediction]
            })

            st.download_button(
                "Download Prediction CSV",
                result.to_csv(index=False),
                "prediction.csv",
                "text/csv"
            )

        except Exception as e:
            st.error(e)

# ====================================================
# CUSTOM INPUT MODE
# ====================================================
else:

    col1,col2 = st.columns(2)

    with col1:
        open_price = st.number_input("Open",value=190.50)
        high = st.number_input("High",value=193.20)
        low = st.number_input("Low",value=189.80)
        volume = st.number_input("Volume",value=55000000)

    with col2:
        ma10 = st.number_input("MA10",value=188.45)
        ma20 = st.number_input("MA20",value=185.90)
        daily_return = st.number_input("Daily Return",value=0.0029,format="%.6f")
        prev_close = st.number_input("Previous Close",value=189.95)

    if st.button("Predict Closing Price"):

        X = pd.DataFrame({
            "Open":[open_price],
            "High":[high],
            "Low":[low],
            "Volume":[volume],
            "MA10":[ma10],
            "MA20":[ma20],
            "Daily_Return":[daily_return],
            "Prev_Close":[prev_close]
        })

        prediction = model.predict(X)[0]

        st.success(f"Predicted Closing Price : ${prediction:.2f}")

        if prediction > prev_close:
            st.success("📈 Expected Increase")
        elif prediction < prev_close:
            st.warning("📉 Expected Decrease")
        else:
            st.info("➡️ No significant change")

st.divider()
st.caption("Developed using Streamlit • Scikit-Learn • yfinance")



