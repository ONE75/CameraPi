config = {
    'description': 'A web API to control cameras using gphoto2',
    'author': 'Reza Mahmood',
    'url': 'http://www.rezamahmood.net',   
    'author_email': 'reza@rezamahmood.net',
    'version': '0.1',   
    'name': 'CameraPi',
	'usbresetpath': '/home/pi/usbreset',
	'bottle_staticfilepath' : '/home/pi/python/projects/web/cameraweb/static',
	'bottle_port' : 8080,
	'bottle_debug': True,
	'bottle_reloader': True,
	'bottle_ip' : 'localhost'
}
