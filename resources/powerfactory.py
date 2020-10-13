import sys
import time
from flask import Response, request, jsonify
from flask_restful import Resource

from json import dumps

from methods.pfMethods import terminal_info, line_info, transformer_info, generator_info, load_info

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

        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        print(current_time)
        time_project = project
        # TODO: CHANGE TIME PROJECT IN ORDER TO MATCH PROPER PROJECT
        if current_time > "6:00" & current_time < "11:59":
            time_project = 0
        elif current_time > "12:00" & current_time < "17:59":
            time_project = 0
        elif current_time > "18:00" & current_time < "5:59":
            time_project = 0
        prj[int(time_project)].Activate()
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

            transformers = pf_app.GetCalcRelevantObjects("*.ElmTr2")
            if not transformers:
                return Response("No transformers found", mimetype="application/json", status=401)
            print("Number of transformers found: %d" % len(transformers))

            print("Collecting all calculation relevant to terminals..")
            parsed_response['terminals'] = terminal_info(terminals, tension_type, len(terminals))

            print("Collecting all calculation relevant to lines..")
            parsed_response['lines'] = line_info(lines, len(lines))

            print("Collecting all calculation relevant to transformers..")
            parsed_response['transformers'] = transformer_info(lines, len(transformers))

            print("All relevant calculations collected")
        elif elem_type == 'terminals':
            terminals = pf_app.GetCalcRelevantObjects("*.ElmTerm")
            if not terminals:
                return Response("No terminals found", mimetype="application/json", status=401)
            print("Number of terminals found: %d" % len(terminals))

            print("Collecting all calculation relevant to terminals..")
            parsed_response['terminals'] = terminal_info(terminals, tension_type, len(terminals))
            print("All relevant calculations to terminals collected")
        elif elem_type == 'lines':
            lines = pf_app.GetCalcRelevantObjects("*.ElmLne")
            if not lines:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of lines found: %d" % len(lines))

            print("Collecting all calculation relevant to lines..")
            parsed_response['lines'] = line_info(lines, len(lines))
            print("All relevant calculations to lines collected")
        elif elem_type == 'transformers':
            transformers = pf_app.GetCalcRelevantObjects("*.ElmTr2")
            if not transformers:
                return Response("No transformers found", mimetype="application/json", status=401)
            print("Number of transformers found: %d" % len(transformers))

            print("Collecting all calculation relevant to lines..")
            parsed_response['transformers'] = transformer_info(transformers, len(transformers))
            print("All relevant calculations to transformers collected")
        elif elem_type == 'generators':
            generators = pf_app.GetCalcRelevantObjects("*.ElmSym")
            if not generators:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of generators found: %d" % len(generators))

            print("Collecting all calculation relevant to generators..")
            parsed_response['generators'] = generator_info(generators, tension_type, len(generators))
            print("All relevant calculations to generators collected")
        elif elem_type == 'loads':
            loads = pf_app.GetCalcRelevantObjects("*.ElmLod")
            if not loads:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of loads found: %d" % len(loads))

            print("Collecting all calculation relevant to loads..")
            parsed_response['loads'] = load_info(loads, tension_type, len(loads))
            print("All relevant calculations to loads collected")

        # print to PowerFactory output window
        print("Python Script ended.")
        prj[int(project)].Deactivate()

        return Response(dumps(parsed_response), mimetype="application/json", status=200)

