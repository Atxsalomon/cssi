import webapp2

class MainHandler(webbapp2.RequestHandler):
    def get(self):
        self.response.write("welcome to Juan online portal")


app = webapp2.WSGIApplication([
    ('/hello-Juan', MainHandler),
], debug=True)
