import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8")
    wirter = csv.writer(file)
    wirter.writerow(["Title", "Company", "Link"])
    for job in jobs:
        wirter.writerow(list(job.values()))
    return