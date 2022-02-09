from flask import Flask, request, Response
import dbinteractions as db
import json

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

app.run(debug=True)