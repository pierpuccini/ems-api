import constants
import time


def terminal_info(terminals, tension_type, total_terminals):
    formatted_terminals = {'$total': total_terminals}
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
                'reactive_gen': {"value": reactive_gen, "unit": reactive_gen_unit[0]}
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
                'reactive_gen': {"value": reactive_gen, "unit": reactive_gen_unit[0]}
            }

    print('Terminals formatted')
    return formatted_terminals


def line_info(lines, total_lines):
    formatted_lines = {'$total': total_lines}
    for line in lines:
        loading = line.GetAttribute(constants.LOADING)
        loading_unit = line.GetAttributeUnit(constants.LOADING)

        max_loading = line.GetAttribute(constants.MAX_LOADING)
        max_loading_unit = line.GetAttributeUnit(constants.MAX_LOADING)

        formatted_lines[line.loc_name] = {
            'loading': {"value": loading, "unit": loading_unit[0]},
            'max_loading': {"value": max_loading, "unit": max_loading_unit[0]}
        }

    print('Lines formatted')
    return formatted_lines


def transformer_info(transformers, total_transformers):
    formatted_transformers = {'$total': total_transformers}
    for transformer in transformers:
        loading = transformer.GetAttribute(constants.LOADING)
        loading_unit = transformer.GetAttributeUnit(constants.LOADING)

        max_loading = transformer.GetAttribute(constants.MAX_LOADING)
        max_loading_unit = transformer.GetAttributeUnit(constants.MAX_LOADING)

        formatted_transformers[transformer.loc_name] = {
            'loading': {"value": loading, "unit": loading_unit[0]},
            'max_loading': {"value": max_loading, "unit": max_loading_unit[0]}
        }

    print('Transformers formatted')
    return formatted_transformers


def generator_info(generators, tension_type, total_generators):
    formatted_generators = {'$total': total_generators}
    for generator in generators:
        loading = generator.GetAttribute(constants.LOADING)
        loading_unit = generator.GetAttributeUnit(constants.LOADING)

        active_power = generator.GetAttribute(constants.ACTIVE_POWER)
        active_power_unit = generator.GetAttributeUnit(constants.ACTIVE_POWER)

        reactive_power = generator.GetAttribute(constants.REACTIVE_POWER)
        reactive_power_unit = generator.GetAttributeUnit(constants.REACTIVE_POWER)

        formatted_generators[generator.loc_name] = {
            'loading': {"value": loading, "unit": loading_unit[0]},
            'active_power': {"value": active_power, "unit": active_power_unit[0]},
            'reactive_power': {"value": reactive_power, "unit": reactive_power_unit[0]}
        }

    print('Generators formatted')
    return formatted_generators


def load_info(loads, tension_type, total_loads):
    formatted_loads = {'$total': total_loads}
    for load in loads:
        nominal_active_power = load.GetAttribute(constants.NOM_ACTIVE_POWER)
        nominal_active_power_unit = load.GetAttributeUnit(constants.NOM_ACTIVE_POWER)

        nominal_reactive_power = load.GetAttribute(constants.NOM_REACTIVE_POWER)
        nominal_reactive_power_unit = load.GetAttributeUnit(constants.NOM_REACTIVE_POWER)

        nominal_voltage = load.GetAttribute(constants.NOM_VOLTAGE)
        nominal_voltage_unit = load.GetAttributeUnit(constants.NOM_VOLTAGE)

        formatted_loads[load.loc_name] = {
            'nominal_active_power': {"value": nominal_active_power, "unit": nominal_active_power_unit[0]},
            'nominal_reactive_power': {"value": nominal_reactive_power, "unit": nominal_reactive_power_unit[0]},
            'nominal_voltage': {"value": nominal_voltage, "unit": nominal_voltage_unit[0]}
        }

    print('Loads formatted')
    return formatted_loads


def set_load(loads, load_to_set, value):
    for load in loads:
        if load.loc_name == load_to_set:
            load.plini = value
    return loads

