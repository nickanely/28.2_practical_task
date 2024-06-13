import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id='HW_28.2_populate_table_with_postgres_dag',
    start_date=pendulum.today(),
    schedule=None,
    tags=['Homework_28.2'],
) as dag:

    start_op = EmptyOperator(task_id='start')

    populate_contacts_op = PostgresOperator(
        task_id='populate_table',
        sql='SELECT populate_contacts();',
        postgres_conn_id='postgres_local',
    )

    finish_op = EmptyOperator(task_id='finish')

start_op >> populate_contacts_op >> finish_op
