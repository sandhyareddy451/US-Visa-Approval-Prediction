
from US_Visa.logger import logging
from US_Visa.exception import USvisaException
import sys


logging.info("welcome to our customer log")

try:
    a=2/0
except Exception as e:
    raise USvisaException(e, sys)