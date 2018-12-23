from logging import getLogger, StreamHandler, Formatter, DEBUG
import requests

import CONSTS

LOGGER = getLogger('custom_search_api')
HANDLER = StreamHandler()
HANDLER.setLevel(DEBUG)
HANDLER.setFormatter(Formatter('%(message)s'))
LOGGER.setLevel(DEBUG)
LOGGER.addHandler(HANDLER)


def fetch(url: str, params: dict=None):
    res = requests.get(url, params)
    res.raise_for_status()
    return res

API_PATH    = "https://www.googleapis.com/customsearch/v1"
start_index = 1
params = {
    "cx" : CONSTS.ENGINE_KEY, #検索エンジンID
    "key": CONSTS.G_KEY, #APIキー
    "q"  : "中島由貴", #検索ワード
    "searchType": "image", #検索タイプ
    "start" : start_index, #開始インデックス
    "num" : 10   #1回の検索における取得件数(デフォルトで10件)
}
for _ in range(10): # 10 * 10 = 100
    res = fetch(API_PATH, params)
    LOGGER.info('#' * 80)
    res_json = res.json()
    for idx, items in enumerate(res_json['items'], start=start_index):
        path = "imgs/" + str(idx) + ".png"
        download_link = items['link']
        LOGGER.info(f'url:{download_link}')
        r = requests.get(download_link, stream=True)
        #if r.status_code == 200:
        #with open(path, 'wb') as f:
        # r.raw.decode_content = True
        #shutil.copyfileobj(r.raw, f)
    start_index = res_json['queries']['nextPage'][0].get('startIndex')
    LOGGER.info(f'next:{start_index}')
    params['start']= start_index
