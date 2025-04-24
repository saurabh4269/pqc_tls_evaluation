"""
Logging and reporting utilities.

Expanded: Add docstring and usage example for setup_logger.
"""
import logging

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """
    Set up a logger that writes to a file.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = setup_logger("test", "test.log")
    logger.info("Logger initialized.")
