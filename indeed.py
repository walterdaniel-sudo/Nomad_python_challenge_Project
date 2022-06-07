import requests
from bs4 import BeautifulSoup

def extract_job2(word):
    URL = f"https://www.indeed.com/jobs?q={word}&rbl=Remote&jlid=aaa2b906602aa8f5&vjk=0f8951984a5e2121"

    lists2 = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    Sup = soup.find("ul", {"class" : "jobsearch-ResultsList"}).find_all("table", {"class" : "jobCard_mainContent"})

    for I in Sup:
        company = I.find("span", {"class" : "companyName"}).text
        title = I.find("a", {"class" : "jcs-JobTitle"}).text
        Link = I.find("a", {"class" : "jcs-JobTitle"})["href"]
        Link = "https://www.indeed.com" + Link

        lists2.append({"title" : title, "company" : company, "link" : Link})

    return lists2