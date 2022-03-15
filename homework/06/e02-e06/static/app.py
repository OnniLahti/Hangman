from flask import Flask
from fruithelper import generate_fruit

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/slot-machine")
def hello_world():
    fruit1 = generate_fruit
    fruit2 = generate_fruit
    fruit3 = generate_fruit
    return f"{fruit1}{fruit2}{fruit3}"

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)