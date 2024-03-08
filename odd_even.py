from loguru import logger

list1 = [10,20,33,44,66,11,17]

def sorting(list1):
    even = []
    odd = []
    for i in list1:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    logger.info(even)
    logger.info(odd)

sorting(list1)