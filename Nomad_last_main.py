from flask import Flask, render_template, request, redirect, send_file
from Weworkremotely import extract_job
from indeed import extract_job2
from remoteok import extract_job3
from Savefile import save_to_file

def merge(word="python"):
    Result = []
    Result.extend(extract_job(word))
    Result.extend(extract_job2(word))
    Result.extend(extract_job3(word))

    return Result

app = Flask("Remote Job Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = merge(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        SearchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="0.0.0.0")