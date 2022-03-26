from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['kamal.lazhar@external.stellantis.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}
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
        email = "kamal.lazhar@external.stellantis.com",
        email_on_failure = True,
        start_date=days_ago(2),
    ) as dag:
        run_this = PythonOperator(
            task_id="test",
            python_callable=test_dagbag,
        )

# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)



