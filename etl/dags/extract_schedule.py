from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import urllib.request
import ujson


def get_schedule():
    """
    Gets the schedule data for the day.
    """

    '''Build URL'''
    # base URL
    url = "http://statsapi.mlb.com/api/v1/schedule?"
    # sportId = 1 for MLB
    url += "sportId=1"
    # date in the required format
    url += "&date=" + datetime.today().strftime('%Y-%m-%d')

    '''Get requested data'''
    with urllib.request.urlopen(url) as raw_json:
        clean_json = ujson.loads(raw_json.read().decode("latin-1"))

    '''Store in MongoDB and return for testing purposes'''
    return clean_json


default_args = {

}