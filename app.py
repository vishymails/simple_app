from flask import Flask, render_template, request, jsonify
import os
import numpy as np

import yaml
import joblib
import json

webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root,"templates")

params_path = "params.yaml"


app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def read_params(config_path) :
    with open(config_path) as yaml_file :
        config = yaml.safe_load(yaml_file)
    return config


def predict(data) :
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction



@app.route("/", methods= ["GET", "POST"])
def index() :
    if request.method == "POST" :
        try :
            if request.form :
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", response= response)
            elif request.json :
                pass
        except Exception as e :
            print(e)
            error = {"error" : "Something went wrong !! try again"}
            error = {"error" : e}

            return render_template("404.html", error=error)
    else :
        return render_template("index.html")

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000, debug=True)

