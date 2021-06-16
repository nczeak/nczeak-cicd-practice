from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pytest import CaptureFixture


def test_get_schedule(capsys: CaptureFixture):
    """

    """

    ''''''
    def hello():
        with capsys.disabled():
            print("Hello, world!")

    dag = DAG(
        "hello_world",
        description="test",
        schedule_interval='*/1 * * * *',
        start_date=datetime(2021, 6, 16)
    )

    dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

    hello_operator = PythonOperator(task_id='hello_task', python_callable=hello, dag=dag)

    dummy_operator >> hello_operator