import os

import pandas as pd
import numpy as np
import re

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bk.db"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Samples = Base.classes.link

stmt = db.session.query(Samples).statement
df = pd.read_sql_query(stmt, db.session.bind)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/samples")
def samples():
    """Return `Transaction` and `Item`."""
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df
    df['Date'] = df['Date'].str.strip()
    # Format the data to send as json
    data = {
        "item": sample_data.Item.tolist(),
        "date": sample_data.Date.tolist(),
        "time": sample_data.Time.tolist(),
        "transaction": sample_data.Transection.tolist()
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()