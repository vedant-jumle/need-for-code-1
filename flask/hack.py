from genericpath import exists
from flask import Flask, redirect, render_template, request , Response
import json
import pandas as pd
import ML_module

app = Flask(__name__)

req_url = {}
df = pd.read_json('./content/jobless.json')
df1= pd.read_csv('./dataset/career_pred.csv')

print("loading model")
model = ML_module("./models/main.h5")
print("Model loaded")

model_output = None

@app.route('/test/<name>', methods=['GET'])
def test(name):
    print('######################################')
    return render_template('job.html', des=df[name].des,name=name, skills= df[name].skills, crs = df[name]["rec courses"] , sal=df[name]['starting salary'], img=df[name]['job-img'])

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/og_form')
def form_page():
    return render_template('form.ejs')

@app.route('/form', methods=['POST'])
def fetch_and_send_details():
    global model_output

    res={
    "Acedamic percentage in Operating Systems": request.form["Acedamic OS"],
    "percentage in Algorithms": request.form["percentage Algo"],
    "Percentage in Programming Concepts": request.form["percentage PC"],
    "Percentage in Software Engineering": request.form["percentage SE"],
    "Percentage in Computer Networks": request.form["percentage CN"],
    "Percentage in Electronics Subjects": request.form["percentage ES"],
    "Percentage in Computer Architecture": request.form["percentage CA"],
    "Percentage in Mathematics": request.form["percentage Math"],
    "percentage in Communication skills": request.form["percentage in CS"],
    "hours working per day": request.form["hours working per day"],
    "logical quotient rating": request.form["logical quotient rating"],
    "hackathons": request.form["hackathon"],
    "coding skill rating": request.form["coding skill rating"],
    "public speaking points": request.form["public speaking points"],
    "can work long time before system?": request.form["can work ltbs"],
    "self-learning capability?": request.form["self learning capability"],
    "Extra-courses did": request.form["extra-courses"],
    "certifications": request.form["certification"],
    "workshops": request.form["workshops"],
    "reading and writing skills": request.form["reading and writing"],
    "memory capability score": request.form["memory capability score"],
    "Interested subjects": request.form["Interested subjects"],
    "Interested career area": request.form["Interested career areas"],
    "Job/Higher Studies?": request.form["job/Higer education"],
    "Type of company want to settle in?": request.form["type of company"],
    "Management or techincal": request.form["Management or techincal"],
    "Salary/work": request.form["Salary/work"],
    "hard/smart worker": request.form["hard/smart worker"],
    "worked in teams ever?": request.form["worked in teams"],
    "Introvert": request.form["Introverted"],
    }

    new_res = {}

    for key in res.keys():
        new_res[key.lower()] = res[key]

    model_output = model.process(new_res)

    return redirect("/form/career")

@app.route("/form/career")
def career():
    global model_output

    return render_template("final_career.ejs", outputs=model_output)

if __name__=='__main__':
    app.run(host='0.0.0.0' , port=6969, debug=True)
