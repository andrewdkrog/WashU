import os

import pandas as pd
import numpy as np

import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bk.db"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Samples = Base.classes.link


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/samples")
def samples():
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    df['Date'] = df['Date'].str.strip()
    data = df
    print(data)
    return data.to_json(orient='records', lines=True)

@app.route("/daily")
def daily():
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    data = df
    df['Date'] = df['Date'].str.strip()
    customers = data.groupby(['Date'])['Transection'].max().reset_index()
    customers.columns = ['Date','Cumulative Customers']
    customers['Daily Customers'] = customers['Cumulative Customers'].diff()
    customers.iloc[0,2] = customers.iloc[0,1]
    
    return customers.to_json(orient='records', lines=True)

@app.route("/hourly")
def hourly():
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    data = df
    df['Date'] = df['Date'].str.strip()
    data["Time"] = pd.to_datetime(data["Time"])
    data["Hour"] = data["Time"].dt.hour
    data["Date"] = pd.to_datetime(data["Date"])

    data["Day_of_Week"] = data["Date"].dt.weekday_name
    days = {'Sunday':'Weekend', 'Monday':'Weekday', 'Tuesday':'Weekday', 'Wednesday':'Weekday',
        'Thursday':'Weekday', 'Friday':'Weekday', 'Saturday':'Weekend'}

    data['Weekend'] = data['Day_of_Week'].apply(lambda x: days[x])
    hourly = data.groupby(['Hour'])['Transection'].count().reset_index()
    
    return hourly.to_json(orient='records', lines=True)

if __name__ == "__main__":
    app.run()