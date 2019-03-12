import pandas as pd
from datetime import datetime
import numpy as np

date_rng = pd.date_range(start='1/1/2018', end='1/08/2018', freq='H')

df['datetime'] = pd.to_datetime(df['date'])

df = df.set_index('datetime')

df.drop(['date'], axis=1, inplace=True)

df.head()
