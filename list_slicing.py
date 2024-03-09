from loguru import logger

string1 = " Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the data warehouse and business intelligence industry’s thought leader on the dimen"
logger.info(string1)

list_slicing = string1.split(" ")
# count = list_slicing.count("the")

count = 0
for i in list_slicing:
    if i == 'the':
        count = count + 1
logger.info(count)
