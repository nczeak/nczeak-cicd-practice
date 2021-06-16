from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def get_schedule():
    """
    Gets the schedule data for the day.
    """


default_args = {

}