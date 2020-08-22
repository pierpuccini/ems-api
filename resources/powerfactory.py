import sys
from flask import Response, request, jsonify
from flask_restful import Resource

from json import dumps

from methods.pfMethods import terminal_info, line_info

sys.path.append("C:\\Program Files (x86)\\DIgSILENT\\PowerFactory 15.1\\python")

# connect to PowerFactory
import powerfactory as pf


class LoadFlow(Resource):
    def get(self, project, elem_type, tension_type):
        pf_app = pf.GetApplication()
        if pf_app is None:
            # raise Exception("getting PowerFactory application failed")
            return Response("getting PowerFactory application failed", mimetype="application/json", status=401)
        # print to PowerFactory output window
        pf_app.PrintInfo("Python Script started..")

        user = pf_app.GetCurrentUser()
        prj = user.GetContents('*.IntPrj')[0]

        # get active project
        # prj = pf_app.GetActiveProject()
        if prj is None:
            # raise Exception("No project activated. Python Script stopped.")
            return Response("No project activated. Python Script stopped.", mimetype="application/json", status=401)

        prj[int(project)].Activate()
        # retrieve load-flow object
        ldf = pf_app.GetFromStudyCase("ComLdf")

        # force balanced load flow
        ldf.iopt_net = 0

        # execute load flow
        ldf.Execute()
        parsed_response = {}
        if elem_type == 'all':
            # collect all relevant terminals, lines
            terminals = pf_app.GetCalcRelevantObjects("*.ElmTerm")
            if not terminals:
                # raise Exception("No calculation relevant terminals found")
                return Response("No terminals found", mimetype="application/json", status=401)
            print("Number of terminals found: %d" % len(terminals))

            lines = pf_app.GetCalcRelevantObjects("*.Elmlne")
            if not lines:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of lines found: %d" % len(lines))

            print("Collecting all calculation relevant to terminals..")
            parsed_response['terminals'] = terminal_info(terminals, tension_type)

            print("Collecting all calculation relevant to lines..")
            parsed_response['lines'] = line_info(lines, tension_type)

            print("All relevant calculations collected")
        elif elem_type == 'terminals':
            terminals = pf_app.GetCalcRelevantObjects("*.ElmTerm")
            if not terminals:
                return Response("No terminals found", mimetype="application/json", status=401)
            print("Number of terminals found: %d" % len(terminals))

            print("Collecting all calculation relevant to terminals..")
            parsed_response['terminals'] = terminal_info(terminals, tension_type)
            print("All relevant calculations to terminals collected")
        elif elem_type == 'lines':
            lines = pf_app.GetCalcRelevantObjects("*.ElmLne")
            if not lines:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of lines found: %d" % len(lines))

            print("Collecting all calculation relevant to lines..")
            parsed_response['lines'] = line_info(lines, tension_type)
            print("All relevant calculations to terminals collected")

        # print to PowerFactory output window
        print("Python Script ended.")
        prj[int(project)].Deactivate()

        return Response(dumps(parsed_response), mimetype="application/json", status=200)
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
