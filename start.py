# Author Z
import tornado.web
from controllers import home

settings = {
    "template_path":"views",
    "static_path":"statics",
    'static_url_prefix':'/statics/',
}

application = tornado.web.Application([
    (r"/index/(?P<page>\d*)",home.IndexHandler),
],**settings)

if __name__ == '__main__':
    application.listen(8005)
    tornado.ioloop.IOLoop.instance().start()