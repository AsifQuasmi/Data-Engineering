from loguru import logger

list1 = [10,20,30,40]

# def avareage(list1):
#     sum = 0
#     for i in list1:
#         sum = sum + i
    
#     length = len(list1)
#     return sum/length

# mean_value = avareage(list1)
# logger.info(mean_value)


def avareage(list1):
    return sum(list1)/len(list1)

mean_value = avareage(list1)
logger.info(mean_value)