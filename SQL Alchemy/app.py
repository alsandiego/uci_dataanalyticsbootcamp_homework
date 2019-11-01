import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import pandas as pd
import datetime as dt
from datetime import datetime

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate the date 1 year ago from the last data point in the database
    # get the latestdate from the data and then deduct 365 days from it
    latestdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prev12monthdate = datetime.strptime(latestdate[0], '%Y-%m-%d') - dt.timedelta(days=365)

    """ Perform a query to retrieve the data and precipitation scores """
    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > prev12monthdate).all()

    """ put data on list and then dictionary to make a dataframe """
    prcp_date=[]
    prcp_record=[]
    for data in precip:
        prcp_date.append(data.date)
        prcp_record.append(data.prcp)
    prcp_dict={'Date':prcp_date,'Precip Data':prcp_record}


    session.close()


    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()
        
    session.close()
    
    # Create a dictionary
    all_stations = []
    for data in results:
        all_stations.append(data.station)
    
    station_dict={'Stations':all_stations}
    
    return jsonify(station_dict)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date 1 year ago from the last data point in the database
    # get the latestdate from the data and then deduct 365 days from it
    latestdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prev12monthdate = datetime.strptime(latestdate[0], '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query all stations
    temps = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > prev12monthdate).all()

    temp_tobs=[]
    temp_date=[]
    for temp in temps:
        temp_tobs.append(temp.tobs)
        temp_date.append(temp.date)
    tobs_dict={'Date':temp_date, 'Tobs Data':temp_tobs}
        
    session.close()
    
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def calc_temps(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate the date 1 year ago from the last data point in the database
    # get the latestdate from the data and then deduct 365 days from it
    latestdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prev12monthdate = datetime.strptime(latestdate[0], '%Y-%m-%d') - dt.timedelta(days=365)
    
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()


    return jsonify(prcp_dict)

if __name__ == '__main__':
    app.run(debug=True)