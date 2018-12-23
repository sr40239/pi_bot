#-*- coding:utf-8 -*-
# ぴの自撮り画像を取得する
# https://qiita.com/ysdyt/items/02a9e6b4e70f26385abc を改変して、画像データを保存ではなくURLの取得のみにした。
import urllib.request
import httplib2
import json
import os
import pickle
import hashlib
import sha3
import CONSTS
from googleapiclient.discovery import build

# google画像検索APIを利用して中島由貴の自撮りを取得する
def getImageUrl(api_key, cse_key, search_word, page_limit):

    service = build("customsearch", "v1", developerKey=api_key)
    page_limit = page_limit
    startIndex = 1
    response = []

    img_list = []


    for nPage in range(0, page_limit):

        try:
            response.append(service.cse().list(
                q=search_word,     
                cx=cse_key,        
                lr='lang_ja',      
                num=10,            
                start=startIndex,
                searchType='image' 
            ).execute())

            startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

        except Exception as e:
            print(e)


    for one_res in range(len(response)):
        if len(response[one_res]['items']) > 0:
            for i in range(len(response[one_res]['items'])):
                img_list.append(response[one_res]['items'][i]['link'])

    return img_list



if __name__ == '__main__':
    # -------------- Parameter and Path Settings -------------- #
    API_KEY = CONSTS.G_KEY
    CUSTOM_SEARCH_ENGINE = CONSTS.ENGINE_KEY

    page_limit = 10
    search_word = '中島由貴'

    correspondence_table = {}

    img_list = getImageUrl(API_KEY, CUSTOM_SEARCH_ENGINE, search_word, page_limit)
    