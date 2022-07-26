from flask import Flask, redirect, request , Response
import json


app = Flask(__name__)

req_url = {}



@app.route('/s', methods=['GET'])
def helloworld():
    res= {"name" : request.form["name"],
    "lastname": request.form["lastname"]} 

    return redirect('http://192.168.136.213:6969')
    # return Response(json.dumps(res),
    # mimetype='application/json')

    #return 'maza ayega'
    # return Response(response=json.dumps(
    #         {"error": str(e)}),
    #         status=500, mimetype="application/json")

@app.route('/', methods=['Get'])
def get_post_form_data():
    return 'yo'

@app.route('/new', methods=['GET'])
def send_to_page():
    return redirect('https://learn-anything.xyz/')

@app.route('/', methods=['POST'])
def fetch_and_send_details():
    res={"Acedamic OS": request.form["Acedamic OS"],
    "percentage Algo": request.form["percentage Algo"],
    "percentage PC": request.form["percentage PC"],
    "percentage SE": request.form["percentage SE"],
    "percentage CN": request.form["percentage CN"],
    "percentage ES": request.form["percentage ES"],
    "percentage CA": request.form["percentage CA"],
    "percentage Math": request.form["percentage Math"],
    "percentage in CS": request.form["percentage in CS"],
    "hours working per day": request.form["hours working per day"],
    "logical quotient rating": request.form["logical quotient rating"],
    "hackathone": request.form["hackathone"],
    "coding skill rating": request.form["coding skill rating"],
    "public speaking points": request.form["public speaking points"],
    "can work ltbs": request.form["can work ltbs"],
    "self learning capability": request.form["self learning capability"],
    "extra-courses": request.form["extra-courses"],
    "certification": request.form["certification"],
    "workshops": request.form["workshops"],
    "takenttests": request.form["takenttests"],
    "olympiads": request.form["olympiads"],
    "reading and writing": request.form["reading and writing"],
    "memory capability score": request.form["memory capability score"],
    "Interested subjects": request.form["Interested subjects"],
    "Interested career areas": request.form["Interested career areas"],
    "job/Higer education": request.form["job/Higer education"],
    "type of company": request.form["type of company"],
    "taken inputs from seniors": request.form["taken inputs from seniors"],
    "interested in games": request.form["interested in games"],
    "interested type of Books": request.form["interested type of Books"],
    "Salary range": request.form["Salary range"],
    "expected in a relationship": request.form["expected in a relationship"],
    "gentle or tuff behaviour": request.form["gentle or tuff behaviour"],
    "Management or techincal": request.form["Management or techincal"],
    "Salary": request.form["Salary"],
    "hard/smart worker": request.form["hard/smart worker"],
    "worked in teams": request.form["worked in teams"],
    "Introverted": request.form["Introverted"],
    }
    return Response(json.dumps(res),
    mimetype='application/json')

if __name__=='__main__':
    app.run(host='0.0.0.0' , port=6969, debug=True)
