import requests
import os

while 1:
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
    URL = input().split(",")
    Result = []

    for j in URL:
        URL_strip = j.strip()
        Result.append(URL_strip)

    for i in Result:
        try:
            if "." not in i:
                print(f"{i} is not a vaild URL")
            else:
                if "https://" in i:
                    response = requests.get(i)
                    if response.status_code == 200:
                        print(f"{i} is up!")
                    else:
                        print(f"{i} is down!")
                elif "https://" not in i:
                    i = "https://"+i
                    response = requests.get(i)
                    if response.status_code == 200:
                        print(f"{i} is up!")
                    else:
                        print(f"{i} is down!")
        except requests.exceptions.ConnectionError:
            print(f"{i} is down!!")

    print("Do you want to start over? y/n")
    yorn = str(input())

    if yorn == "y":
        os.system("cls")
        continue
    elif yorn == "n":
        print("k. bye!")
        break