import os
import cherrypy

config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080
    }
}


class App:

    @cherrypy.expose
    def hello(self):
        try:
            apikey = cherrypy.request.headers['api-key']
        except KeyError:
            apikey = ""
        if apikey == '2b230ad96f21329b24ead2fc48cb451644631c4e':
            if cherrypy.request.method == 'GET':
                 return "{'data:', 'GET'}"
            if cherrypy.request.method == 'POST':
                 return "{'data:', 'POST'}"
            return "{'error:', 'invalid method'}"
        else:
            return "{'error:', 'invalid key'}"

    @cherrypy.expose
    def upload(self, ufile):
        upload_path = os.path.dirname(__file__)
        upload_filename = 'saved.txt'
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(ufile.filename, size, ufile.content_type, data)
        return out


if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)
