from loguru import logger

string1 = " Ralph Kimball founded the Kimball Group. Since the mid-1980s, the THE been The data warehouse and business intelligence industry’s thought leader on the dimen"
logger.info(string1)

list_slicing = string1.split(" ")
list_slicing_lower = string1.lower().split(" ")
logger.info(list_slicing_lower)
# count = list_slicing.count("the")

count = 0
for i in list_slicing_lower:
    if i == 'the':
        count = count + 1
logger.info(f"Total count of the is = {count} ")
