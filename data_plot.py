import pandas as pd
import plotly.express as px
from tags import ch_tags

# 繪製道路與四種設施在臺北市內的分佈
for tag in ch_tags:
    df = pd.read_csv('node_data/{}在臺北市之分佈經緯度.csv'.format(tag))
    px.scatter(df, x='經度', y='緯度', title='{}在臺北市之分佈經緯度'.format(tag)).write_image('figures/{}在臺北市之分佈經緯度.png'.format(tag))