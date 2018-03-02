from bottle import *
import urllib.request, json
@route('/static/<nafn>')
def static(nafn):
    return static_file(nafn,root='./static')

with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template("skra1.tpl", data=data)

#run()
run(host='0.0.0.0',port=os.environ.get('PORT'))
""""""
