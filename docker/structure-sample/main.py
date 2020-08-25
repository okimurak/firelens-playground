import logging
import sys
import datetime
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(
            log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


logger = logging.getLogger()

logHandler = logging.StreamHandler(sys.stdout)
logHandler.setLevel(logging.DEBUG)
formatter = CustomJsonFormatter()
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)

logger.info("Hello Python World !")
