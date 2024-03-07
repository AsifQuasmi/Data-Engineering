from loguru import logger

labour_name = ["Ramesh","Suresh","Prathamesh"]
IDs = [1,2,3,4,7,6,9,10]
IDs.sort(reverse=True)
logger.info(IDs)
logger.info(labour_name[::-1])

labour_name.append("Mahesh")
labour_name.append("Suresh")
logger.info(labour_name)

labour_name2 = ["Sad","Uti"]
labour_name.extend(labour_name2)
logger.info(labour_name)
labour_name.insert(1,"Alliswell")
logger.info(labour_name)


labour_name_with_cost = [["Mahesh", 500],["Ramesh",400], ["Suresh", 400],["Prathamesh",300]]
logger.info(labour_name_with_cost[0][1])
logger.info(f"{labour_name_with_cost[3][0]} is costing us {labour_name_with_cost[3][1]}")