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

####
# /api/v1.0/obs_by_species_and_date
####  
@app.route("/api/v1.0/obs_by_species_and_date/species/start/end")
def obs_by_species_and_date(species, start, end):

    # Create session from Python to the DB:
    session = Session(engine)

    # Get data for the selected species and date ranges
    # 
    # Returns a list of tuples, like this:
    # [('2016-08-24', 0.08), ('2016-08-24', 2.15), ('2016-08-24', 2.28), ...
    bird_data = session.query(Birds.COMMON_NAME, Birds.OBSERVATION_DATE, Birds.LATITUDE, Birds.LONGITUDE).\
        filter(
            Birds.OBSERVATION_DATE >= (start),
            Birds.OBSERVATION_DATE <= (end),
            Birds.COMMON_NAME
        ).order_by(Birds.OBSERVATION_DATE).all()

    # Close the session as soon as it's no longer needed:
    session.close()

    # Convert list of tuples to a dictionary:
    birds_dict = {}
    birds_dict = dict(bird_data)
    print(bird_data)

    # Return the JSON representation of your dictionary.
    return jsonify(bird_data)

if __name__ == '__main__':
    app.run(debug=True)

# obs_by_species_and_date("Bald Eagle", "2011-01-19", "2011-01-20")

