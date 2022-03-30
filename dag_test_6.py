from airflow.operators.email_operator import EmailOperator
from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG


def test_dagbag():
    default_args = {
        "owner": "airflow",
        "start_date": datetime(2022, 2, 16),
        'email': ['lazkamal34@gmail.com'],
        'email_on_failure': True,
    }
with DAG(
        dag_id="Sending_mail",
        schedule_interval="@once",
        default_args=default_args,
) as dag:
    sending_email = EmailOperator(
        task_id='sending_email',
        to='lazkamal34@gmail.com',
        subject='Airflow Alert !!!',
        html_content="""<h1>Testing Email using Airflow</h1>""",
    )






