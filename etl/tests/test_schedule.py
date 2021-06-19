from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pytest import CaptureFixture
import os
import sys
# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from dags.extract_schedule import get_schedule


def test_get_schedule(capsys: CaptureFixture):
    """

    """

    ''''''
    test_op = PythonOperator(task_id="test", python_callable=get_schedule)
    result = test_op.execute(context={})
    with capsys.disabled():
        print(result)