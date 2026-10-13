from loguru import logger
from pathlib import Path

# Создаём папку log, если её нет
Path("log").mkdir(exist_ok=True)

logger.add(
    "log/calculator.log",
    rotation="1 MB",
    level="DEBUG"
)


logger.info("Application started")
logger.success("Data loaded successfully")
logger.warning("Memory usege in heigh")
logger.error("Application started")
logger.debug("That's it, beautiful and simple logging!")