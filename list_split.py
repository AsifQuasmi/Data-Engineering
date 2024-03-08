from loguru import logger

Str1 = 'from loguru import logger'
list1 = Str1.split(" ")
logger.info(list1)

list1[0] = 12
logger.info(list1)