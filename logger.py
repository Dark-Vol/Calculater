from loguru import logger

logger.add(
    "calculator.log",
    rotation="1 MB",
    level="DEBUG"
)


logger.info("Application started")
logger.success("Data loaded successfully")
logger.warning("Memory usege in heigh")
logger.error("Application started")
logger.debug("That's it, beautiful and simple logging!")