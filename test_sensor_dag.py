import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.sensors.sql import SqlSensor

with DAG(
        dag_id='HW_28.2_sensor_dag',
        start_date=pendulum.today(),
        schedule=None,
        tags=['Homework_28.2'],
) as dag:
    start_op = EmptyOperator(task_id='start')

    check_data_sensor_op = SqlSensor(
        task_id='check_for_data',
        conn_id='postgres_local',
        sql='SELECT 1 FROM contacts LIMIT 1;',
        mode='poke',
        poke_interval=60,
        timeout=7 * 24 * 60 * 60,
    )

    end_op = EmptyOperator(task_id='end')

start_op >> check_data_sensor_op >> end_op
