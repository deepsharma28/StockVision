# StockVision

StockVision – AI Powered Stock Forecasting Dashboard

StockVision is a machine learning-powered web application that predicts stock prices using historical market data. It provides interactive visualizations, technical indicators, and AI-based price forecasting using Streamlit.

🚀 Live Demo
Example:
https://stockvision.streamlit.app

## 📸 Dashboard Preview

### 🖥️ StockVision UI / Dashboard
![StockVision Dashboard](Screenshot%202026-06-12%20081611.png)

### 🧠 StockVision Logo
![StockVision Logo](assets/logo.png)

📊 Features
🔮 AI-based stock price prediction (ML model)
📉 Real-time stock data from Yahoo Finance
📊 Interactive charts (Price, Moving Averages, Volume)
🧠 Feature engineering (Lag features, MA, Volatility, Returns)
📈 Model performance metrics display
📌 Feature importance visualization
🎯 Multi-stock support (TSLA, AAPL, MSFT)
⚡ Fast and responsive Streamlit UI
🏗️ Tech Stack
Python
Streamlit
Pandas / NumPy
Scikit-learn
Yahoo Finance (yfinance)
Plotly
Joblib
📁 Project Structure
StockVision/
│
├── app.py
├── models/
│   ├── TSLA_model.pkl
│   ├── AAPL_model.pkl
│   └── MSFT_model.pkl
│
├── metrics/
│   └── metrics.csv
│
├── assets/
│   └── logo.png
│
├── README.md
⚙️ How It Works
User selects a stock (TSLA / AAPL / MSFT)
Data is fetched from Yahoo Finance
Feature engineering is applied:
Lag values
Moving averages
Volatility
Returns
Pre-trained ML model predicts next price
Dashboard visualizes:
Actual price trend
Moving averages
Volume
Prediction results
🧠 Machine Learning Model

The model uses engineered financial features:

Lag_1, Lag_2, Lag_3, Lag_5
MA_5, MA_10, MA_20
Volatility (Rolling Std)
Return (% change)
Volume

Trained using supervised regression models (stored as .pkl files).

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/StockVision.git
cd StockVision
2. Create virtual environment
python -m venv venv
3. Activate environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
📸 Preview

Replace this with your actual image

📊 Example Output
Current Stock Price
Predicted Price
Expected Change
Interactive Charts
Model Feature Importance
🔥 Future Improvements
Live streaming stock updates
LSTM / Deep Learning model integration
Portfolio tracking system
Buy/Sell signal generation
Multi-day forecasting graph
🤝 Author

Deep Sharma
📍 India
💼 Aspiring Data Engineer / ML Developer

⭐ Support

If you like this project:

Give it a ⭐ on GitHub
Share with others
Fork and improve it
