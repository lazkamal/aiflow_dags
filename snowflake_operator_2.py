import airflow
from airflow import DAG
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from datetime import timedelta, datetime


dag = DAG(
    'snowflake_operator_2',
    start_date=datetime(2021, 1, 1),
    default_args={'snowflake_conn_id': 'snowflake_conn'},
    tags=['example'],
    catchup=False,
)


snowflake_op_sql_str = SnowflakeOperator(
    task_id='snowflake_op_sql_str',
    dag=dag,
    sql=CREATE_TABLE_SQL_STRING,
)

snowflake_op_with_params = SnowflakeOperator(
    task_id='snowflake_op_with_params',
    dag=dag,
    sql=SQL_INSERT_STATEMENT,
    parameters={"id": 56},
)

snowflake_op_sql_list = SnowflakeOperator(task_id='snowflake_op_sql_list', dag=dag, sql=SQL_LIST)

snowflake_op_sql_multiple_stmts = SnowflakeOperator(
    task_id='snowflake_op_sql_multiple_stmts',
    dag=dag,
    sql=SQL_MULTIPLE_STMTS,
)

snowflake_op_template_file = SnowflakeOperator(
    task_id='snowflake_op_template_file',
    dag=dag,
    sql='/opt/airflow/dags/repo/sql/query1.sql',
)
snowflake_op_template_file
