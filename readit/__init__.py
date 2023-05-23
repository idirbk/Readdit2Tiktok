import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s [%(levelname)s] %(message)s",  # Set the log message format
    datefmt="%Y-%m-%d %H:%M:%S"  # Set the date and time format
)


stream_handler = logging.StreamHandler()  # Create a stream handler

# Create a file handler
file_handler = logging.FileHandler("tiktok.log")  # Specify the path to the log file

# Configure the file handler
file_handler.setLevel(logging.INFO)  # Set the logging level for the file handler

# Create a formatter and add it to the file handler
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

# Attach the file handler to the logger
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

