import sys
from flask import Response, request, jsonify
from flask_restful import Resource

sys.path.append("C:\\Program Files\\JetBrains\\PyCharm 2020.2\\debug-eggs\\pydevd-pycharm.egg")
sys.path.append("C:\\Program Files (x86)\\DIgSILENT\\PowerFactory 15.1\\python")

import pydevd_pycharm
# connect to PowerFactory
import powerfactory as pf

pydevd_pycharm.settrace('192.168.0.92', port=21000, stdoutToServer=True, stderrToServer=True)


class TensionApi(Resource):
    def get(self):
        pf_app = pf.GetApplicationExt()
        pf_app.show()
        if pf_app is None:
            # raise Exception("getting PowerFactory application failed")
            return Response("getting PowerFactory application failed", mimetype="application/json", status=401)
        # print to PowerFactory output window
        pf_app.PrintInfo("Python Script started..")

        user = app.GetCurrentUser()
        prj = user.GetContents('*.IntPrj')[0]

        # get active project
        # prj = pf_app.GetActiveProject()
        if prj is None:
            # raise Exception("No project activated. Python Script stopped.")
            return Response("No project activated. Python Script stopped.", mimetype="application/json", status=401)

        prj.Activate()
        # retrieve load-flow object
        ldf = pf_app.GetFromStudyCase("ComLdf")

        # force balanced load flow
        ldf.iopt_net = 0

        # execute load flow
        ldf.Execute()

        # collect all relevant terminals
        print("Collecting all calculation relevant terminals..")
        terminals = pf_app.GetCalcRelevantObjects("*.ElmTerm")
        if not terminals:
            # raise Exception("No calculation relevant terminals found")
            return Response("No calculation relevant terminals found", mimetype="application/json", status=401)
        print("Number of terminals found: %d" % len(terminals))

        formatted_voltage = []
        for terminal in terminals:
            voltage = terminal.GetAttribute("m:u")
            print("Voltage at terminal %s is %f p.u." % (terminal, voltage))
            formatted_voltage.append("Voltage at terminal %s is %f p.u." % (terminal, voltage))

        # print to PowerFactory output window
        print("Python Script ended.")
        return Response(formatted_voltage, mimetype="application/json", status=200)
    # def get(self):
    #   movies = Movie.objects().to_json()
    #   return Response(movies, mimetype="application/json", status=200)
    # def post(self):
    #   body = request.get_json()
    #   movie = Movie(**body).save()
    #   id = movie.id
    #   return {'id': str(id)}, 200
    #
    # class MovieApi(Resource):
    #   def put(self, id):
    #     body = request.get_json()
    #     Movie.objects.get(id=id).update(**body)
    #     return '', 200
    #
    #   def delete(self, id):
    #     movie = Movie.objects.get(id=id).delete()
    #     return '', 200
    #
    #   def get(self, id):
    #     movies = Movie.objects.get(id=id).to_json()
    #     return Response(movies, mimetype="application/json", status=200)
