import pandas as pd
from datetime import datetime
import finnhub
import numpy as np
import matplotlib
import matplotlib.pyplot as plot
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import activations
from tensorflow.keras.callbacks import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
import matplotlib.pyplot as plt
import mplfinance as mpf
from tensorflow.keras.models import load_model
from datetime import datetime
import time
import os

import base64
from io import BytesIO

# FINNHUB_KEY = os.environ['FINNHUB']

class MakePrediction:

    def __init__(self, ticker):
        self.ticker = ticker
        # self.client = finnhub.Client(api_key=FINNHUB_KEY)
        self.client = finnhub.Client(api_key='bua9lb748v6q418gd0i0')

    def get_candlestick_data(self, ticker, timeframe, start, end):
        '''
        Makes call to finnhub api and returns the processed response as a dataframe
        '''
        data = self.client.stock_candles(ticker, timeframe, start, end)
        del data['s']
        df = pd.DataFrame.from_dict(data)
        df['t'] = df['t'].apply(lambda x: datetime.fromtimestamp(x))
        df = df.rename(columns={'c': 'Close', 'h': 'High', 'l': 'Low', 'o': 'Open', 't': 'Date', 'v': 'Volume'})
        df.set_index('Date', inplace=True)
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        return df

    def stock_data_253(self):
        '''
        Uses get_candlestick_data to get candlestick data for a given stock and returns the df with the most recent 253 rows
        '''
        current_time = int(time.time())
        prev_time = current_time - 46656000
        df = self.get_candlestick_data(self.ticker, 'D', prev_time, current_time)
        df = df.iloc[len(df)-253:]
        return df

    def get_prediction(self):
        '''
        Uses other helper functions and returns a nested array of 7 days of stock predictions. Each day is an array with 5 price points
        '''
        data = self.stock_data_253()
        open_data = data.iloc[:, 0:5].to_numpy()
        scaler = MinMaxScaler(feature_range = (0, 1))
        open_data = scaler.fit_transform(data)
        x_test = [open_data[0:253]]
        x_test = np.asarray(x_test)
        model = load_model('bull_and_bear/minimize_size_weights.hdf5')
        stock_prediction = model.predict(x_test)
        stock_prediction = scaler.inverse_transform(stock_prediction.reshape(-1, stock_prediction.shape[-1])).reshape(stock_prediction.shape)
        return stock_prediction[0]

    def get_prediction_df(self):
        '''
        Post processing the get_prediction results, putting them in a df with correct date index and column names, appends to 2 months of historical data, returns the appended df
        '''
        stock_prediction = self.get_prediction()
        prediction_df = [i for i in stock_prediction]
        date_index = []
        for i in range(7):
            date_index.append(datetime.fromtimestamp((i*86400) + int(time.time()))) 
        prediction_df = pd.DataFrame(data=prediction_df, index=date_index)
        prediction_df = prediction_df.rename(columns={0: 'Open', 1: 'High', 2: 'Low', 3: 'Close', 4: 'Volume'})
        combined_df = self.stock_data_253().tail(30).append(prediction_df)
        return combined_df


    def get_df_img(self):
        matplotlib.use('agg')
        df = self.get_prediction_df()
        s = mpf.make_mpf_style(base_mpf_style='yahoo', gridstyle=' ')
        fig, axlist = mpf.plot(df, type='candle', figratio=(8, 5), returnfig=True, style=s, volume=True)
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

        return encoded


if __name__ == "__main__":
    pass