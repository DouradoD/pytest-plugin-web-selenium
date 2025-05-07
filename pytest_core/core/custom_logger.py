import logging

# setting logger level and format
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
# create logger with 'spam_application'
logger = logging.getLogger()

LINE_SEPARATION_LENGTH = 80
LINE_SEPARATION = '=' * LINE_SEPARATION_LENGTH