import subprocess
import shutil
import sys
from utilities.logger import logger
from utilities.config_reader import ConfigReader

def run_tests():
    config = ConfigReader()
    report_dir = config.get('allure', 'report_dir')

    shutil.rmtree(report_dir, ignore_errors=True)

    logger.info('Running tests...')
    result = subprocess.run([
        sys.executable, '-m', 'pytest', f'--alluredir={report_dir}', '-v'
    ])

    if result.returncode > 1:
        logger.error(f'Pytest exited unexpectedly with code {result.returncode}')
        sys.exit(result.returncode)

    logger.info('Generating Allure report')
    
    allure_path = r"C:\allure\\bin\\allure.bat"
    
    try:
        subprocess.run(
            f'"{allure_path}" generate {report_dir} -o allure-report --clean',
            shell=True, check=True
        )
        logger.info('Allure report generated')
    except Exception as e:
        logger.error(f'Error generating allure report: {e}')
        sys.exit(1)

    print('Execution complete. Open allure-report/index.html to view it.')

if __name__ == '__main__':
    run_tests()
