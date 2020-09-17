
import airflow, sys
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      # this in combination with catchup=False ensures the DAG being triggered from the current date onwards along the set interval
    'provide_context': True,                            # this is set to True as we want to pass variables on from one task to another
}

def load_preprocess():
    print(sys.path)

dag = DAG(
    dag_id='initial_model_DAjG',
    default_args=args,
    schedule_interval= '@once',             # set interval
	catchup=False,                          # indicate whether or not Airflow should do any runs for intervals between the start_date and the current date that haven't been run thus far
)


task1 = PythonOperator(
    task_id='load_preprocess',
    python_callable=load_preprocess,        # function to be executed
    op_kwargs={},
    dag=dag,
)

