from genericpath import exists
from datasets import tqdm
from django.shortcuts import render
from flask import Flask, jsonify, redirect, render_template, request , Response
import json
from matplotlib import image
import pandas as pd
from sklearn import datasets
import jinja2
env = jinja2.Environment()
env.globals.update(zip=zip)
import ML_module

app = Flask(__name__)

req_url = {}
df = pd.read_json('./content/jobless.json')
df1= pd.read_csv('./dataset/career_pred.csv')

print(len(df.keys()), len(df1["suggested job role"].unique()))
print("loading model")
model = ML_module.CareerAdvisor("./models/main.h5")
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

# @app.route('/testlist', methods=['GET'])
# def testlist():
#     return render_template('testlist.html', data=df.to_json())

# @app.route('/testlist', methods=['POST'])
# def testlist1():
#     print(request.form)
#     ret={"v1": [request.form['v1']]}
#     print('\n\n',ret,'\n\n')
#     return Response(json.dumps(ret),
#     mimetype='application/json')

@app.route('/explore', methods=['GET'])
def career_paths():
    # jobs = df1['suggested job role'].unique().tolist()
    jobs = list(df.keys())
    return render_template('career_paths.ejs' , jobs = jobs , images=[df[job]['job-img'] for job in jobs], length=len(jobs))

@app.route('/explore/<name>', methods=['GET'])
def career_paths_detail(name):
     return render_template('job.html', des=df[name].des,name=name, skills= df[name].skills, crs = df[name]["rec courses"] , sal=df[name]["starting salary"], img=df[name]["job-img"])



@app.route('/form', methods=['POST'])
def fetch_and_send_details():
    global model_output

    res={
    "Acedamic percentage in Operating Systems": int(request.json["os_marks"]),
    "percentage in Algorithms": int(request.json["aoa_marks"]),
    "Percentage in Programming Concepts": int(request.json["pc_marks"]), #
    "Percentage in Software Engineering": int(request.json["se_marks"]),
    "Percentage in Computer Networks": int(request.json["cn_marks"]),
    "Percentage in Electronics Subjects": int(request.json["es_marks"]),
    "Percentage in Computer Architecture": int(request.json["coa_marks"]),
    "Percentage in Mathematics": int(request.json["math_marks"]),
    "percentage in Communication skills": int(request.json["comm_marks"]),
    "hours working per day": request.json["work_hours"],
    "logical quotient rating": request.json["logic"],
    "hackathons": request.json["hackathons"],
    "coding skills rating": request.json["coding_skills"], #
    "public speaking points": request.json["communication_skills"],
    "can work long time before system?": request.json["long_hours"],
    "self-learning capability?": request.json["self_learner"],
    "Extra-courses did": request.json["extra_curricular"],
    "certifications": request.json["certificates"].lower().split(","),
    "workshops": request.json["workshops"].lower().split(","),
    "reading and writing skills": request.json["read_write"],
    "memory capability score": request.json["memory"],
    "Interested subjects": request.json["interests"].lower().split(","),
    "Interested career area": request.json["career_interests"].lower().split(","),
    "Job/Higher Studies?": request.json["future_plans"],
    "Type of company want to settle in?": request.json["company_pref"].lower().split(","),
    "Management or technical": request.json["management_choice"],
    "Salary/work": request.json["work_salary"],
    "hard/smart worker": request.json["hard_smart"],
    "worked in teams ever?": request.json["team_before"], #
    "Introvert": request.json["intovert_not"],
    }

    new_res = {}

    for key in res.keys():
        new_res[key.lower()] = res[key]

    model_output = model.process(new_res)
    print(model_output)
    return render_template("final_career.ejs", outputs=model_output)

@app.route("/form/career")
def career():
    global model_output

    return render_template("final_career.ejs", outputs=model_output)

if __name__=='__main__':
    app.run(host='0.0.0.0' , port=6969, debug=True)
