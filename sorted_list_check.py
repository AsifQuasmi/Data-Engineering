from loguru import logger

list1 = [11,22,44,88]

# length = len(list1)
# count = 1
# if length <=1:
#     logger.info(f"list {list1} is sorted ")
# else:
#     for i in range(length-1):
#         if list1[i] > list1[i+1]:
#             logger.info(f"list {list1} is not sorted ")
#             break
#         else:
#             count+=1
    
#     if count == length:
#         logger.info(f"list {list1} is sorted ")


def is_sorted(list1):
    list2 = sorted(list1)
    if list2 == list1:
        logger.info(f"list {list1} is a sorted list ")
    else:
        logger.info(f"list {list1} is not a sorted list ")


is_sorted(list1)