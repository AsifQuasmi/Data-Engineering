from loguru import logger

labour_name = ["Ramesh","Suresh","Prathamesh"]
IDs = [1,200,3,4,700,6,900,1000]

labour_name += IDs
logger.info(labour_name)
length = len(labour_name)
logger.info(length)

lvc = labour_name.index("Ramesh")
labour_name.insert(3,"Nushta")
logger.info(labour_name)
# logger.info(lvc)
pop_value = labour_name.pop()
if pop_value > 500:
    logger.info(f"Costly labour ")

logger.info(labour_name)
