import time, logger

log = logger.setup_applevel_logger()

try:
    log.info("Starting the file")
except Exception as e:
    log.exception("Error occured")
    log.exception(e)
