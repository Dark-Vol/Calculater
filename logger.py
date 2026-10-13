from loguru import logger
from pathlib import Path

# Создаём папку log, если её нет
Path("log").mkdir(exist_ok=True)

logger.add(
    "log/calculator.log",
    rotation="1 MB",
    level="DEBUG"
)



# Logs an informational message when the application starts
logger.info("Application started")

# Logs a success message when data has been loaded successfully
logger.success("Data loaded successfully")

# Logs a warning when memory usage is high
logger.warning("Memory usage is high")

# Logs an error message when an error occurs
logger.error("An error occurred")

# Logs a debug message, usually used for troubleshooting and development
logger.debug("That's it, beautiful and simple logging!")
