import constants


def terminal_info(terminals, tension_type):
    formatted_terminals = {}
    for terminal in terminals:
        voltage_magnitude = terminal.GetAttribute(constants.MAGNITUDE)
        voltage_magnitude_unit = terminal.GetAttributeUnit(constants.MAGNITUDE)

        voltage_line_magnitude = terminal.GetAttribute(constants.LINE_LINE_MAGNITUDE)

        angle = terminal.GetAttribute(constants.ANGLE)
        angle_unit = terminal.GetAttributeUnit(constants.ANGLE)

        active_out = terminal.GetAttribute(constants.ACTIVE_OUTGOING)
        active_out_unit = terminal.GetAttributeUnit(constants.ACTIVE_OUTGOING)

        reactive_out = terminal.GetAttribute(constants.REACTIVE_OUTGOING)
        reactive_out_unit = terminal.GetAttributeUnit(constants.REACTIVE_OUTGOING)

        active_flow = terminal.GetAttribute(constants.ACTIVE_POWER_FLOW)
        active_flow_unit = terminal.GetAttributeUnit(constants.ACTIVE_POWER_FLOW)

        reactive_flow = terminal.GetAttribute(constants.REACTIVE_POWER_FLOW)
        reactive_flow_unit = terminal.GetAttributeUnit(constants.REACTIVE_POWER_FLOW)

        active_gen = terminal.GetAttribute(constants.ACTIVE_GENERATION)
        active_gen_unit = terminal.GetAttributeUnit(constants.ACTIVE_GENERATION)

        reactive_gen = terminal.GetAttribute(constants.REACTIVE_GENERATION)
        reactive_gen_unit = terminal.GetAttributeUnit(constants.REACTIVE_GENERATION)

        if tension_type == "all":
            formatted_terminals[terminal.loc_name] = {
                'magnitude': {"value": voltage_magnitude, "unit": voltage_magnitude_unit[0]},
                'line': {"value": voltage_line_magnitude, "unit": "kV"},
                'angle': {"value": angle, "unit": angle_unit[0]},
                'active_out': {"value": active_out, "unit": active_out_unit[0]},
                'reactive_out': {"value": reactive_out, "unit": reactive_out_unit[0]},
                'active_flow': {"value": active_flow, "unit": active_flow_unit[0]},
                'reactive_flow': {"value": reactive_flow, "unit": reactive_flow_unit[0]},
                'active_gen': {"value": active_gen, "unit": active_gen_unit[0]},
                'reactive_gen': {"value": reactive_gen, "unit": reactive_gen_unit[0]},
            }
        elif voltage_line_magnitude <= 57.5:
            formatted_terminals[terminal.loc_name] = {
                'magnitude': {"value": voltage_magnitude, "unit": voltage_magnitude_unit[0]},
                'line': {"value": voltage_line_magnitude, "unit": "kV"},
                'angle': {"value": angle, "unit": angle_unit[0]},
                'active_out': {"value": active_out, "unit": active_out_unit[0]},
                'reactive_out': {"value": reactive_out, "unit": reactive_out_unit[0]},
                'active_flow': {"value": active_flow, "unit": active_flow_unit[0]},
                'reactive_flow': {"value": reactive_flow, "unit": reactive_flow_unit[0]},
                'active_gen': {"value": active_gen, "unit": active_gen_unit[0]},
                'reactive_gen': {"value": reactive_gen, "unit": reactive_gen_unit[0]},
            }

        print('Terminals formatted')
    return formatted_terminals


def line_info(lines, tension_type):
    formatted_lines = {}
    for line in lines:
        v_line_line = line.GetAttribute(constants.LINE_LINE_MAGNITUDE_LINES)
        v_line_line_unit = line.GetAttributeUnit(constants.LINE_LINE_MAGNITUDE_LINES)

        current_magnitude = line.GetAttribute(constants.CURRENT_MAGNITUDE)
        current_magnitude_unit = line.GetAttributeUnit(constants.CURRENT_MAGNITUDE)

        active_power = line.GetAttribute(constants.ACTIVE_POWER)
        active_power_unit = line.GetAttributeUnit(constants.ACTIVE_POWER)

        reactive_power = line.GetAttribute(constants.REACTIVE_POWER)
        reactive_power_unit = line.GetAttributeUnit(constants.REACTIVE_POWER)

        total_active_power = line.GetAttribute(constants.TOTAL_ACTIVE_POWER)
        total_active_power_unit = line.GetAttributeUnit(constants.TOTAL_ACTIVE_POWER)

        total_reactive_power = line.GetAttribute(constants.TOTAL_REACTIVE_POWER)
        total_reactive_power_unit = line.GetAttributeUnit(constants.TOTAL_REACTIVE_POWER)

        active_power_losses = line.GetAttribute(constants.ACTIVE_LOSSES_TOTAL)
        active_power_losses_unit = line.GetAttributeUnit(constants.ACTIVE_LOSSES_TOTAL)

        reactive_power_losses = line.GetAttribute(constants.REACTIVE_LOSSES_TOTAL)
        reactive_power_losses_unit = line.GetAttributeUnit(constants.REACTIVE_LOSSES_TOTAL)

        if tension_type == "all":
            formatted_lines[line.loc_name] = {
                'line_voltage': {"value": v_line_line, "unit": v_line_line_unit[0]},
                'current': {"value": current_magnitude, "unit": current_magnitude_unit[0]},
                'active': {"value": active_power, "unit": active_power_unit[0]},
                'reactive': {"value": reactive_power, "unit": reactive_power_unit[0]},
                'total_active': {"value": total_active_power, "unit": total_active_power_unit[0]},
                'total_reactive': {"value": total_reactive_power, "unit": total_reactive_power_unit[0]},
                'active_losses': {"value": active_power_losses, "unit": active_power_losses_unit[0]},
                'reactive_losss': {"value": reactive_power_losses, "unit": reactive_power_losses_unit[0]},
            }
        elif voltage_line_magnitude <= 57.5:
            formatted_lines[line.loc_name] = {
                'line_voltage': {"value": v_line_line, "unit": v_line_line_unit[0]},
                'current': {"value": current_magnitude, "unit": current_magnitude_unit[0]},
                'active': {"value": active_power, "unit": active_power_unit[0]},
                'reactive': {"value": reactive_power, "unit": reactive_power_unit[0]},
                'total_active': {"value": total_active_power, "unit": total_active_power_unit[0]},
                'total_reactive': {"value": total_reactive_power, "unit": total_reactive_power_unit[0]},
                'active_losses': {"value": active_power_losses, "unit": active_power_losses_unit[0]},
                'reactive_losss': {"value": reactive_power_losses, "unit": reactive_power_losses_unit[0]},
            }

        print('Terminals formatted')
    return formatted_lines
