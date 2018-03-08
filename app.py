import os
from bottle import *
import urllib.request, json

@route('/static/<nafn>')
def static(nafn):
    return static_file(nafn,root='./static')

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template("skra1.tpl", data=data,)


@route('/company/<name>')
def index(name):
    strCompanyMin = ""
    dblCompanyMin = 1000.0

    for i in data['results']:
        if dblCompanyMin > float(i['bensin95']):
            dblCompanyMin = i['bensin95']
            strCompanyMin = i['company']
    return template("skra2.tpl", data=data, dblCompanyMin=dblCompanyMin, strCompanyMin=strCompanyMin,name=name)

@error(404)
def error404(error):
    return """villa hefur komid upp"""


#run()
run(host='0.0.0.0',port=os.environ.get('PORT'))

""""""
