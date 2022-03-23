import unittest
from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator



with DAG(
    dag_id="dag_test2",
    schedule_interval="@daily",
    start_date=days_ago(2),
    catchup=False,
    tags=["example"],
) as dag:
    class TestDagIntegrity(unittest.TestCase):
        LOAD_SECOND_THRESHOLD = 2

        def setUp(self):
            self.dagbag = DagBag()

        def test_import_dags(self):
            self.assertFalse(
                len(self.dagbag.import_errors),
                'DAG import failures. Errors: {}'.format(
                    self.dagbag.import_errors
                )
             )

        def test_alert_email_present(self):

            for dag_id, dag in self.dagbag.dags.iteritems():
                emails = dag.default_args.get('email', [])
                msg = 'Alert email not set for DAG {id}'.format(id=dag_id)
                self.assertIn('alert.email@gmail.com', emails, msg)


    suite = unittest.TestLoader().loadTestsFromTestCase(TestDagIntegrity)


    run_this = PythonOperator(
        task_id="test",
        python_callable=unittest.TextTestRunner(verbosity=2).run(suite),
    )