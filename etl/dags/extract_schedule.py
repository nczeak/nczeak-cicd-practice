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


def get_games():
    """
    Gets the games for the day.
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

dag = DAG(
    dag_id="extract",
    default_args=default_args,
    start_date=datetime(2021, 6, 1)
)

extract_schedule_task = PythonOperator(
    python_callable=get_schedule,
    dag=dag
)

schedule_to_games_task = PythonOperator(
    python_callable=get_games,
    dag=dag
)

extract_schedule_task >> schedule_to_games_task