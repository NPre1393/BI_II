import pandas as pd
import datetime as dt
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import task3_mach as t3
from datetime import datetime
from utils.extract_features import extract_ts_features
import csv

mpl.rcParams['timezone'] = 'Europe/Vienna'

def get_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp)

def get_datetime_string(timestamp):
    return get_datetime(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def df_get_datetime(df):
    dts = []
    for item in df:
        dts.append(get_datetime(item))    
    return dts

def writeToFile(fname, df):
    with open(fname, 'a') as file:
        wr = csv.writer(file)
        wr.writerow(df)

def get_df(machs, window=3):
    df = pd.DataFrame(machs)
    df.columns = ['value', 'timestamp']
    df.value = df.value.astype(float)
    x = [dt.datetime.strptime(elem, '%Y-%m-%dT%H:%M:%S.%f') for elem in df.timestamp]
    u = [dt.datetime.timestamp(elem) for elem in x]
    df.index = df_get_datetime(u)
    df.timestamp = u
    return df
    #print(df)
    #res = df.drop('timestamp', axis=1)
    #paa_data = res.rolling(window).mean().dropna()[::window]
    #df['timestamp'] = u
    
    
def create_paa_plot(res, paa, window):
    """
    plots x-coords of interpolated dataframe and paa dataframe 
    :input res: resampled/interpolated dataframe
    :input paa: paa dataframe
    """
    #TODO: plot x,y,z,total infeatures one figure

    original_data = res.valuefeatures
    paa_data = np.array(paa.vafeatureslue)
    
    original_len = len(original_data)
    a = 0
    if not original_len % window == 0:
        a = 1
    
    print(len(original_data))
    print(len(paa_data))
    plt.plot(figsize=(12,8))
    plt.plot(np.arange(original_len), original_data, 'o-', label='Original')
    plt.plot(np.arange(window // 2,
                   (original_len + window // 2),
                   window)-a, paa_data.T, 'o--', label='PAA')
    plt.vlines(np.arange(0, original_len, window),
           original_data.min(), original_data.max(), color='g', linestyles='--', linewidth=0.5)
    plt.legend(loc='best', fontsize=14)
    plt.show()
"""
#fName = "1363058b-e88a-4ce4-8ef0-92f3197046df.xes.yaml"
#fName = "596ae4e1-ddc6-4f7c-b85b-45e31db907e0.xes.yaml"
fName = "9cd024b9-dba2-4676-bec7-fde13f294cf6.xes.yaml"

#fName = "ccf8b5f9-45e6-4b52-aa65-7cdd555eca05.xes.yaml"
information = "State/actToolRadius"
#information = "Spindle/actSpeed"
machining, queue = t3.query_main(open("/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/{0}".format(fName), "r"), information)
#information = "State/actToolLength1"
fName = "ccf8b5f9-45e6-4b52-aa65-7cdd555eca05.xes.yaml"
machining2, queue2 = t3.query_main(open("/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/{0}".format(fName), "r"), information)
#print(machining)
#print(machining2)
#print(queue2)
#mach_ts = pd.read_csv("machining_times_c.csv", sep=";", header=0)
"""
"""
print(machining)
print(machining2)
print(len(machining))
df = get_df(machining)
df2 = get_df(machining2)
print(df, df2)
uludag = df.append(df2)
print(uludag)

print(df.head())
(fig, ax) = plt.subplots(1,1)
ax.plot(df.value)
#plt.savefig("img/load/Axis_Z_aaLoad_581.png")
plt.show()

features, cols = extract_ts_features(df, col='value')

print(features, cols)

(fig, ax) = plt.subplots(1,1)
#ax.plot(x, df.value)
ax.plot(paa_data)

#plt.savefig("tool_len_124.png")
plt.show()
"""

root_dir = "/media/hailegebressi/Windows8_OS1/Users/Julien/Documents/data/BI/gv12/logs/parts/"
#col_names = ['mean', 'std', 'min', '20%', '40%', '50%', '60%', '80%', 'max', 'median', 'acfmean', 'acfstd', 'acfmedian', 'qstatmean', 'qstatstd', 'qstatmedian', 'mda', 'max_index', 'sma_sim', 'sma_adv', 'sma_sim_abs', 'sma_adv_abs', 'energy', 'iqr', 'entropy', 'autoreg_coeff', 'kurtosis', 'skewness', 'length', 'trace_id', 'qr']
#prod_measures = "prod_measurements2.csv"
mach_ts = "data/tool_len.csv"
#writeToFile(mach_ts, col_names)
information = "State/actToolLength1"
df = pd.DataFrame()
for dirName, subdirList, fileList in os.walk(root_dir):
    print('Found dir: %s' % dirName)
    for fname in fileList:
        item = open(dirName+'/'+fname, 'r')    
        machs, queue = t3.query_main(item, information)   
        """
        if len(machs)>50:
            print(len(machs), queue)
            features, cols = extract_ts_features(get_df(machs), col='value')
            features.append(len(machs))
            features.extend(queue)

            #print(features)
            writeToFile(mach_ts, features)
        elif len(machs)<50 and len(machs)>0:
            print("Machining btw 0 and 50: ",len(machs), queue)
        """
        if len(machs) > 0:
            tmp = get_df(machs)
            tmp.to_csv(mach_ts, mode='a', header=False)
            df = df.append(tmp)
            print(len(df))
"""
df_plot = df.sort_values(by='timestamp')
plt.plot(df_plot.value)
plt.show()
"""

"""
print(mach_ts)
start = [dt.datetime.strptime(elem[:23], '%Y-%m-%dT%H:%M:%S.%f') for elem in mach_ts.time_calling]
end = [dt.datetime.strptime(elem[:23], '%Y-%m-%dT%H:%M:%S.%f') for elem in mach_ts.time_done]

#u = [dt.datetime.timestamp(elem) for elem in x]

durations = []
for i in range(0,len(start)):
    dur = end[i] - start[i]
    dur_s = dur.total_seconds()
    durations.append(dur_s)

mach_ts['duration'] = durations
print(mach_ts)
mach_ts.to_csv("mach_durations.csv", index=False)
"""