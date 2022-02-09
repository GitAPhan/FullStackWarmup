from flask import Flask, request, Response
import dbinteractions as db
import json
import sys

app = Flask(__name__)

@app.get('/hero')
def get_hero():
    heros = db.get_hero_db()

    heros_json = json.dumps(heros, default=str)

    return Response(heros_json, mimetype="application/json", status=200)

@app.get('/villian')
def get_villian():
    villians = db.get_villian_db()

    villians_json = json.dumps(villians, default=str)

    return Response(villians_json, mimetype="application/json", status=200)

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print("You must pass a mode to run this python script. Either 'testing' or 'production'")
    exit() 

if mode == "testing":
    print("running in testing mode!")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == "production":
    print("running in production mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5005)
else:
    print("Please run with either 'testing' or 'production'")
    exit()