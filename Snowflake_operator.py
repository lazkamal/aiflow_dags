import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(
dag_id="snowflake_operator", default_args=args, schedule_interval=None
)
snowflake_query = [
"""DROP TABLE DATA_SCH.Employee;""",
"""create table Employee (id number, first_name string, last_name string, company string, email string, cellphone string, streetaddress string, city string, postalcode number);""",
"""insert into Employee values(1, 'Kamal', 'Lazhar', 'Stellantis', 'kamal123', '12345', 'Clemenceau', 'Montbeliard', 25200 ),(2, 'Ayyoub', 'Sghiouri', 'Stellantis', 'ayyoub123', '5678', 'Clemenceau', 'Montbeliard', 25200 );""",
]
def get_row_count(**context):
  dwh_hook = SnowflakeHook(snowflake_conn_id="snowflake_conn")
  result = dwh_hook.get_first("select count(*) from Employee")
  logging.info("Number of rows in `Employee` - %s", result[0])
with dag:
  create_insert = SnowflakeOperator(
  task_id="snowfalke_create",
  sql=snowflake_query ,
   snowflake_conn_id="snowflake_conn",
  )
  get_count = PythonOperator(task_id="get_count", python_callable=get_row_count)
create_insert >> get_count
