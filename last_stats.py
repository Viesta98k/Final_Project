import pandas as pd
import plotly.express as px
from scipy.stats import pearsonr
from tags import ch_tags

road_count = [0]*110
all_counts = []
pearsons = []
dfs = []    # 不是深度優先搜索
for tag in ch_tags:
    df = pd.read_csv('node_data/{}分組.csv'.format(tag))
    dfs.append(df)
for i, row in dfs[0].iterrows():
    ct_idx = int(row['y']*10+row['x'])
    road_count[ct_idx]+=1
for i in range(1, 5):
    tmp_count = [0]*110
    for j, row in dfs[i].iterrows():
        ct_idx = int(row['y']*10+row['x'])
        tmp_count[ct_idx]+=1
    pearsons.append(pearsonr(road_count, tmp_count)[0])
    all_counts.append(tmp_count)
px.bar(x = ch_tags[1:], y = pearsons, labels={'x': '設施類型', 'y':'相關係數'},title='民生設施與道路分佈相關係數').write_image('figures/民生設施與道路分佈相關係數.png')
for i, ct in enumerate(all_counts):
    px.histogram(x=ct, labels={'x':'設施數量'}, title='{}在區域中數量分配圖'.format(ch_tags[i+1])).update_layout(yaxis_title='區域數目').write_image('figures/{}在區域中數量分配圖.png'.format(ch_tags[i+1]))