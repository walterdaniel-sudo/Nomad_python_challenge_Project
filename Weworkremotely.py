import requests
from bs4 import BeautifulSoup


def extract_job(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}&button="

    lists = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    container = soup.find("div", {"class" : "jobs-container"}).find_all("section", {"class", "jobs"})

    for J in container:
        final = J.find_all("li", {"class" : "feature"})
        for I in final:
            title = I.find("span", {"class" : "title"}).text
            company = I.find("span", {"class" : "company"}).text
            Link = I.find("span", {"class" : "company"}).parent["href"]
            Link = "https://weworkremotely.com" + Link

            lists.append({"title" : title, "company" : company, "link" : Link})

    return lists