from loguru import logger
length = int(input("Enter the length of land: "))
 
if length < 100 :
    # length = int(input("Enter the length of land greater than 100 ft: "))
    logger.info(f"Enter the length greater than 100 ft ")
    if length >80:
        logger.info(f"Land is too short for 4 BHK but you can build 3 BHK house :( ")
    else:
        logger.info("Land is not having much space to build 4 BHK house :( ")
elif length >=500:
    logger.info(f"You can make more than one building with this area :) ")
else:
    # logger.info()
    breath = int(input("Enter another value for the breath: "))