from .powerfactory import LoadFlow, SetLoadFlow


def initialize_routes(api):
    # project: index of the desired project to load
    # elem_type: type of element to review, terminals, lines, generators, transformers, loads (tr2, tr1)
    # tension_type: 'all' tension levels or only medium tension (57.5kv)
    api.add_resource(LoadFlow, '/api/load-flow/<project>/<elem_type>/<tension_type>')
    api.add_resource(SetLoadFlow, '/api/load-flow/set-point')
