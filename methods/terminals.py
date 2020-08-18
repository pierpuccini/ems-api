def terminal_info(pf_app):
    terminals = pf_app.GetCalcRelevantObjects("*.ElmTerm")
    if not terminals:
        # raise Exception("No calculation relevant terminals found")
        return Response("No calculation relevant terminals found", mimetype="application/json", status=401)
    print("Number of terminals found: %d" % len(terminals))

    formatted_voltage = []
    for terminal in terminals:
        voltage = terminal.GetAttribute("m:u")

        print("Voltage at terminal %s is %f p.u." % (terminal.GetNodeName(), voltage))
        print("Voltage at terminal %s is %f p.u." % (terminal.cDisplayName, voltage))

        voltage_string = "Voltage at terminal " + terminal.cDisplayName + " is " + str(voltage) + " p.u."

        formatted_voltage.append(voltage_string)
    return formatted_voltage

