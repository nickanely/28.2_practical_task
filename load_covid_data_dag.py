import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='HW_28.2_load_covid_data_dag',
    start_date=pendulum.today(),
    schedule=None,
    tags=['Homework_28.2'],
) as dag:
    start_op = EmptyOperator(task_id='start')

    load_data_op = BashOperator(
        task_id='load_data',
        bash_command='curl -o /tmp/covid_regions.json https://covid-api.com/api/regions',
    )

    finish_op = EmptyOperator(task_id='finish')


start_op >> load_data_op >> finish_op
