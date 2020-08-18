from .powerfactory import LoadFlow


def initialize_routes(api):
    api.add_resource(LoadFlow, '/api/load-flow/<elem_type>')
    # api.add_resource(MovieApi, '/api/movies/<id>')
