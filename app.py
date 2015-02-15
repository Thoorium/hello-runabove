import bottle
from bottle import template

# Run bottle internal test server when invoked directly ie: non-uxsgi mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
# Run bottle in application mode. Required in order to get the application working with uWSGI!
else:
    app = application = bottle.default_app()

@app.route('/')
def index():
    return template('<h1>{{message}}</h1>', message='Hello Runabove!')