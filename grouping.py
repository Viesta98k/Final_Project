import pandas as pd
from scipy.stats import pearsonr
from tags import ch_tags

# 臺北市經緯度上下界乘以50
MIN_LON_50 = 6072
MAX_LON_50 = 6082
MIN_LAT_50 = 1247
MAX_LAT_50 = 1257

for i, tag in enumerate(ch_tags):
    # 將dataframe乘以50後取整準備分組
    df = pd.read_csv('node_data/{}在臺北市之分佈經緯度.csv'.format(tag), index_col=0).mul(50).astype('int32')   
    df['x'] = df['經度']-MIN_LON_50
    df['y'] = df['緯度']-MIN_LAT_50
    df = df.clip(lower=pd.Series({'x':0, 'y':0}),upper=pd.Series({'x': 10, 'y':10}), axis=1)
    df.to_csv('node_data/{}分組.csv'.format(tag))
