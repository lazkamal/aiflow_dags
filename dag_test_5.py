from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator

try:
    def test_dagbag():
        dag_bag = DagBag(include_examples=False)
        assert not dag_bag.import_errors
        for dag_id, dag in dag_bag.dags.iteritems():
            emails = dag.default_args.get('email', [])
            msg = 'Alert email not set for DAG {id}'.format(id=dag_id)
            assertIn('lazkamal34@gmail.com', emails, msg)


    with DAG(
        dag_id="dag_test_5",
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



