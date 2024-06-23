import overpy
import pandas as pd
from tags import tags, ch_tags

api = overpy.Overpass() # 初始化api



total_size = 0
for i, tag in enumerate(tags):
    lon = []    # 經度資料
    lat = []    # 緯度資料
    result = api.query("area['name'='臺北市']; nwr[{}](area); out;".format(tag))
    for v in result.nodes:
        lon.append(v.lon)
        lat.append(v.lat)
    df = pd.DataFrame({'經度':lon, '緯度':lat})
    df.to_csv('node_data/{}在臺北市之分佈經緯度.csv'.format(ch_tags[i]))
    print("{}資料列數:{}".format(ch_tags[i],df.shape[0]))
    total_size+=df.shape[0]
print('總資料列數：{}'.format(total_size))
