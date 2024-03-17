# Data collection and processing 

A collection of python scripts to obtain and process Korea-related open data

- pv_gen.py: to collect solar energy generation data (한국전력거래소_지역별 시간별 태양광 발전량 정보) from https://www.data.go.kr (공공데이터포털) through API
- korea_loc.py: to find administrative regions (level 1: 도/특별시/광역시) for a given lat/lon based on the Korean map data from https://guides.lib.umich.edu/c.php?g=283110&p=1886160 > Global Administrative Areas > https://gadm.org/download_country.html (v4.1 is used)
