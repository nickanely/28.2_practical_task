from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from pendulum import datetime

with DAG(
        dag_id='weekly_dag',
        # to-do statement is a bit ambiguous 'starting from 15th of June'
        # if you have ment that first dag run should be on 15th of June then
        # start date down here should be 2024.6.14
        start_date=datetime(2024, 6, 15),
        schedule_interval='@weekly',
        end_date=datetime(2024, 7, 13),
        tags=['Homework_30.2'],
) as dag:
    start_op = EmptyOperator(task_id='start')

    task_op = BashOperator(
        task_id='run_task',
        bash_command='echo "Running task weekly"',
    )

    end_op = EmptyOperator(task_id='end')

start_op >> task_op >> end_op
