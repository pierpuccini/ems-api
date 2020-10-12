import sys
from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes

sys.path.append("C:\\Program Files\\JetBrains\\PyCharm 2020.2\\debug-eggs\\pydevd-pycharm.egg")

app = Flask(__name__)

api = Api(app)
initialize_routes(api)

@app.route('/')
def hello():
    return 'Api started'


if __name__ != '__main__':
    print('main')
    import pydevd_pycharm

    pydevd_pycharm.settrace('192.168.0.92', port=21000, stdoutToServer=True, stderrToServer=True)

app.run(host='0.0.0.0')

