import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


def _populate_contacts():
    pg_hook = PostgresHook(postgres_conn_id='postgres_local')
    pg_hook.run('SELECT populate_contacts();')


with DAG(
        dag_id='HW_28.2_populate_table_with_python_dag',
        start_date=pendulum.today(),
        schedule=None,
        tags=['Homework_28.2'],
) as dag:
    start_op = EmptyOperator(task_id='start')

    load_data_op = PythonOperator(
        task_id='trigger_function',
        python_callable=_populate_contacts,
    )

    end_op = EmptyOperator(task_id='end')

start_op >> load_data_op >> end_op
