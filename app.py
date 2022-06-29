import sys
from flask import Flask
from housing.exception import HousingException
from housing.logger import logging


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message) 
        logging.info("We are testing Logging module")
    return "CI/CD PIPELINE ESTABLISHED"

if __name__=="__main__":
    app.run(debug=True)