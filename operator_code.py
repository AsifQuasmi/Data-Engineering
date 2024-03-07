from loguru import logger
# import math
# length_of_land = 100
# breath_of_land = 100
# bricks_per_unit = 10.5
# labour1 = "Jagmohan"
# labour2 = "Rampyare"
# Is_home = True


# area = length_of_land*breath_of_land
# perimeter = 2*(length_of_land+breath_of_land)

# div = 15/4
# ceil_value = math.ceil(15/4)
# floor_value = math.floor(15/4)
# #print(area)
# logger.info(f"Area of land = {area} sqft")
# logger.info(f"perimeter of land = {perimeter} ft")
# logger.info(f"div of numbers = {div}")
# logger.info(f"celing and floor value = {ceil_value} {floor_value} repectevly")


# logger.info(f"Addition of two numbers = {length_of_land}+{breath_of_land}")

length = int(input("Enter length of the area : "))
breath = int(input("Enter breath of the land : "))

area = length * breath

logger.info(area)

