# remoteio

import requests
from bs4 import BeautifulSoup

URL = "https://remoteok.io/api?tag=python"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
jobs = requests.get(URL,headers=headers).json()
db =[]


def get_jobs(): #이 사이트의 경우 검색해 나오는 페이지 하나만을 스캔할 것이기 때문에 extract_jobs를 만들지 않는다.
    for job in jobs:
        if "company_logo" in job:
            title=job["position"]
            company=job["company"]
            location=job["location"]
            apply_link=job["url"]
            db.append({"title":title, "company":company, "location":location, "apply-link":apply_link})
    return db
    
