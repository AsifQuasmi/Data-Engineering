from loguru import logger
from collections import deque
list1 = [10,20,30,40,50]
times = 3
logger.info(list1)
# for d in range(times):
#     first_value = list1[0]
#     for i in range(1,len(list1)):
#         list1[i-1] = list1[i]
#     list1[len(list1)-1] = first_value

# logger.info(list1)


# list2 = list1[times:]+list1[0:times]
# logger.info(list2)

dq = deque(list1)
logger.info(dq)
dq.rotate(-times)
logger.info(dq)
list1 = list(dq)
logger.info(list1)