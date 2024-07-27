import logging

def test_logging_concept():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formater = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)")
    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler) #filehandler object
    logger.setLevel(logging.INFO)
    logger.debug("A debug statemeeent")
    logger.info("infomation statement")
    logger.warning("something id in warning mode")
    logger.error("a major error has happend")
    logger.critical("ritical issue")