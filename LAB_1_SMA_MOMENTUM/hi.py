# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # LAB 1

# %%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## Download data
# - OHLC data
# - Fundamental data

# %%
# Lấy data từ Apple trên yahoo finance
data = yf.download("AAPL", start="2015-01-01", end="2025-10-01", progress = False)
data.tail()

# %%
# Vẽ biểu đồ giá đóng
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label='Close')      # Giá

plt.legend()
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("AAPL Close Price")
plt.show()

# %% [markdown]
# ## Technical indicators
#

# %% [markdown]
# ### Simple moving average (SMA)
#

# %%
df = yf.download("AAPL", start="2022-01-01", end="2025-10-01", progress = False)

df['SMA_20'] = df['Close'].rolling(window=20).mean() # rolling windows 20 days
df['SMA_50'] = df['Close'].rolling(window=50).mean() # rolling windows 50 days
df['SMA_100'] = df['Close'].rolling(window=100).mean() # rolling windows 50 days
df['SMA_200'] = df['Close'].rolling(window=200).mean() # rolling windows 50 days


# %%
plt.figure(figsize=(14,5))
plt.plot(df['Close'], label='Close')      # Giá
plt.plot(df['SMA_20'], label='SMA 20')    # SMA 20
plt.plot(df['SMA_50'], label='SMA 50')    # SMA 50
plt.plot(df['SMA_100'], label='SMA 100')  # SMA 100
plt.plot(df['SMA_200'], label='SMA 200')  # SMA 200
plt.grid(True, alpha=0.5)
plt.legend()
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Close Price with SMA")
plt.show()

# %% [markdown]
# - Identifying trend

# %% [markdown]
# ## Momentum trading

# %%
