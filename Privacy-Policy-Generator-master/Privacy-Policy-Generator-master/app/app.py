import flask
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename, escape
from description import Description
from view import View
from bs4 import BeautifulSoup
import datetime
import json
import re
import os
import sys
cookie = []
#i = 0
z = 0
x = 0
y = 0
j = 0
v = 0
purposes = []
recipients = []
tomeasures = []
risks = []
data = {
    "dpv:DataController": {
        "resource": "",
        "schema:name": "",
        "schema:legalName": "",
        "schema:address": "",
        "schema:email": "",
        "schema:url": "",
        "schema:telephone": ""
    },
    "dpv:PersonalDataHandling": [

    ],
    "dpv:Purpose": [

    ],
    "dpv:Recipient": [

    ],
    "dpv:TechnicalOrganisationalMeasure": [

    ],
    "dpv:Risk": [

    ],
    "Cookie": [

    ]
}

app = Flask(__name__)

BASE_PATH = os.path.dirname(__file__)

if(sys.platform == "win32"):
    json_path = os.path.join(BASE_PATH, "static\input.json")
    sample_path = os.path.join(BASE_PATH, "static\inputExample.json")
    blank_path = os.path.join(BASE_PATH, "static\input-skeleton.json")
else:
    json_path = os.path.join(BASE_PATH, "static/input.json")
    sample_path = os.path.join(BASE_PATH, "static/input.json")
    blank_path = os.path.join(BASE_PATH, "static/input-skeleton.json")

def is_json(file_name):
    return file_name.lower().split(".")[1] == "json"

@app.route('/', methods=['GET'])
def home():

    return render_template('home.html')

@app.route('/sample',methods=['GET'])
def sample():
    return render_template('sample-policy.html')

@app.route('/jsongenerator',methods=['POST','GET'])

def json():
    global cookie
    if request.method=='POST':
        import json
        data['dpv:DataController']["resource"]= request.form["dc1"]
        data['dpv:DataController']["schema:name"] = request.form["dc2"]
        data['dpv:DataController']["schema:legalName"]= request.form["dc3"]
        data['dpv:DataController']["schema:address"] = request.form["dc4"]
        data['dpv:DataController']["schema:email"] = request.form["dc5"]
        data['dpv:DataController']["schema:url"] = request.form["dc6"]
        data['dpv:DataController']["schema:telephone"] = request.form["dc7"]
        pdc = request.form["pdc"]
        cookies = request.form["cookies"]
        #print(pdc)
        pd = pdc.split(',')
        cookie = cookies.split(',')
        count = 1
        #print(pd[1])
        for i in pd:
            data['dpv:PersonalDataHandling'].append({
                "resource": "PDH" + str(count),
                "dpv:hasPersonalDataCategory": i,
                "dpv:hasDataController": "",
                "dpv:hasDataSubject": "",
                "dpv:hasPurpose": [],
                "dpv:hasProcessing": [],
                "dpv:hasRecipient": [],
                "dpv:hasTechnicalOrganisationalMeasure": [],
                "dpv:hasLegalBasis": [],
                "dpv:hasRisk": [],
                "dpv:Collect": [],
                "dpv:StorageDuration": "",
                "dpv:StorageLocation": ""
            })
            count = count + 1
        count = 1
        for i in cookie:
            data['Cookie'].append({
                "resource": "Cookie" + str(count),
                "schema:name": i,
                "dpv:hasPersonalDataCategory": [],
                "dpv:hasPurpose": "",
                "schema:description": "",
                "Provenance": ""
            })
            count = count + 1
        #eg = json.dumps(data, indent=2, separators=(',', ': '))
        #print(eg)
        return redirect(url_for("json1",c=0))

    else:
        return render_template('jsongen.html')
@app.route('/jsongenerator1',methods=['POST','GET'])

def json1():
    global z
    #if click submit then if end of list go next page else go to next part of list and gather data from there
    if request.method=='POST':


        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasDataController"] = request.form["a"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasDataSubject"] = request.form["b"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasPurpose"] = request.form["c"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasProcessing"] = request.form["d"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasRecipient"] = request.form["e"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasTechnicalOrganisationalMeasure"] = request.form["f"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasLegalBasis"] = request.form["g"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasRisk"] = request.form["risk"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:Collect"] = request.form["h"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:StorageDuration"] = request.form["i"]
        data['dpv:PersonalDataHandling'][int(z)-1]["dpv:StorageLocation"] = request.form["j"]

        purposes.extend(data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasPurpose"].split(','))
        recipients.extend(data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasRecipient"].split(','))
        tomeasures.extend(data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasTechnicalOrganisationalMeasure"].split(','))
        risks.extend(data['dpv:PersonalDataHandling'][int(z)-1]["dpv:hasRisk"].split(','))
        #eg = json.dumps(data, indent=2, separators=(',', ': '))
        #print(eg)

        return redirect(url_for("json1"))

    else:
        count = 1
        import json
        z = z + 1
        if(z >= len(data["dpv:PersonalDataHandling"])+1):
            purpose = list(dict.fromkeys(purposes))
            recipient = list(dict.fromkeys(recipients))
            tomeasure = list(dict.fromkeys(tomeasures))
            risk = list(dict.fromkeys(risks))
            #print(purpose)
            for i in purpose:
                data['dpv:Purpose'].append({
                    "dpv:hasPurpose": i,
                    "dpv:hasProcessing": [],
                    "dpv:hasPersonalDataCategory": [],
                    "dpv:hasLegalBasis": []
                })

            for i in recipient:
                data['dpv:Recipient'].append({
                    "resource": i,
                    "schema:name": "",
                    "schema:address": "",
                    "schema:description": "",
                    "schema:phoneNumber": ""
                })
            for i in tomeasure:
                data['dpv:TechnicalOrganisationalMeasure'].append({
                    "resource": "safetyMeasure" + str(count),
                    "schema:name": i,
                    "schema:description": "",
                    "dpv:hasPersonalDataCategory": []
                })
                count = count + 1
            count = 1
            for i in risk:
                data['dpv:Risk'].append({
                    "resource": "Risk" + str(count),
                    "schema:name": i,
                    "dpv:hasPersonalDataCategory": []
                })
                count = count + 1
            count = 1
            #print(json.dumps(data, indent=2, separators=(',', ': ')))
            return redirect(url_for("json2"))
        else:
            return render_template('jsongenpdc.html', cat=data['dpv:PersonalDataHandling'][z-1]["dpv:hasPersonalDataCategory"])



@app.route('/jsongenerator2',methods=['POST','GET'])
def json2():
    global x

    tmp = []
    if request.method == 'POST':
        data['dpv:Purpose'][int(x) - 1]["dpv:hasProcessing"] = request.form["a"]
        data['dpv:Purpose'][int(x) - 1]["dpv:hasLegalBasis"] = request.form["b"]
        #print(request.form["b"])


        return redirect(url_for("json2"))
    else:
        import json
        for i in range(len(list(dict.fromkeys(purposes)))):
            for j in range(len(data["dpv:PersonalDataHandling"])):
                if list(dict.fromkeys(purposes))[i] in data["dpv:PersonalDataHandling"][j]["dpv:hasPurpose"]:
                    tmp.append(data["dpv:PersonalDataHandling"][j]["dpv:hasPersonalDataCategory"])
                data["dpv:Purpose"][i]["dpv:hasPersonalDataCategory"] = tmp
            tmp = []

        if (x >= len(data["dpv:Purpose"])):
            for a in range(len(list(dict.fromkeys(risks)))):
                for b in range(len(data["dpv:PersonalDataHandling"])):
                    if list(dict.fromkeys(risks))[a] in data["dpv:PersonalDataHandling"][b]["dpv:hasRisk"]:
                        tmp.append(data["dpv:PersonalDataHandling"][b]["dpv:hasPersonalDataCategory"])
                    data["dpv:Risk"][a]["dpv:hasPersonalDataCategory"] = tmp
                tmp = []
            return redirect(url_for("json3"))
        else:
            x = x + 1
            return render_template('jsongenpurp.html', cat=data["dpv:Purpose"][x - 1]["dpv:hasPurpose"])


@app.route('/jsongenerator3',methods=['POST','GET'])

def json3():
    global y


    if request.method == 'POST':
        data['dpv:Recipient'][int(y) - 1]["schema:name"] = request.form["a"]
        data['dpv:Recipient'][int(y) - 1]["schema:address"] = request.form["b"]
        data['dpv:Recipient'][int(y) - 1]["schema:description"] = request.form["c"]
        data['dpv:Recipient'][int(y) - 1]["schema:phoneNumber"] = request.form["d"]




        return redirect(url_for("json3"))
    else:


        if (y >= len(data["dpv:Recipient"])):

            return redirect(url_for("json4"))
        else:
            y = y + 1
            print(y)
            return render_template('jsongenrecip.html', cat=data["dpv:Recipient"][y - 1]["resource"])


@app.route('/jsongenerator4',methods=['POST','GET'])
def json4():
    global j

    tmp = []
    if request.method == 'POST':
        #data['Cookie'][int(j) - 1]["resource"] = equest.form["a"]r
        data['Cookie'][int(j) - 1]["dpv:hasPersonalDataCategory"] = request.form["a"]
        data['Cookie'][int(j) - 1]["dpv:hasPurpose"] = request.form["b"]
        data['Cookie'][int(j) - 1]["schema:description"] = request.form["c"]
        data['Cookie'][int(j) - 1]["Provenance"] = request.form["d"]

        #print(request.form["b"])


        return redirect(url_for("json4"))
    else:
        import json

        if (j >= len(data["Cookie"])):

            return redirect(url_for("json5"))
        else:
            j = j + 1
            return render_template('jsongencookie.html', cat=data["Cookie"][j - 1]["schema:name"])

@app.route('/jsongenerator5',methods=['POST','GET'])
def json5():
    global v

    tmp = []
    if request.method == 'POST':
        #data['Cookie'][int(j) - 1]["resource"] = equest.form["a"]r
        data['dpv:TechnicalOrganisationalMeasure'][int(v) - 1]["schema:description"] = request.form["a"]




        return redirect(url_for("json4"))
    else:
        import json
        for i in range(len(list(dict.fromkeys(tomeasures)))):
            for j in range(len(data["dpv:PersonalDataHandling"])):
                if list(dict.fromkeys(tomeasures))[i] in data["dpv:PersonalDataHandling"][j]["dpv:hasTechnicalOrganisationalMeasure"]:
                    tmp.append(data["dpv:PersonalDataHandling"][j]["dpv:hasPersonalDataCategory"])
                data["dpv:TechnicalOrganisationalMeasure"][i]["dpv:hasPersonalDataCategory"] = tmp
            tmp = []

        if (v >= len(data["dpv:TechnicalOrganisationalMeasure"])):
            print(json.dumps(data, indent=2, separators=(',', ': ')))
            return redirect(url_for("home"))
        else:
            v = v + 1
            return render_template('jsongentomeasure.html', cat=data["dpv:TechnicalOrganisationalMeasure"][v - 1]["schema:name"])





@app.route('/download/<file_name>')
def download_file(file_name):

    file_name = escape(file_name)
    if file_name == "inputExample.json":
        return send_file(sample_path,as_attachment=True)
    elif file_name == "input-skeleton.json":
        return send_file(blank_path,as_attachment=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if(request.method == 'POST'):
        f = request.files['file']
        if f and is_json(f.filename): #If file is valid save it
            f.save(json_path)

    return redirect((url_for('policy')))

@app.errorhandler(FileNotFoundError)
def no_file(e):
    return redirect((url_for('home')))


@app.route('/policy', methods=['GET','POST'])
def policy():
    import json
    dta = {}

    date = datetime.date.today()
    date = date.strftime("%B %d, %Y")

    with open(json_path) as f:
        dta = json.load(f)

    dta["date"] = date

    collect_set = set()
    process_set = set()

    data_classes = []
    purposes= []

    #Creating sets of different data,purpose,collection and processing catagories
    for cat in dta["dpv:PersonalDataHandling"]:
        collect_set.update(cat["dpv:Collect"])
        process_set.update(cat["dpv:hasProcessing"])
        data_classes.append(cat["dpv:hasPersonalDataCategory"])

    for purp in dta["dpv:Purpose"]:
         purposes.append(purp["dpv:hasPurpose"])

    collect_view = View.create_collect_view(dta, collect_set)

    #Assigning personal data categories to the relevant recipients
    for recip in dta["dpv:Recipient"]:
        recip["PersonalDataCategory"] = set()
        for cat in dta["dpv:PersonalDataHandling"]:
            for cat_recip in cat["dpv:hasRecipient"]:
                if cat_recip == recip["resource"]:
                    recip["PersonalDataCategory"].add(cat["dpv:hasPersonalDataCategory"])

    dpvDescriptions = Description.descriptions(data_classes)
    dpvDescriptions.update(Description.descriptions(purposes))

    topics = [{"heading": "Overview", "page": "Overview.html"},
              {"heading": "Personal Data View", "page": "Data-View.html"},
              {"heading": "Data Collection View", "page": "Collect-View.html"},
              {"heading": "Purpose View", "page": "Purpose-View.html"},
              {"heading": "Data Sharing View", "page": "Share-View.html"},
              {"heading": "Safety Measure View", "page": "TOMeasure-View.html"},
              {"heading": "Risk View", "page": "Risk-View.html"},
              {"heading": "Cookies", "page": "cookies.html"},
              {"heading": "Rights", "page": "Rights.html"}]

    os.remove(json_path)

    return render_template('policy.html',
                           topics=topics,
                           data=dta,
                           dpv=dpvDescriptions,
                           purposes=purposes,
                           collect=collect_view)


if __name__ == '__main__':
    app.run(debug=True)
