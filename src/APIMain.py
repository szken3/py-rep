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

# 商品検索APIのリクエストURL
# 後ろの日付はバージョンの代わり
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"

# これもこんなにめんどくさかったか？
api_id = apiInfo.RAKUTEN_APPLICATION_ID

# バドミントンをキーワードに価格降順をjson形式
# パラメータに関しては公式を参照 https://webservice.rakuten.co.jp/api/ichibaitemsearch/
keyword = "バドミントン"
sort = "-itemPrice"
format = "json"

response = requests.get(url, params = {
     'applicationId':api_id,
     'keyword':keyword,
     'sort':sort,
     'format':json}
     )

# 一回だけ抜いただけなので1ページに表示される上限30アイテムの情報のみ出力される
json_data = response.json()
for i in json_data["Items"]:
    item = i["Item"]
    print(item["itemName"] + item["itemUrl"])

# ファイル出力
# json_file = open('test_json.json', 'w')
# json.dump(json_data, json_file)
