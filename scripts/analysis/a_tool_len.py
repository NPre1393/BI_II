import sys
sys.path.append('../')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as dates
from matplotlib.dates import date2num

mpl.rcParams['timezone'] = 'Europe/Vienna'

df = pd.read_csv('../data/tool_len.csv', header=0, index_col=0)

df1 = df.sort_values(by='timestamp')
#df1.index = pd.to_datetime(df1.index)
print(np.unique(df1.value))
df_17 = df1.loc['2018-10-17':'2018-10-18']
df_17.index = pd.to_datetime(df_17.index)
df_18 = df1.loc['2018-10-18':'2018-10-19']
df_18.index = pd.to_datetime(df_18.index)
df_19 = df1.loc['2018-10-19':'2018-10-20']
df_19.index = pd.to_datetime(df_19.index)

fig = plt.figure(figsize=(20,5))
ax = plt.subplot(111)
plt.plot(df_19.value)
ax.set_title('actToolRadius 2018-10-19')
ax.xaxis_date()
ax.xaxis.set_minor_locator(dates.MinuteLocator(interval=15))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%H:%M'))
ax.xaxis.set_major_locator(dates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(dates.DateFormatter(''))
fig.savefig("../img/actToolLen/actToolLen_19-10-2018.png", dpi=900)
