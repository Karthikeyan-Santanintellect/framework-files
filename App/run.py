from pdb import run
import time
import logging
import subprocess
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# logger.info('loading frameworks')
# subprocess.run('py frameworks.py')
# time.sleep(2)

# logger.info('loading standards')
# subprocess.run('py standards.py')
# time.sleep(2)

# logger.info('loading regulations')
# subprocess.run('py regulations.py')
# time.sleep(2)

# logger.info('loading NIST AI RMF')
# subprocess.run('py nist_ai-rmf.py')
# time.sleep(2)

# logger.info('loading NIST CSF 2.0')
# subprocess.run('py nist_csf.py')
# time.sleep(2)

# logger.info('loading NIST PMF')
# subprocess.run('py nist_pmf_1.py')
# time.sleep(2)

# logger.info('loading NIST PMF 1.1')
# subprocess.run('py nist_pmf_1_1.py')
# time.sleep(2)

# logger.info('loading NIST RMF')
# subprocess.run('py nist_rmf.py')
# time.sleep(2)

# logger.info('loading ISO 27001')
# subprocess.run('py iso27001.py')
# time.sleep(2)

# logger.info('loading ISO 27002')
# subprocess.run('py iso27002.py')
# time.sleep(2)

# logger.info('loading HIPAA')
# subprocess.run('py hipaa.py')
# time.sleep(2)

# logger.info('loading HITRUST')
# subprocess.run('py hitrust.py')

BASE_DIR = Path(__file__).resolve().parent


def run_script(script_path, group=None, sleep=2):
    try:
        if group:
            logger.info(f'loading {group}')

        full_path = BASE_DIR / script_path

        if not full_path.exists():
            raise FileNotFoundError(f'Script not found: {full_path}')

        logger.info(f'loading {full_path}')

        subprocess.run(
            [sys.executable, str(full_path)],
            check=True
        )

        logger.info(f'successfully loaded {script_path}')

    except subprocess.CalledProcessError:
        logger.error(f'Script failed: {script_path}', exc_info=True)

    except Exception:
        logger.error(f'Unexpected error running {script_path}', exc_info=True)

    finally:
        time.sleep(sleep)


# IS Frameworks
run_script('cis_controls.py', 'IS_Frameworks_Standard')
run_script('iso27001.py')
run_script('iso27002.py')
run_script('nist_ai_rmf.py')
run_script('nist_csf.py')
run_script('nist_pmf_1_1.py')
run_script('nist_pmf_1.py')
run_script('nist_rmf.py')

# Industry Standards
run_script('glba.py', 'Industry_Standard_Regulation')
run_script('hipaa.py')
run_script('hitech.py')
run_script('hitrust.py')
run_script('nerc_cip.py')
run_script('pcidss.py')
run_script('tisax.py')

# Regional Regulations
run_script('cpra.py', 'Regional_standard_regulation')
run_script('dpdpa.py')
run_script('gdpr.py')
run_script('shield.py')
run_script('tdpsa.py')
run_script('dora.py')
run_script('vcdpa.py')
run_script('nis_2.py')






logger.info('Loaded all frameworks')
