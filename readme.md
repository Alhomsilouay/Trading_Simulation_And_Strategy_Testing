
## Introduction

The aim of this repo is be familar with the basics of trading simulation and trading strategies testing, and this by using  several tools and libraries. Bellow some of the known backtesting libraries in python:

                                       Table: Comparison of Backtesting Libraries
|Library	     |Ease of Use	|Flexibility	|Performance Metrics	|Visualization	|Maintenance |Best For                         |
|----------------|--------------|---------------|-----------------------|---------------|------------|--------------------|
|Backtesting.py	 |High	        |  Medium	    |Yes      	            |Yes	        |Active |Beginners, simple strategies    |
|Backtrader	     |Medium	    |    High	    |Yes	                |Yes	        |Inactive |    Advanced users, optimization |
|Zipline	     |Medium	    |    High	    |Yes	                |Limited	    |Abonded |    Algorithmic trading, large datasets |
|PyAlgoTrade	 |Medium	    |    High	    |Yes	                |Yes	        | Inactive|   Exchange-specific, advanced users |
|VectorBT        |Medium        |     High      |Yes                    |  Yes             |Active |Beginners, ML integration|
|Finmarketpy     |Low           | Medium        |Yes                    | Yes | Active |Volatility-targeted strategies|



### Backtesting.py
Backtesting.py, which is a powerful Python backtesting framework for developing  and testing trading strategies. 
Backtesting.py is a lightweight library that allows you to:

1. Create and simulate trading strategies
2. Run backtests on historical data
3. Visualize performance and trades
4. Generate metrics (e.g., Sharpe ratio, drawdowns, returns, etc.)

Backtesting ingests all kinds of OHLC data (stocks, forex, futures, crypto, ...) as a pandas.DataFrame with columns 'Open', 'High', 'Low', 'Close' and (optionally) 'Volume'. Such data is widely obtainable, e.g. with packages:
- pandas-datareader,
- Quandl,
- findatapy,
- yFinance,
- investpy, etc.

### Backtrader
Backtrader is an open-source Python library. Backtrader allows you to focus on writing reusable trading strategies, indicators and analyzers instead of having to spend time building infrastructure. It is used for:

1. Backtesting trading strategies (historical simulation)
2. Paper trading (live testing with fake money)
3. Live trading (integration with brokers like Interactive Brokers, Alpaca, etc.)
4. Optimization of strategy parameters
5. Handling complex indicators and multiple data feeds

| Feature	| Description |
|-----------|-------------|
|Strategy Class	| Inherit from bt.Strategy to define your logic.  |
|Indicators	     |Built-in indicators like RSI, SMA, MACD, Bollinger, ATR, etc.|
|Custom Indicators	|You can define your own indicators very easily. |
|Commission & Slippage	|Easily simulate realistic trading environments.|
|Portfolio Management	|Supports multiple assets, cash, positions.|
|Timeframes	           |Works with any frequency: minute, hourly, daily, weekly, etc.|
|Live Trading	|Integrates with brokers for real-time trading.|

## Code files description

The code examples are the following focusing on Backtesting.py and Backtrader:

### 1_MA Crossover strategy test.ipynb

The goal of the code in  "1_MA Crossover strategy test.ipynb":
is to do a step-by-step code to be fmiliar with the simulation of a forex strategy testing.

The m-period and n-period MA crossover (m < n) is a common strategy. When the short MA crosses above the long MA, it's a buy signal, and vice versa for a sell

1. Calculate the moving averages.
2. Generate buy/sell signals.
3. Simulate trades based on these signals, using the ATR indicator to choose SL and TP.
4. Compute performance metrics.
5. Visualize the results.



### 2_RSI_BuyBacktesting.py
It is a python code to start with Backtesting.py library

### 3_RSI_BuyBacktesingJuypterNB.ipynb

This file is a Jupter Notebook of 2_RSIBacktesting.py with more notes and explanations


### 4_SMA_Backtesing.ipynb

Backtesting a simple moving average (MA) cross-over strategy, on Google data. using backtesting.py library


### 5_Backtrader_1.ipynb
In this file we follow the following steps:
- Installing libraries
- Importing
- Fetching data, Cleaning data  
- Initialization and feeding data to  Backtrader's data format
- Running cerebro (the engine class of Backtrader)
- Plotting


### 6_Backtrader_2.ipynb
In this file we follow the following steps:
- Installing libraries
- Importing
- Fetching data, parsing  
- Initialization and feeding data to  Backtrader's data format
- Define strategy (RSI crossover)
- Run backtesting
- Print Strategy Performance Metrics
- Plotting 

### 7_Backtrader_3.ipynb
This file deal with hourly EURUSD data over one year, in which we try to use Backtrader library to test a moving average crossover strategy

In this file we follow the following steps:
- Installing libraries
- Importing
- Fteching hourly EURUSD data  and cleaning 
- Defining strategy class with hourly timeframe adjustments
- Initialization and feeding data to  Backtrader's data format
- Run simulation
- Print Strategy Performance Metrics
- Plotting 


### 8_Backtrader_4.ipynb
This file is a Juypter NoteBook version of the py files of Backterder documentation web page:
https://www.backtrader.com/docu/order-creation-execution/bracket/bracket/
The goal is go step-by-step in code to understand the use of "Bracket Orders"

### 9_Backtrader_5.ipynb
This file is based on the reference:
Rajandran R 
Introduction to Backtrader – Creating your First Trading Strategy – Python Trading Tutorial
September 25, 2024


## Refferences:

- https://kernc.github.io/backtesting.py/
- https://github.com/ChadThackray/backtesting-py-2022/
_ https://www.backtrader.com/
- Algovibes, Python for Finance: https://www.youtube.com/@Algovibes
- https://www.youtube.com/@parttimelarry
- https://www.marketcalls.in/python/introduction-to-backtrader-creating-your-first-trading-strategy-python-trading-tutorial.html


## Appendix 1
### Strategy Performance Metrics


<img src="Documents/Strategy Metrics 1.PNG" alt="Strategy Result" width="1000"/>

<img src="Documents/Strategy Metrics 2.PNG" alt="Strategy Result" width="1000"/>

<img src="Documents/Strategy Metrics 3.PNG" alt="Strategy Result" width="1000"/>