from src.template_renders import template_renders


def setup_routes(app):
    app.router.add_route('GET', '/', template_renders.index, name='index')
    app.router.add_route('GET', '/boxing/', template_renders.boxing_matches, name='boxing_matches')
    app.router.add_route('GET', '/football/', template_renders.football_matches, name='football_matches')