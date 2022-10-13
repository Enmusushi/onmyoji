import logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s :%(name)s %(funcName)s : %(message)s'
                    )

logging.info("test info")
logging.error("test error")
# logging.
