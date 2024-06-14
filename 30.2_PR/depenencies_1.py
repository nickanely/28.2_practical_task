import pendulum
from airflow import DAG
from airflow.models.baseoperator import chain_linear
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id='dependencies_1',
        start_date=pendulum.today(),
        tags=['Homework_30.2'],
) as dag:
    task_A = EmptyOperator(task_id='task_A')
    task_B = EmptyOperator(task_id='task_B')
    task_C = EmptyOperator(task_id='task_C')
    task_D = EmptyOperator(task_id='task_D')
    task_E = EmptyOperator(task_id='task_E')
    task_F = EmptyOperator(task_id='task_F')
    task_G = EmptyOperator(task_id='task_G')
    task_H = EmptyOperator(task_id='task_H')

chain_linear(
    [task_A, task_B, task_C],
    [task_D, task_E, task_F],
    [task_G, task_H],
)
