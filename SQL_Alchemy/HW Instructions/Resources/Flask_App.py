import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation for the last year"""
    # Set first day included in query
    query_date = '2016-08-18'
    # Query all stations
    precip = session.query(measurement.date, measurement.prcp, measurement.station).filter(measurement.date >= query_date)#.filter(Precip.station == 'USC00511918')

    dates = []
    precipitation = []

    for row in precip:
        dates.append(row[0])
        precipitation.append(row[1])

    precip_dict = dict(zip(dates, precipitation))

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all station names"""
    # Query all stations
    station_list = session.query(station.name).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(station_list))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations for the previous year"""
    # Set first day included in query
    query_date = '2016-08-18'
    # Query all stations
    temp_data = session.query(measurement.date, measurement.tobs, measurement.station).filter(measurement.date >= query_date)#.filter(Precip.station == 'USC00511918')

    dates = []
    tobs = []

    for row in temp_data:
        dates.append(row[0])
        tobs.append(row[1])

    tobs_dict = dict(zip(dates, tobs))

    return jsonify(tobs_dict)


if __name__ == '__main__':
    app.run(debug=True)