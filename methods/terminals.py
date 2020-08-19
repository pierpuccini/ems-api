import constants


def terminal_info(terminals, tension_type):
    formatted_voltage = {}
    for terminal in terminals:
        voltage_magnitude = terminal.GetAttribute(constants.MAGNITUDE)
        voltage_magnitude_unit = terminal.GetAttributeUnit(constants.MAGNITUDE)
        voltage_line_magnitude = terminal.GetAttribute(constants.LINE_LINE_MAGNITUDE)
        angle = terminal.GetAttribute(constants.ANGLE)
        angle_unit = terminal.GetAttributeUnit(constants.ANGLE)
        ts = terminal.GetContents()
        # print("Voltage at terminal %s is %f p.u." % (terminal.GetNodeName(), voltage))
        # print("Voltage at terminal %s is %f p.u." % (terminal.cDisplayName, voltage))

        # voltage_string = "Voltage at terminal " + terminal.cDisplayName + " is " + str(voltage) + " p.u."
        if tension_type == "all":
            formatted_voltage[terminal.cDisplayName] = {
                'magnitude': {"value": voltage_magnitude, "unit": voltage_magnitude_unit[0]},
                'line': {"value": voltage_line_magnitude, "unit": "kV"},
                'angle': {"value": angle, "unit": angle_unit[0]},
            }
        elif voltage_line_magnitude <= 57.5:
            formatted_voltage[terminal.cDisplayName] = {
                'magnitude': {"value": voltage_magnitude, "unit": voltage_magnitude_unit[0]},
                'line': {"value": voltage_line_magnitude, "unit": "kV"},
                'angle': {"value": angle, "unit": angle_unit[0]},
            }

        print('Terminals formatted')
    return formatted_voltage

