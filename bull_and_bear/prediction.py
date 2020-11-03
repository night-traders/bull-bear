# prediction class 
# to be called by views

import pandas as pd
from datetime import datetime
import finnhub
import numpy as np
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

