# weworkremotely

import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com/remote-jobs/search?term=python"

def get_list():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    containers = soup.find("div", {"class":"jobs-container"}).find_all("section", {"class":"jobs"})
    return containers

def extract_job(containers): #이 사이트의 경우 검색해 나오는 페이지 하나만을 스캔할 것이기 때문에 extract_jobs를 만들지 않는다.
    result = []
    for container in containers:
        jobs = container.find("article").find("ul").find_all("li")
        for job in jobs:
            if "feature" in job.attrs["class"] or len(job.attrs["class"]) == 0:
                title=job.find("span", {"class":"title"}).text
                company=job.find("span", {"class":"company"}).text
                location="remote"
                a_list = job.find_all('a')
                apply_link=""
                for link in a_list:
                    if link not in job.find('div', {"class":"tooltip"}):
                        apply_link=link['href']
                print(apply_link)
                result.append({"title":title, "company":company, "location":location, "apply-link":apply_link})
    return result


def get_jobs():
    containers = get_list()
    return extract_job(containers)