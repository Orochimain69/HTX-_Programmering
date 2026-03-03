import flask


#app = flask.Flask(__name__)
app = flask.Flask(__name__, template_folder='my_templates')


@app.route("/")

def index():
    name = 'Emil'
    return flask.render_template(
        'Webserver.html',
        show_name=name,
        )

app.run()