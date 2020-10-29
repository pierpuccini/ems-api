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
        num_customer = load.GetAttribute(constants.NUM_CUSTOMERS)
        num_customer_unit = load.GetAttributeUnit(constants.NUM_CUSTOMERS)

        nominal_active_power = load.GetAttribute(constants.NOM_ACTIVE_POWER)
        nominal_active_power_unit = load.GetAttributeUnit(constants.NOM_ACTIVE_POWER)

        nominal_reactive_power = load.GetAttribute(constants.NOM_REACTIVE_POWER)
        nominal_reactive_power_unit = load.GetAttributeUnit(constants.NOM_REACTIVE_POWER)

        nominal_voltage = load.GetAttribute(constants.NOM_VOLTAGE)
        nominal_voltage_unit = load.GetAttributeUnit(constants.NOM_VOLTAGE)

        formatted_loads[load.loc_name] = {
            'num_customer': {"value": num_customer, "unit": num_customer_unit[0]},
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


def set_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print('Current time: ' + current_time)
    if "00:00" < current_time <= "00:59":
        time_project = 0
    elif "01:00" <= current_time <= "01:59":
        time_project = 1
    elif "02:00" <= current_time <= "02:59":
        time_project = 2
    elif "03:00" <= current_time <= "03:59":
        time_project = 3
    elif "04:00" <= current_time <= "04:59":
        time_project = 4
    elif "05:00" <= current_time <= "05:59":
        time_project = 5
    elif "06:00" <= current_time <= "06:59":
        time_project = 6
    elif "07:00" <= current_time <= "07:59":
        time_project = 7
    elif "08:00" <= current_time <= "08:59":
        time_project = 8
    elif "09:00" <= current_time <= "09:59":
        time_project = 9
    elif "10:00" <= current_time <= "10:59":
        time_project = 10
    elif "11:00" <= current_time <= "11:59":
        time_project = 11
    elif "12:00" <= current_time <= "12:59":
        time_project = 12
    elif "13:00" <= current_time <= "13:59":
        time_project = 13
    elif "14:00" <= current_time <= "14:59":
        time_project = 14
    elif "15:00" <= current_time <= "15:59":
        time_project = 15
    elif "16:00" <= current_time <= "16:59":
        time_project = 16
    elif "17:00" <= current_time <= "17:59":
        time_project = 17
    elif "18:00" <= current_time <= "18:59":
        time_project = 18
    elif "19:00" <= current_time <= "19:59":
        time_project = 19
    elif "20:00" <= current_time <= "20:59":
        time_project = 20
    elif "21:00" <= current_time <= "21:59":
        time_project = 21
    elif "22:00" <= current_time <= "22:59":
        time_project = 22
    elif "23:00" <= current_time <= "23:59":
        time_project = 23
    else:
        time_project = 0

    return time_project
