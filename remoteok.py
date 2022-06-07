import requests
from bs4 import BeautifulSoup

def extract_job3(word):
    headers = {'user-Agent' : 'Daniel'}
    url = f"https://remoteok.com/remote-{word}-jobs"

    lists3 = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find('table', id='jobsboard').find_all("tr", {"class" : "job"})

    for J in table:
        company = J.find("h3", itemprop="name").text
        company = company.strip('\n')
        title = J.find("h2", itemprop="title").text
        title = title.strip('\n')
        Link = J.find("a", {"class" : "preventLink"})["href"]
        Link = "https://remoteok.com"+Link

        lists3.append({"title" : title, "company" : company, "link" : Link})

    return lists3