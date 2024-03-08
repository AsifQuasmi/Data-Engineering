from loguru import logger

list1 = [10,20,30,40,50,50,10,100,100,200,5,199]

# def second_largest(list1):
#     if len(list1) <= 1:
#         return None
#     else:
#         maximum_value = list1[0]
#         second_value = None
#         for i in list1[1:]:
#             if i > maximum_value:
#                 second_value = maximum_value
#                 maximum_value = i
#             elif i != maximum_value:
#                 if second_value == None or second_value < i:
#                     second_value = i
#     return second_value

# second_val = second_largest[list1]
# logger.info(second_val)

#def second_largest(list1):

updated_list = list(set(list1))
updated_list.sort()
logger.info(updated_list)
length = len(updated_list)
logger.info(length)
second_value = updated_list[length-2]
logger.info(second_value)
#logger.info(updated_list[len(updated_list)]-2)
    # if len(updated_list) <= 1:
    #     return None
    # else:
    #     return updated_list[len(updated_list) -1]

#second_val = second_largest[list1]
#logger.info(second_val)