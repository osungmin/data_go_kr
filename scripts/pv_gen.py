#!/usr/bin/env python
import requests
import json
from datetime import datetime

import pandas as pd
import numpy as np
print("all modules imported")

"""
한국전력거래소_지역별 시간별 태양광 발전량 정보
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15103243
"""

def count_rows(url, params):
    #request data
    req=requests.get(url, params = params)
    #print("request result code", req) #200=successuful!

    #convert to dictionary format
    json_dict=json.loads(req.text)

    json_df=json_dict['response']['body']['items']['item']
    df=pd.DataFrame(json_df)

    numOfRows=float(json_dict['response']['body']['numOfRows'])
    totCnt=float(json_dict['response']['body']['totalCount'])
    loopCnt=np.ceil(totCnt/numOfRows)

    if totCnt != 408.:
        print(" > how many data?", totCnt)
    return(loopCnt)

#url setup
url='http://apis.data.go.kr/B552115/PvAmountByLocHr/getPvAmountByLocHr'

for yr in np.arange(2023, 2023+1, 1):

    print("***** working on YEAR of", yr)
    dates=pd.date_range(start=str(int(yr))+"0101",end=str(int(yr))+"1231")

    for date in dates:

        print(" >", date)
        tradeYmd=datetime.strftime(date,'%Y%m%d')

        #params setup for the first time
        params = {
            'serviceKey' : '',
            'pageNo' : '1',
            'numOfRows' : '500',
            'dataType' : 'json',
            'tradeYmd' : tradeYmd }

        #count loop number
        loopCnt=count_rows(url, params)

        #main loop
        for i in range(int(loopCnt)):

            print(" ...", i+1 , "out of", int(loopCnt))
            #page number
            params['pageNo'] = str(i+1)

            #request data
            req=requests.get(url, params = params)
            #convert to dictionary format
            json_dict=json.loads(req.text)
            #read data
            json_df=json_dict['response']['body']['items']['item']

            if i==0: df=pd.DataFrame(json_df)
            else:    df=pd.concat([df.copy(), pd.DataFrame(json_df)],
                                  axis=0, ignore_index=True)


        #save
        df.to_csv('your_data_path', index=False)

    print("Done.")

print("End.")
