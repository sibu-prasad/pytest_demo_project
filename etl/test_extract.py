import pytest
import allure
from utilities.logger import logger
from utilities.db_utility import DBManager

@pytest.mark.regression
def test_extract_data():
    logger.info("Starting DB configuration test.")

    db_manager = DBManager()
    engine = db_manager.get_engine()

    try:
        with engine.connect() as connection:
            logger.info("Successfully connected to database.")
            result = connection.exec_driver_sql("SELECT * FROM emp;")
            rows = result.fetchall()
            logger.info(f"Number of rows fetched: {len(rows)}")

            assert len(rows) > 0, "No data retrieved from employee table."

    except Exception as e:
        logger.error(f"Error during DB extraction: {e}")
        pytest.fail(f"DB extraction failed: {e}", pytrace=True)
    return rows