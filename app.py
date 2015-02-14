import bottle
from bottle import route, template

app = application = bottle.default_app()

@route('/')
def index():
    return template('<h1>{{message}}</h1>', message='Hello Runabove!')