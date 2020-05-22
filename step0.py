from werkzeug.wrappers import Response,request

def application(environ,stat_response):
	request = Request(environ)
	text = 'hello %s!'% request.args.get('name','world')
	response=response(text,mimetype='text/plain')
	return response(environ,stat_response)
	