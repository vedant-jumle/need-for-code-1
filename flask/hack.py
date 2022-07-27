from genericpath import exists
from flask import Flask, redirect, render_template, request , Response
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
    return render_template('career_paths.ejs' , jobs = jobs , images=[df[job]['job-img'] for job in jobs], length=len(jobs) , des = [df[job]['des'] for job in jobs])

@app.route('/explore/<name>', methods=['GET'])
def career_paths_detail(name):
     return render_template('job.html', des=df[name].des,name=name, skills= df[name].skills, crs = df[name]["rec courses"] , sal=df[name]["starting salary"], img=df[name]["job-img"])



@app.route('/form', methods=['POST'])
def fetch_and_send_details():
    global model_output

    res={
    "Acedamic percentage in Operating Systems": request.form["os_marks"],
    "percentage in Algorithms": request.form["aoa_marks"],
    "Percentage in Programming Concepts": request.form["percentage PC"], #
    "Percentage in Software Engineering": request.form["se_marks"],
    "Percentage in Computer Networks": request.form["cn_marks"],
    "Percentage in Electronics Subjects": request.form["es_marks"],
    "Percentage in Computer Architecture": request.form["coa_marks"],
    "Percentage in Mathematics": request.form["math_marks"],
    "percentage in Communication skills": request.form["comm_marks"],
    "hours working per day": request.form["work_hours"],
    "logical quotient rating": request.form["logic"],
    "hackathons": request.form["hackathons"],
    "coding skill rating": request.form["coding_skills"], #
    "public speaking points": request.form["communication_skills"],
    "can work long time before system?": request.form["long_hours"],
    "self-learning capability?": request.form["self_learner"],
    "Extra-courses did": request.form["extra_curricular"],
    "certifications": request.form["certificates"],
    "workshops": request.form["workshops"],
    "reading and writing skills": request.form["read_write"],
    "memory capability score": request.form["memory"],
    "Interested subjects": request.form["interests"],
    "Interested career area": request.form["career_interests"],
    "Job/Higher Studies?": request.form["future_plans"],
    "Type of company want to settle in?": request.form["company_pref"],
    "Management or techincal": request.form["management_choice"],
    "Salary/work": request.form["work_salary"],
    "hard/smart worker": request.form["hard_smart"],
    "worked in teams ever?": request.form["worked in teams"], #
    "Introvert": request.form["intovert_not"],
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
