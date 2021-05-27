import requests
from bs4 import BeautifulSoup

LIMIT = 50

URL = "https://stackoverflow.com/jobs?q=python&so_source=JobSearch&so_medium=Internal&pg="


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")[:-1]
    last_page = pages[-1].get_text().strip()
    return int(last_page)

def extract_job(html):
    title = html.find("div", {"class":"grid--cell fl1"}).find("a").string
    company = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find_all("span")[0].string
    if company is not None:
        company = company.rstrip()
    location = html.find("h3", {"class":"fc-black-700 fs-body1 mb4"}).find_all("span")[1].string
    if location is not None:
        location = location.lstrip('\r\n').rstrip()
    job_id = html["data-jobid"]
    
    return {"title":title, "company":company, "location":location, "apply-link":f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: page {page + 1}")
        result = requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs



    
def get_jobs():
   last_page = get_last_page()
   jobs = extract_jobs(last_page)
   return jobs