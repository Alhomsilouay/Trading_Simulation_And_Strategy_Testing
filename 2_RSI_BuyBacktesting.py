
# backtesting.py, which is a powerful Python backtesting framework for developing 
# and testing trading strategies.
# backtesting.py is a lightweight library that allows you to:

# 1. Create and simulate trading strategies

# 2. Run backtests on historical data

# 3. Visualize performance and trades

# 4. Generate metrics (e.g., Sharpe ratio, drawdowns, returns, etc.)

# Note: backtesting.py doesn’t come with a huge set of built-in indicators like some big 
# libraries (e.g., TA-Lib or pandas-ta), but it does provide a basic set of tools and lets you define 
# custom indicators using plain pandas or NumPy.

# Referenes:
# - https://kernc.github.io/backtesting.py/
# - https://github.com/ChadThackray/backtesting-py-2022/

import yfinance as yf
import datetime   #Built-in Python module, useful for handling date/time data (often used in backtesting).
import pandas as pd
import pandas_ta as ta   # A technical analysis library that offers over 100 indicators (like RSI, MACD, etc.).
from backtesting import Backtest   ## The engine that runs your strategy on data
from backtesting import Strategy  #The base class you inherit to define your custom strategy logic
from backtesting.lib import crossover   #Utility function that checks when one series crosses above another (used for buy/sell triggers).
from backtesting.test import GOOG  #Sample dataset (Google stock prices) included with the library for testing.

# Fetch hourly EURUSD data from Yahoo Finance
# data = yf.download("EURUSD=X", start="2024-01-01", end="2024-04-30", interval="1h")
# data.dropna(inplace=True)

# Define RSI (Relative Strength Index) Buy_only logic Strategy Class
# Step through bars one by one
# This allows multiple buys over time if price keeps crossing above 30, and closes trades once RSI gets too high.


# Define RSI Buy_Sell logic Strategy Class
class RsiBuy_Only_Logic(Strategy):
    u_bound = 70     # RSI above this = overbought (we may want to sell).
    l_bound = 30     # RSI below this = oversold (we may want to buy).
    rsi_window = 14      # Period of the RSI (how many bars to look back).
    #  Initialize Indicators
    def init(self):         # init() runs once at the start of the strategy to set up indicators
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)
        # self.I(...) is a wrapper that registers and caches indicators. It ensures the indicators are aligned with the data
        # ta.rsi(...) computes RSI using pandas_ta.
        # pd.Series(self.data.Close) ensures the closing price is treated as a series for RSI calculation
        # self.rsi is an array of RSI values for each bar (time step)
      
    # Strategy Logic (Buy-Only logic)  
    def next(self):     # Buy-Sell logic
        # Exit long if overbought
        if crossover(self.rsi, self.u_bound):
           self.position.close()
        else:
            # Enter long if RSI crosses above 30
            if crossover(self.l_bound, self.rsi):
                self.buy()
            
bt = Backtest(GOOG, RsiBuy_Only_Logic, cash=10_000, commission=.002) # runs the strategy on the data and returns performance statistics.
               # Commission per trade (0.2%).
               # daily data (interval=1d).
#bt = Backtest(data, RsiBuyOnly, cash=10000, commission=0.0002)
stats = bt.run()
print(stats)

bt.plot()      # bt.plot() creates an interactive chart
