from .movie import MoviesApi, MovieApi

def initialize_routes(api):
 api.add_resource(MoviesApi, '/movies')
 api.add_resource(MovieApi, '/movies/<id>')