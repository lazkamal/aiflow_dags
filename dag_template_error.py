# use for Documentation
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.email import send_email_smtp
import os
import airflow
import logging
import subprocess

START_DATE = airflow.utils.dates.days_ago(1)

# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'email': ['kamal.lazhar@external.stellantis.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
# [END default_args]

# ---------------------------------------------------------------
#               STEP 3 :  define a DAG and set params
dag = DAG('Dag_test_error',
          default_args=default_args,
          description='Test DAG for data project',
          schedule_interval='@monthly',
          start_date=START_DATE,
          catchup=False,
          )

cmd_t_1='echo "Welcome to Airflow " '
cmd_t_2='exit 1'
cmd_t_end=' echo "Tache terminee avec succes"'

# ---------------------------------------------------------------
#               STEP 4 - define and set DAG's tasksas dag:
with dag:

    t_1 = BashOperator(
        task_id='test_welcome',
	bash_command='echo "Welcome to Airflow " '
        )

    t_2 = BashOperator(
        task_id='test_run_error',
	bash_command='exit 1'
        )

    t_end = BashOperator(
        task_id='task_finished',
	bash_command=' echo "Tache terminee avec succes"'
        )

    t_1 >> t_2 >> t_end