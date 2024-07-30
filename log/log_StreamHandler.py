import logging

logger = logging.getLogger("log_StreamHandler")
handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.warning('This is a warning message')