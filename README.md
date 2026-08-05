# stock-price-prediction
# 📈 Apple Stock Price Prediction using Machine Learning

## Live Demo

🚀 https://stock-price-prediction-kevaxswdgp3ervwged7vc6.streamlit.app/
## Overview

This project is a **Machine Learning-based web application** that predicts Apple (AAPL) stock prices using historical stock market data. The model is trained on historical Apple stock prices and deployed through a **Flask** web application, allowing users to enter stock-related values and obtain a predicted stock price.

---

## Features

* Predict Apple stock prices using a trained Machine Learning model.
* User-friendly Flask web interface.
* Uses historical Apple stock market data.
* Feature engineering using Moving Averages and Daily Returns.
* Model is trained once and saved for faster future predictions.
* Consistent predictions for the same input without retraining.

---

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib
* HTML
* CSS

---

## Project Structure

```text
Apple-Stock-Price-Prediction/
│
├── app.py
├── train_model.py
├── stock_model.pkl
├── scaler.pkl
├── apple_stock.csv
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## Machine Learning Features

The model uses the following input features:

* Open Price
* High Price
* Low Price
* Volume
* 10-Day Moving Average (MA10)
* 20-Day Moving Average (MA20)
* Daily Return

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Apple-Stock-Price-Prediction.git
```

Move into the project directory:

```bash
cd Apple-Stock-Price-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Future Improvements

* Support prediction for multiple stocks.
* Add interactive charts and visualizations.
* Integrate live stock market data.
* Improve prediction accuracy using advanced ML/DL models such as LSTM.

---

## Author

Developed by **Bhupalam Harini**
