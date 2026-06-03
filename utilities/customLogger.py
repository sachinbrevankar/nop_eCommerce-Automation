import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename=".\\Logs\\automation.log",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S',
            force = True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger