import web
from gothonweb import *

urls = (
        '/game', 'GameEngine',
        '/', 'Index',
)

app = web.application(urls, globals())

class Index(object):
    def GET(self):
        pass
        
class GameEngine(object):
    def GET(self):
        pass

    def POST(self):
        pass

if __name__ == "__main__":
    app.run()
    # code...
