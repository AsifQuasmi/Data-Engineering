from loguru import logger

# list1 = [10,5,20,8,30,300,44]
list1 = []
# logger.info(max(list1))

# def get_largest(list1):
#     max_value = list1[0]
#     for i in list1:
#         if max_value < i:s
#             max_value = i
        
#     return max_value

# largest_value = get_largest(list1)
# logger.info(largest_value)

def get_largest(list1):
    if len(list1) == 0:
        return None
    else:
        max_value = list1[0]
        for i in list1:
            if max_value < i:
                max_value = i
        
        return max_value
    
largest_value = get_largest(list1)
logger.info(largest_value)