# 楽天APIお試し
import os
import sys
import pandas as pd
import numpy as np
import requests
import pprint
import json

# 自作のモジュールの読み込みってこんなめんどくさかったか？
cdir = os.getcwd() + "/src"
sys.path.append(cdir)

import apiInfo

url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"

# これもこんなにめんどくさかったか？
api_id = apiInfo.RAKUTEN_APPLICATION_ID
category_num = '564500'
format_num = '2'
page_num = '1'

result = {}
for page_int in range(3):
    page_num = str(page_int+1)
    response = requests.get(url, params = {
    'applicationId':api_id,
    'genreId':category_num,
    'formatVersion':format_num,
    'page':page_num}
    )
    json_data = response.json()

    for rank in range(30):
        try:
            rank_num = json_data['Items'][rank]['rank']
            ItemName_str = json_data['Items'][rank]['itemName']
            ItemUrl_str = json_data['Items'][rank]['itemUrl']
            ShopName_str = json_data['Items'][rank]['shopName']
            ItemPrice_str = json_data['Items'][rank]['itemPrice']
            PointRate_str = json_data['Items'][rank]['pointRate']
            add_data = {}
            add_data['ItemName'] = ItemName_str
            add_data['StoreName'] = ShopName_str
            add_data['ItemUrl'] = ItemUrl_str
            add_data['ItemPrice'] = ItemPrice_str
            add_data['PointRate'] = PointRate_str
            result[rank_num] = add_data
        except IndexError:
            break
        except KeyError:
            break

#pprint.pprint(result)
#pprint.pprint(response.json())
#with open('download_r.json', 'w') as f:
    #json.dump(json_data, f, ensure_ascii=False, indent=4)

res = pd.DataFrame(result).T
res.to_csv('to_csv_out.csv', encoding='utf_8_sig')
