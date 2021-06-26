import requests
from bs4 import BeautifulSoup
from so import get_jobs as get_so_jobs
from wwr import get_jobs as get_wwr_jobs
from rio import get_jobs as get_rio_jobs
from save import save_to_file

so_jobs = get_so_jobs()
wwr_jobs = get_wwr_jobs()
rio_jobs = get_rio_jobs()


jobs = wwr_jobs + rio_jobs + so_jobs
save_to_file(jobs)

