import flask, flask.views, os, send_sms

app = flask.Flask(__name__)

app.secret_key = "GenericKey" 

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        to = flask.request.form['to']
        body = flask.request.form['body']

        send_sms.text(to, body)
        return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


