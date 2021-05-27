import requests
from bs4 import BeautifulSoup
from indeed import show_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = indeed_jobs + so_jobs
save_to_file(jobs)
