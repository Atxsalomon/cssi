import webapp2
from google.appengine.api import urlfetch
import json
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

class DormTemp(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('template/dorm.html')
        self.response.write(template.render())
        
app = webapp2.WSGIApplication([
    ('/dorm', DormTemp),
    ])
