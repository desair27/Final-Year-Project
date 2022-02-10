import json
from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('personaldata.html')


if __name__ == '__main__':
    app.run()

# data = open('exampleinput.json','r')

# d = data.read()

# obj = json.loads(d)

# print(str(obj['dpv:PersonalDataHandling'][1]['resource']))
# print(len(obj['dpv:PersonalDataHandling']))

# for x in range(0,len(obj['dpv:PersonalDataHandling'])):
#    print(str(obj['dpv:PersonalDataHandling'][x]['resource']))
