import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import acf
from statsmodels import robust
from scipy.stats import iqr
import scipy as sp
from spectrum import arburg
from scipy.stats import kurtosis, skew

import matplotlib.pyplot as plt
import matplotlib

def extract_ts_features(segment, col='value'):
        """
        extract features for given segment

        features: median, mean, std, min, percentiles, max, correlations, ?acf?
        :return: list with feature values
        """
        # get median of total col
        total_median = segment[col].median()

        # specify percentiles
        perc = [.20,.40,.60,.80]
        
        # describe returns count, mean, std, min, percentiles and max
        #total_describe = segment.describe(percentiles=perc).total
        total_describe = segment.describe(percentiles=perc)[col]
          
        # correlation of total col for x,y,z and time
        # method can be spearman, pearson and kendall
        #corre = segment.corr(method='pearson')[col]
        #print(corre)

        # autocorrelation function for total col, nlags controls number of values
        # qstat=True also gives Q-statistic (acf_df[1]) and p-values (acf_df[2])
        acf_df = acf(segment[col], fft=True, qstat=True, nlags=len(segment[col]))
        # aggregate acf values and qstat values
        acorr_mean = acf_df[0].mean()
        acorr_std = acf_df[0].std()
        acorr_med = np.median(acf_df[0])
        qstat_mean = acf_df[1].mean()
        qstat_std = acf_df[1].std()
        qstat_med = np.median(acf_df[1])
        # mda
        median_absolute_deviation = robust.mad(segment[col])
        # index for maximum value (only really important for frequency domain data)
        """
        max_val = segment.loc[segment[col].idxmax(), col]
        max_val_idx = pd.Index(segment[col])
        if not isinstance(max_val, np.float64):
            idx = len(segment)
        else:
            idx = max_val_idx.get_loc(max_val)
        """
        max_df = segment[col].reset_index(drop=True)
        idx = max_df.idxmax()

        # signal magnitude area
        sma_sim, sma_adv, sma_sim_abs, sma_adv_abs = calc_sma(segment[col])
        # energy
        energy = (segment[col].values**2).sum(axis=0)
        # interquartile range
        inter_qr = iqr(segment[col], axis=0)
        # entropy
        ent = entropy(segment[col])
        P = autoreg_coeff(segment[col]) 

        kurtosis, skewness = kurtosis_skewness(segment[col])

        col_names = list(total_describe.index[1:])
        col_names.extend(['median', 'acfmean', 'acfstd', 'acfmedian' , 'qstatmean', 'qstatstd', 'qstatmedian', 'mda', 'max_index', 'sma_sim', 'sma_adv', 'sma_sim_abs', 'sma_adv_abs', 'energy', 'iqr', 'entropy', 'autoreg_coeff', 'kurtosis', 'skewness'])
        
        # add all to list and return
        descr_list = list(total_describe.values[1:])
        #correlation_list = list(corre.values[:4]) 
        
        descr_list.append(total_median)
        #descr_list.extend(correlation_list)
        descr_list.extend([acorr_mean, acorr_std, acorr_med, qstat_mean, qstat_std, qstat_med])
        descr_list.extend([median_absolute_deviation, idx, sma_sim, sma_adv, sma_sim_abs, sma_adv_abs, energy, inter_qr, ent, P, kurtosis, skewness])

        return descr_list, col_names

def calc_sma_for_window(data):
    return np.sum(data) / len(data)

def calc_sma_adv_for_window(data):
    return np.sum(data - np.mean(data) / len(data))

def calc_absolutes_for_list(list):
    return ([abs(i) for i in list])

def calc_sma(data):
    sma_sim = calc_sma_for_window(data)
    sma_adv = calc_sma_adv_for_window(data)

    sma_sim_abs = calc_sma_for_window(calc_absolutes_for_list(data))
    sma_adv_abs = calc_sma_adv_for_window(calc_absolutes_for_list(data))
    return sma_sim, sma_adv, sma_sim_abs, sma_adv_abs

def entropy(data):
    p_data = data.value_counts()/len(data) 
    entropy = sp.stats.entropy(p_data)   
    return entropy

def autoreg_coeff(df, order=1):
    """
    Estimate the complex autoregressive parameters by the Burg algorithm
    :return P: Real variable representing driving noise variance (mean square of residual noise) 
    from the whitening operation of the Burg filter. 
    """
    AR, P, k = arburg(df, order=order)
    return P

def kurtosis_skewness(df):
    return kurtosis(df), skew(df)