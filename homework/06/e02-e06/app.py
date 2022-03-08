from flask import Flask
import datetime
from htmlhelper import generate_html_page

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)
date = datetime.datetime.now()

# if url is in root
@app.route("/date")
def hello_world():
    return generate_html_page("Date", date)

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
