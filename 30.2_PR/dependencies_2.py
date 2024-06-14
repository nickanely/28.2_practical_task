import pendulum
from airflow import DAG
from airflow.models.baseoperator import chain_linear, chain
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

with DAG(
        dag_id='dependencies_2',
        start_date=pendulum.today(),
        tags=['Homework_30.2'],
) as dag:
    start = EmptyOperator(task_id='start')

    pick_erp_system = EmptyOperator(task_id='pick_erp_system')
    fetch_sales_new = EmptyOperator(task_id='fetch_sales_new')
    fetch_sales_old = EmptyOperator(task_id='fetch_sales_old', trigger_rule=TriggerRule.DUMMY)
    clean_sales_new = EmptyOperator(task_id='clean_sales_new')
    clean_sales_old = EmptyOperator(task_id='clean_sales_old', trigger_rule=TriggerRule.DUMMY)

    fetch_weather = EmptyOperator(task_id='fetch_weather')
    clean_weather = EmptyOperator(task_id='clean_weather')

    join_datasets = EmptyOperator(task_id='join_datasets', trigger_rule=TriggerRule.ONE_SUCCESS)
    train_model = EmptyOperator(task_id='train_model')
    deploy_model = EmptyOperator(task_id='deploy_model')

    chain(start, pick_erp_system, [fetch_sales_new, fetch_sales_old], [clean_sales_new, clean_sales_old], join_datasets)
    start >> fetch_weather >> clean_weather >> join_datasets
    join_datasets >> train_model >> deploy_model
