# Data collection and processing 

A collection of python scripts to obtain and process Korea-related open data

# About this repository

* solar: to collect solar energy generation data from https://www.data.go.kr (공공데이터포털 한국전력거래소)
  - api_solar: 한국전력거래소_지역별 시간별 태양광 발전량 정보 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15103243) 
* asos: to collect ASOS data from https://www.data.go.kr (공공데이터포털 기상청)
  - api_asos: 기상청_지상(종관, ASOS) 시간자료 조회서비스 (https://www.data.go.kr/data/15057210/openapi.do)
* aerosol: to collect air quality data from https://www.airkorea.or.kr/ (한국환경공단 에어코리아)
* others:

  - latlon_loc.py: to find administrative regions (level 1: 도/특별시/광역시) for a given lat/lon based on the Korean map data from https://guides.lib.umich.edu/c.php?g=283110&p=1886160 > Global Administrative Areas > https://gadm.org/download_country.html (v4.1 is used)

# Related posts
* How to use an API
