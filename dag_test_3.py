from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator

def test_dagbag():
        dag_bag = DagBag(include_examples=False)
	print(dag_bag.dags.items())
        # assert not dag_bag.import_errors
        for dag_id, dag in dag_bag.dags.items():
            error_msg = f"{dag_id} in {dag.full_filepath} has no description"
            assert dag.description, "Invalid"
		
def cal():
	x = 1
	y = 1
	assert y, "Invalid Operation"
	print(x / y)
try:
	

    with DAG(
        dag_id="dag_test_3",
        schedule_interval="@daily",
        start_date=days_ago(2),
    ) as dag:
        run_this = PythonOperator(
            task_id="test",
            python_callable=test_dagbag,
        )

# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)

