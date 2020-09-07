import constants


def terminal_info(terminals, tension_type, total_terminals):
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
                'total': total_terminals
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
                'total': total_terminals
            }

        print('Terminals formatted')
    return formatted_terminals


def line_info(lines, total_lines):
    formatted_lines = {}
    for line in lines:
        loading = line.GetAttribute(constants.LOADING)
        loading_unit = line.GetAttributeUnit(constants.LOADING)

        max_loading = line.GetAttribute(constants.MAX_LOADING)
        max_loading_unit = line.GetAttributeUnit(constants.MAX_LOADING)

        formatted_lines[line.loc_name] = {
            'loading': {"value": loading, "unit": loading_unit[0]},
            'max_loading': {"value": max_loading, "unit": max_loading_unit[0]},
            'total': total_lines
        }

        print('Lines formatted')
    return formatted_lines


def transformer_info(transformers, total_transformers):
    formatted_transformers = {}
    for transformer in transformers:
        loading = transformer.GetAttribute(constants.LOADING)
        loading_unit = transformer.GetAttributeUnit(constants.LOADING)

        max_loading = transformer.GetAttribute(constants.MAX_LOADING)
        max_loading_unit = transformer.GetAttributeUnit(constants.MAX_LOADING)

        formatted_transformers[transformer.loc_name] = {
            'loading': {"value": loading, "unit": loading_unit[0]},
            'max_loading': {"value": max_loading, "unit": max_loading_unit[0]},
            'total': total_transformers
        }

        print('Transformers formatted')
    return formatted_transformers
