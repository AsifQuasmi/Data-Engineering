from loguru import logger

list1 = [10,20,20,30,30,10,11]
# count1 = 0
# for i in list1:
#     if list1.count(i)%2==0:
#         count1=count1+1
#         #print(i)
#     elif list1.count(i)%2!=0:
#         logger.info(f"{i} is odd in list")
#         break
# print(count1)
# if count1 == len(list1):
#     logger.info(f"No odd element found")

def check_odd(list1):
    result = 0
    for i in list1:
        result = result ^ i
    return result

result = check_odd(list1)
if result == 0:
    logger.info("list has no odd occurence of any value ")
else:
    logger.info(f"list has odd occurance of {result} value ")