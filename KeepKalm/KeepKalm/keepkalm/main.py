import webapp2
import jinja2
import os

jinja_env =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class KeepKalm(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('/templates/index.html')
        ()
        self.response.write(t.render())

    def post(self):
        t = jinja_env.get_template('/templates/index.html')
        self.response.write(t.render())

class Response(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('/templates/index.html')
        seed_data()
        self.response.write(t.render())

    def post(self):
        option=self.request.get('option')
        option2=self.request.get('option2')
        option3=self.request.get('option3')
        option4=self.request.get('option4')
        option5=self.request.get('option5')


        d = {'option':option,'option2':option2,'option3':option3,'option4':option4,'option5':option5}
        t = jinja_env.get_template('/templates/result.html')
        self.response.write(t.render(d))


class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template('templates/front.html')
        self.response.write(welcome_template.render({'animate': True}))  # the response

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template('templates/front.html')
        self.response.write(welcome_template.render({'animate': False}))  # the response


app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/welcome', WelcomePage),
        ('/keepkalm', KeepKalm),
        ('/response', Response),
        ], debug=True)
