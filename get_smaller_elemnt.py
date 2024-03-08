from loguru import logger

list1 = [8, 100, 20,40,3,7]
x = 10

def getsmaller(list1,x):
    smaller = []
    for i in list1:
        if i < x:
            smaller.append(i)
    return smaller

smaller = getsmaller(list1,x) 
logger.info(smaller)