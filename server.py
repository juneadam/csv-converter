"""
A server file for a CSV to JSON converter
"""
# from model import db
from flask import Flask, render_template
# redirect, request, flash, session
import jinja2
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")



if __name__ == "__main__":
    # from model import connect_to_db
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)