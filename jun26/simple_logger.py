import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application Started")
logging.info("User Logged In")
logging.warning("Low Disk Space")
logging.error("Sample Error Message")
logging.info("Application Closed")