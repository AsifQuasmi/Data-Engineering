from loguru import logger

list1 = [10,20,40,50]
# list2 = []
# for i in range(len(list1),0,-1):
#     # print(i)
#     list2.append(list1[i-1])

# logger.info(list1)
# logger.info(list2)

list2 = list(reversed(list1))
list3 = list1[::-1]
logger.info(list1)
logger.info(list2)
logger.info(list3)