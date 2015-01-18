import requests
from bottle import route, run

# s.headers.update({'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"})
@route('/getID/<file_number>')
def getfilenumber(file_number):
    s = requests.Session()
    s.get('http://kcerds.dol-esa.gov/query/getOrgQry.do') # set session Cookie
    d = s.post('http://kcerds.dol-esa.gov/query/getOrgQryResult.do', data={'fileNumber': file_number})
    return d.text

run(host='localhost', port=8080, debug=True)
