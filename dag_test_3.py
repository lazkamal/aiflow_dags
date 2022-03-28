from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['lazkamal34@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}
def cal():
	x = 1
	y = 0
	assert y , "Invalid Operation"
	print(x / y)
try:
    def test_dagbag():
        dag_bag = DagBag(include_examples=False)
        assert not dag_bag.import_errors
        # dag = dag_bag.dags['tutorial']
        # error_msg = f"databricks_dag in {dag.full_filepath} has no description"
        for dag_id, dag in dag_bag.dags.items():
            error_msg = f"{dag_id} in {dag.full_filepath} has no description"
            assert dag.description, error_msg
            print("Valid Dag")

    with DAG(
        dag_id="dag_test_3",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(2),
    ) as da
        run_this = PythonOperator(
            task_id="test",
            python_callable=cal,
        )

# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)



