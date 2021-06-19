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