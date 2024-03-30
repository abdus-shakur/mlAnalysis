import logging


class LOGGING_TEST:

    def method1(self):
        data = {'first': 'value'}
        data1 = {'second': 'value'}
        self.logger.error(f"Error : {data1} , {data}")
        self.logger.info("info")
        self.logger.warning("Warn")
        self.logger.debug("Debug")

    def __init__(self):
        logging.basicConfig(filename="logging.log", level=logging.DEBUG,
                            filemode="w",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
        self.logger = logging.getLogger(__name__)


test = LOGGING_TEST()
test.method1()
