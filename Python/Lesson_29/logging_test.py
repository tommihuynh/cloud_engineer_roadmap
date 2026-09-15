import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


logging.info("Server health check started")
logging.info("web-01 is running")
logging.warning("web-02 is stopped")
logging.info("Server health check finished")
