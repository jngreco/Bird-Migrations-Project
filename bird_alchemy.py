# 
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
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

####
# Flask Setup
####
app = Flask(__name__)

####
# Flask Routes
####
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/obs_by_species_and_date/species/start/end<br/>"
    )

# Helper function to convert SQL Alchemy ORM rows to dictionaries
def object_as_dict(row):
    result = {}
    for column in inspect(row).mapper.column_attrs:
        result[column.key] = getattr(row, column.key)
    return result

####
# /api/v1.0/obs_by_species_and_date
# Example URL:  http://127.0.0.1:5000/api/v1.0/obs_by_species_and_date/Bald%20Eagle/2011-01-19/2011-01-20
####  
@app.route("/api/v1.0/obs_by_species_and_date/<species>/<start>/<end>")
def obs_by_species_and_date(species, start, end):

    # Create session from Python to the DB:
    session = Session(engine)

    # Get data for the selected species and date ranges
    bird_data = session.query(Birds).\
        filter(
            Birds.OBSERVATION_DATE >= (start),
            Birds.OBSERVATION_DATE <= (end),
            Birds.COMMON_NAME == (species),
        ).all()

    # Convert each row into a dictionary for jsonify:
    bird_data = [object_as_dict(row) for row in bird_data]

    # bird_data = [row._asdict() for row in bird_data]  # Convert 'Row' objects into dictionaries

    # Close the session as soon as it's no longer needed:
    session.close()

    # Return the JSON representation of your dictionary.
    return jsonify(bird_data)

if __name__ == '__main__':
    app.run(debug=True)

