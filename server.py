from flask import *
from copy import deepcopy
app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home():
    global session
    if "count" in session:
        sess_inst = deepcopy(session)
        sess_inst["count"] += 1
        session = deepcopy(sess_inst)
        return {"count": session["count"]}
    session["count"] = 0
    return {"count": session["count"]}


@app.route('/clear')
def getVariable():
    session.clear()
    return "session cleared"


if __name__ == '__main__':
    app.run(debug=True, port=5003)
