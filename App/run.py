import time
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info('loading frameworks')
subprocess.run('py frameworks.py')
time.sleep(2)

logger.info('loading standards')
subprocess.run('py standards.py')
time.sleep(2)

logger.info('loading regulations')
subprocess.run('py regulations.py')
time.sleep(2)

logger.info('loading NIST AI RMF')
subprocess.run('py nist_ai-rmf.py')
time.sleep(2)

logger.info('loading NIST CSF 2.0')
subprocess.run('py nist_csf.py')
time.sleep(2)

logger.info('loading NIST PMF')
subprocess.run('py nist_pmf_1.py')
time.sleep(2)

logger.info('loading NIST PMF 1.1')
subprocess.run('py nist_pmf_1_1.py')
time.sleep(2)

logger.info('loading NIST RMF')
subprocess.run('py nist_rmf.py')
time.sleep(2)

logger.info('loading ISO 27001')
subprocess.run('py iso27001.py')
time.sleep(2)

logger.info('loading ISO 27002')
subprocess.run('py iso27002.py')
time.sleep(2)

logger.info('loading HIPAA')
subprocess.run('py hipaa.py')
time.sleep(2)

logger.info('loading HITRUST')
subprocess.run('py hitrust.py')

logger.info('Loaded all frameworks')
