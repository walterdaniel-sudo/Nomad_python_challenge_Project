import csv
import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr/"

def create_csv(company, link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    rows = soup.find("tbody").find_all("tr")
    jobs = []

    for row in rows:
        localHtml = row.find("td", {"class": "local first"})
        local = ""
        if localHtml is not None:
            local = localHtml.text
        titleHtml = row.find("span", {"class": "title"})
        title = ""
        if titleHtml is not None:
            title = titleHtml.text
        dataHtml = row.find("td", {"class" : "data"})
        data = ""
        if dataHtml is not None:
            data = dataHtml.text
        payHtml = row.find("td", {"class" : "pay"})
        pay = ""
        if payHtml is not None:
            pay = payHtml.text
        regDateHtml = row.find("td", {"class" : "regDate last"})
        regDate = ""
        if regDateHtml is not None:
            regDate = regDateHtml.text

        if local != '' and title != '' and data != '' and pay != '' and regDate != '':
            job = [local, title, data, pay, regDate]
            jobs.append(job)

        company = company.replace("/", "n")
        file = open(company+".csv", mode="w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
        for job in jobs:
            writer.writerow(job)
            print(job)

def extract_Info():
    lists=[]
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    goodsBox = soup.find_all("li", {"class" : "impact"})
    # 회사명
    for row in goodsBox: 
        company = row.find("span", { "class":"company"}).text
        link = row.find("a")["href"]
        lists.append({'company' : company, 'link' : link})
        create_csv(company, link)

extract_Info()