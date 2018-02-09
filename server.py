from bottle import route, run, template, request, static_file
from main import *
import os


game_info = start_web()
# game = mouse_path()

@route('/')
def index():
	return template('views/index', table = game_info) #, game=path_data)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('static/img/:path#.+#')
def send_static(filename):
    return static_file(filename, root='static/img') 
	
run(host='localhost', port=8080, debug=True, reloader=True)