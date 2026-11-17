## Airflow orchestration

`dags/gasprices_pythonoperator_dag.py` runs the ETL as three Airflow tasks (extract, transform, load) using PythonOperator. Data passes between tasks via XCom.

**Run it:**
1. Install the dependencies into Airflow's environment: `pandas`, `python-dotenv`, `psycopg2-binary`, `sqlalchemy`
2. Copy the DAG file into `~/airflow/dags/`
3. Update the `.env` path in `load_dotenv()` to match your machine
4. Test it:

```bash
airflow dags test project2_gas_prices_pythonoperator 2026-01-01
```

API keys and database credentials are loaded from `.env` and are never committed.
