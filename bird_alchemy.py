# 
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import datetime as dt

####
# SQL Alchemy ORM initilization
####
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///data/birds_db")
# 
# Reflect an existing database into a new model
Base = automap_base()
# 
# Reflect the tables
Base.prepare(autoload_with=engine)
# 
# Save references to each table
Birds = Base.classes.birds
Birdmetadata = Base.classes.birdmetadata

####
# Flask Setup
####
app = Flask(__name__)
CORS(app)
####
# Flask Routes
####
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/obs_by_name_and_date/common_name/start/end<br/>"
        f"/api/v1.0/metadata_by_name/common_name<br/>"
        f"/api/v1.0/all_data_dates/start/end<br/>"
    )

####
#DATE RANGE STRINGS
#2015: 2015-01-01/2015-12-31
#2016: 2016-01-01/2016-12-31
#2017: 2017-01-01/2017-12-31
#2018: 2018-01-01/2018-12-31
#2019: 2019-01-01/2019-12-31
#2020: 2020-01-01/2020-12-31
####

# Helper function to convert SQL Alchemy ORM rows to dictionaries
def object_as_dict(row):
    result = {}
    for column in inspect(row).mapper.column_attrs:
        result[column.key] = getattr(row, column.key)
    return result

####
# /api/v1.0/obs_by_name_and_date
# Example URL:  http://127.0.0.1:5000/api/v1.0/obs_by_name_and_date/Bald%20Eagle/2011-01-19/2011-01-20
####  
@app.route("/api/v1.0/all_data_dates/<start>/<end>")
def all_data_dates(start, end):

    # Create session from Python to the DB:
    session = Session(engine)

    # Get data for the selected common_name and date ranges
    results = session.query(Birds.BIRD_INDEX ,Birds.COMMON_NAME, Birds.LONGITUDE, Birds.LATITUDE).\
        filter(
            Birds.OBSERVATION_DATE >= (start),
            Birds.OBSERVATION_DATE <= (end),
        ).all()

    # Convert each row into a dictionary for jsonify:
    bird_data = []
    for result in results:
        bird_dict = {}
        bird_dict["Bird Index"] = result[0]
        bird_dict["Common Name"] = result[1]
        bird_dict["Longitude"] = result[2]
        bird_dict["Latitude"] = result[3]
        bird_data.append(bird_dict)
    #bird_data = [object_as_dict(row) for row in bird_data]

    # Close the session as soon as it's no longer needed:
    session.close()

    # Return the JSON representation of your dictionary.
    return jsonify(bird_data)


####
# /api/v1.0/obs_by_name_and_date
# Example URL:  http://127.0.0.1:5000/api/v1.0/obs_by_name_and_date/Bald%20Eagle/2011-01-19/2011-01-20
####  
@app.route("/api/v1.0/obs_by_name_and_date/<common_name>/<start>/<end>")
def obs_by_name_and_date(common_name, start, end):

    # Create session from Python to the DB:
    session = Session(engine)

    # Get data for the selected common_name and date ranges
    bird_data = session.query(Birds).\
        filter(
            Birds.OBSERVATION_DATE >= (start),
            Birds.OBSERVATION_DATE <= (end),
            Birds.COMMON_NAME == (common_name),
        ).all()

    # Convert each row into a dictionary for jsonify:
    bird_data = [object_as_dict(row) for row in bird_data]

    # Close the session as soon as it's no longer needed:
    session.close()

    # Return the JSON representation of your dictionary.
    return jsonify(bird_data)

####
# /api/v1.0/metadata_by_name
# Example URL:  http://127.0.0.1:5000/api/v1.0/metadata_by_name/Bald%20Eagle
####  
@app.route("/api/v1.0/metadata_by_name/<common_name>")
def metadata_by_name(common_name):

    # Create session from Python to the DB:
    session = Session(engine)

    # Get data for the selected common_name and date ranges
    bird_data = session.query(Birdmetadata).\
        filter(
            Birdmetadata.COMMON_NAME == (common_name)
        ).all()

    # Convert each row into a dictionary for jsonify:
    bird_data = [object_as_dict(row) for row in bird_data]

    # Close the session as soon as it's no longer needed:
    session.close()

    # Return the JSON representation of your dictionary.
    return jsonify(bird_data)

if __name__ == '__main__':
    app.run(debug=True)

