import pytest
import json
from flask import Flask,render_template
from collections import defaultdict
pytest.main()
app=Flask(__name__)
p=defaultdict(list)

@app.route("/home")
def home():
    with open("data.txt","r") as wrt:
        data=wrt.readlines()
    for i in data:
        k=i.split(" ")
        p["api"].append(k[0])
        p["result"].append(k[1])
    return render_template("home.html",ps=p)

if __name__=="__main__":
    app.run(debug=True)
