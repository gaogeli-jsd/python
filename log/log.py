import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('my_log.log', 'a')

#stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('Debugging information')
logger.info('Informational message')
logger.warning('Warning:config file %s not found', 'server.conf')
logger.error('Error occurred')
logger.critical('Critical error -- shutting down')