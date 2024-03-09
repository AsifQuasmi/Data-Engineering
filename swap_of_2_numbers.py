from loguru import logger

number1 = 10
number2 = 20
logger.info(f"{number1},{number2}")
number1 = number1 ^ number2
number2 = number1 ^ number2
number1 = number1 ^ number2

# number1,number2 = number2,number1

logger.info(f"{number1},{number2}")