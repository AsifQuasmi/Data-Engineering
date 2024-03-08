#check if list is sorted or not

from loguru import logger

list1 = [10,20,30,40,50]
list2 = sorted(list1)
count1 = 0
if (list2 == list1):
    count1= count1+1
    logger.info("List is sorted")
print(count1)
print("List is sorted..............")
# count=0
# def check_sorted(list1):
#     if len(list1) <= 1:
#         return True
#     else:
#         for i in list1:
#             if i <= i+1:
#                 count++
#             else:
#                 break;
#     return count


# val = check_sorted(list1)
# if val == len(list1):
#     logger.info("List is sorted")
# logger.info(val)