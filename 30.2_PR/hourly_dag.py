import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id='hourly_dag',
        # logic here: dag is scheduled from 9:00 to 17:00
        # first dag will be triggered at 11:00 and last at 19:00
        # logic here is intentionally different from previous task's logic
        start_date=pendulum.datetime(2024, 6, 17),
        schedule_interval='0 9-17/2 * * 1-5',
        tags=['Homework_30.2'],
        catchup=False,
) as dag:
    start_op = EmptyOperator(task_id='start')

    task_op = BashOperator(
        task_id='run_task',
        bash_command='echo "Running task in every 2 hours on working days"',
    )

    end_op = EmptyOperator(task_id='end')

start_op >> task_op >> end_op
