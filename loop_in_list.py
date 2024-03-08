#loop and range method in list

from loguru import logger

list1 = [10,20,30,40]

for i in range(len(list1)):
    logger.info(f"Value of {i} variable is {list1[i]}")