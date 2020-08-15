from .powerfactory import TensionApi


def initialize_routes(api):
    api.add_resource(TensionApi, '/api/tension')
    # api.add_resource(MovieApi, '/api/movies/<id>')
