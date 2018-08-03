import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("welcome to Juan online portal")


app = webapp2.WSGIApplication([
    ('/hello-juan', MainHandler),
], debug=True)
