# conftest.py
from pytest_dependency import DependencyManager
import logging, os
DependencyManager.ScopeCls['module'] = DependencyManager.ScopeCls['session']
option = None

def pytest_addoption(parser):
    """Add the skippytestconfigure"""
    parser.addoption( '-U', '--skippytestconfigure', action = "store", default = False, help = "Skip pytest_configure ?")

def pytest_configure(config):
    skippytestconfigure = config.option

    # set the log format
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s \n---"

    # configure the logger
    logging.basicConfig(filename = os.getcwd() + "/reports/pytest.log", filemode = 'w',
                        level = logging.NOTSET,
                        format = LOG_FORMAT)
    logger = logging.getLogger()

