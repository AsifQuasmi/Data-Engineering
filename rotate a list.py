from loguru import logger

list1 = [10,20,30,40]

# list2 = list1[1:]+list1[0:1]
# logger.info(list1)
# list1.append(list1.pop(0))

# #logger.info(list1)
# logger.info(list1)

# logger.info(list1)
# first_value = list1[0]
# for i in range(len(list1)-1):
#     logger.info(i)   
#     list1[i]=list1[i+1]
# list1.insert(len(list1)-1, first_value)
# list1.pop()

logger.info(list1)
first_value = list1[0]
for i in range(1,len(list1)):
    # logger.info(i)
    list1[i-1]=list1[i]
    
list1[len(list1)-1] = first_value
logger.info(list1)