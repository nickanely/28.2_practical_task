import pendulum
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='HW_28.2_email_notification',
    start_date=pendulum.today(),
    schedule=None,
    tags=['Homework_28.2'],
) as dag:
    start_op = EmptyOperator(task_id='start')

    email_op = EmailOperator(
        task_id='send_email',
        to='some_email',
        subject='Airflow Task Update',
        html_content='This is an automated email to notify you about the Airflow task status.',
        email_conn_id='email_to_send',
    )

    finish_op = EmptyOperator(task_id='finish')

    start_op >> email_op >> finish_op
