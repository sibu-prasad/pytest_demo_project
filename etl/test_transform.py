import pytest
import allure
from utilities.logger import logger
from etl.test_extract import test_extract_data
import pandas as pd

@pytest.mark.db
def test_transform_data():
    db_manager = test_extract_data()
    logger.info("Starting DB transformation test.")
    df = pd.DataFrame(db_manager)
    logger.info(f"Dataframe created with shape: {df.head(2)}")
    df.to_csv("data/transformed_data.csv", index=False)
    logger.info("Data transformed and saved to CSV.")
