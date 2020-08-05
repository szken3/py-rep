import requests
from bs4 import BeautifulSoup

# HTMLを全て取得
url = "https://www.amazon.co.jp/%E3%82%88%E3%81%AA%E3%82%88%E3%81%AA%E3%82%A8%E3%83%BC%E3%83%AB-350ml%C3%9724%E6%9C%AC/dp/B0069FI26O?ref_=Oct_s9_apbd_simh_hd_bw_b3sAUV&pf_rd_r=EN2V7FNVNC97CK4ZE43A&pf_rd_p=2431d242-8386-50c7-95fe-e621d811af78&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=57239051"
res = requests.get(url)

# とりあえずh1タグだけを抜き出して見る
soup = BeautifulSoup(res.text, "html.parser")
print(soup.h1)
