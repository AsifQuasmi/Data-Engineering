from loguru import logger

index = 0

list1 = [10,20,30,40,60]
value = 50

# list1.append(None)
# length = len(list1)


# for i in list1:
#     if value < i:
#         index = index +1
# logger.info(type(list1))
# logger.info(type(i))
# logger.info(index)
# logger.info(length)


list1.append(value)
list1.sort()
logger.info(list1)

for i in list1:
    print(i, end =" ")