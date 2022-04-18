from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def test_dagbag():
    dag_bag = DagBag()
    assert not dag_bag.import_errors

    #   for dag_id, dag in dag_bag.dags.items():
    #     error_msg= f"{dag_id} in {dag.full_filepath} has no tags"
    #     assert dag.tags, error_msg

    for dag_id, dag in dag_bag.dags.items():
        error_msg = f"{dag_id} in {dag.full_filepath} has no description"
        assert dag.description, error_msg


with DAG(
        dag_id="dag_test_3",
        schedule_interval="@daily",
        start_date=days_ago(2),
) as dag:
    run_this = PythonOperator(
        task_id="test",
        python_callable=test_dagbag,
    )

class TestHelloWorldDAG(unittest.TestCase):
    """Check HelloWorldDAG expectation"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        """Check task count of hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 3)

    def test_contain_tasks(self):
        """Check task contains in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['dummy_task', 'multiplyby5_task','hello_task'])

    def test_dependencies_of_dummy_task(self):
        """Check the task dependencies of dummy_task in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        dummy_task = dag.get_task('dummy_task')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, [])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['hello_task', 'multiplyby5_task'])

    def test_dependencies_of_hello_task(self):
        """Check the task dependencies of hello_task in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        hello_task = dag.get_task('hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['dummy_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorldDAG)
unittest.TextTestRunner(verbosity=2).run(suite)