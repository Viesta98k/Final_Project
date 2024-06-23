import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from tags import ch_tags

for tag in ch_tags:
    df = pd.read_csv('node_data/{}在臺北市之分佈經緯度.csv'.format(tag))
    model_k_means = KMeans(n_clusters=6,  max_iter=100, n_init='auto') #設定分群數目和最大迭代次數
    model_k_means.fit(df)
    px.scatter(x=df['經度'], y=df['緯度'], color=model_k_means.labels_, title='{}在臺北市之分佈經緯度k-means聚類結果'.format(tag)).write_image('figures/{}在臺北市之分佈經緯度k-means聚類結果.png'.format(tag))