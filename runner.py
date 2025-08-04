import subprocess
import shutil
from utilities.config_reader import ConfigReader

def run_tests():
    config = ConfigReader()
    report_dir = config.get('allure', 'report_dir')

    # Clean existing results
    shutil.rmtree(report_dir, ignore_errors=True)

    # Run pytest
    subprocess.run([
        "pytest",
        "--alluredir", report_dir,
        "-v"
    ], check=True)

    # Generate Allure report with shell=True on Windows
    subprocess.run([
        "allure", "generate", report_dir,
        "-o", "allure-report",
        "--clean"
    ], shell=True)

    print("Execution completed. Open allure-report/index.html to view results")

if __name__ == "__main__":
    run_tests()