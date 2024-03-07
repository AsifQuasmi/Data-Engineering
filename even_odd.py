from loguru import logger

number = int(input("Enter the value :"))

if number%2 == 0:
    logger.info(f"{number} is an even number")
else:
    logger.info(f"{number} is an odd number ")