import sys
import time
import ast
import constants
from flask import Response, request, jsonify
from flask_restful import Resource, reqparse

from json import dumps

from methods.pfMethods import terminal_info, line_info, transformer_info, generator_info, load_info, set_load

parser = reqparse.RequestParser()

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
        # if prj is None:
        #     # raise Exception("No project activated. Python Script stopped.")
        #     return Response("No project activated. Python Script stopped.", mimetype="application/json", status=401)

        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        print('Current time: ' + current_time)
        time_as_list = current_time.split(":")
        time_project = int(time_as_list[0])
        if "23:00" <= current_time <= "23:59" or "00:00" <= current_time <= "05:59":
            price = constants.LOW_TARIFF
        elif "16:00" <= current_time <= "22:59":
            price = constants.HIGH_TARIFF
        else:
            price = constants.BASE_TARIFF

        print(time_project)

        prj = prj[int(time_project)]
        prj.Activate()
        print('Activated project name: ' + prj.loc_name)

        # get active project
        prj = pf_app.GetActiveProject()
        if prj is None:
            # raise Exception("No project activated. Python Script stopped.")
            return Response("No project activated. Python Script stopped.", mimetype="application/json", status=401)

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

            generators = pf_app.GetCalcRelevantObjects("*.ElmSym")
            if not generators:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of generators found: %d" % len(generators))

            loads = pf_app.GetCalcRelevantObjects("*.ElmLod")
            if not loads:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of loads found: %d" % len(loads))

            print("Collecting all calculation relevant to terminals..")
            parsed_response['terminals'] = terminal_info(terminals, tension_type, len(terminals))

            print("Collecting all calculation relevant to lines..")
            parsed_response['lines'] = line_info(lines, len(lines))

            print("Collecting all calculation relevant to transformers..")
            parsed_response['transformers'] = transformer_info(transformers, len(transformers))

            print("Collecting all calculation relevant to generators..")
            parsed_response['generators'] = generator_info(generators, tension_type, len(generators))

            print("Collecting all calculation relevant to loads..")
            parsed_response['loads'] = load_info(loads, tension_type, len(loads))

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

        prj.Deactivate()
        parsed_response['cost'] = price
        print("Python Script ended.")

        return Response(dumps(parsed_response), mimetype="application/json", status=200)


class SetLoadFlow(Resource):
    def post(self):
        data = ast.literal_eval(request.data.decode('utf-8'))
        element = list(data.keys())[0]
        value = list(data.values())[0]
        pf_app = pf.GetApplication()
        if pf_app is None:
            # raise Exception("getting PowerFactory application failed")
            return Response("getting PowerFactory application failed", mimetype="application/json", status=401)
        # print to PowerFactory output window
        pf_app.PrintInfo("Python Script started..")

        user = pf_app.GetCurrentUser()
        prj = user.GetContents('*.IntPrj')[0]

        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        print('Current time: ' + current_time)
        time_as_list = current_time.split(":")
        time_project = int(time_as_list[0])
        if "23:00" <= current_time <= "23:59" or "00:00" <= current_time <= "05:59":
            price = constants.LOW_TARIFF
        elif "16:00" <= current_time <= "22:59":
            price = constants.HIGH_TARIFF
        else:
            price = constants.BASE_TARIFF

        print(time_project)

        prj = prj[int(time_project)]
        prj.Activate()
        print('Activated project name: ' + prj.loc_name)

        # get active project
        prj = pf_app.GetActiveProject()
        if prj is None:
            # raise Exception("No project activated. Python Script stopped.")
            return Response("No project activated. Python Script stopped.", mimetype="application/json", status=401)

        if 'Load' in element:
            loads = pf_app.GetCalcRelevantObjects("*.ElmLod")
            if not loads:
                return Response("No lines found", mimetype="application/json", status=401)
            print("Number of loads found: %d" % len(loads))
            set_load(loads, element, value)

        # retrieve load-flow object
        ldf = pf_app.GetFromStudyCase("ComLdf")

        # force balanced load flow
        ldf.iopt_net = 0

        # execute load flow
        ldf.Execute()
        parsed_response = {}

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

        generators = pf_app.GetCalcRelevantObjects("*.ElmSym")
        if not generators:
            return Response("No lines found", mimetype="application/json", status=401)
        print("Number of generators found: %d" % len(generators))

        loads = pf_app.GetCalcRelevantObjects("*.ElmLod")
        if not loads:
            return Response("No lines found", mimetype="application/json", status=401)
        print("Number of loads found: %d" % len(loads))

        print("Collecting all calculation relevant to terminals..")
        parsed_response['terminals'] = terminal_info(terminals, 57.5, len(terminals))

        print("Collecting all calculation relevant to lines..")
        parsed_response['lines'] = line_info(lines, len(lines))

        print("Collecting all calculation relevant to transformers..")
        parsed_response['transformers'] = transformer_info(transformers, len(transformers))

        print("Collecting all calculation relevant to generators..")
        parsed_response['generators'] = generator_info(generators, 57.5, len(generators))

        print("Collecting all calculation relevant to loads..")
        parsed_response['loads'] = load_info(loads, 57.5, len(loads))

        print("All relevant calculations collected")

        prj.Deactivate()
        parsed_response['cost'] = price
        print("Python Script ended.")

        return Response(dumps(parsed_response), mimetype="application/json", status=200)
