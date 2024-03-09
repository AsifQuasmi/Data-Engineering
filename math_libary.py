from loguru import logger
# from math import sqrt,pow,fabs,factorial,gcd


# #value = m.sqrt(26)

# print(pow(20,2))
# logger.info(factorial(4))
# logger.info(gcd(100,200,3))


num = 20

for i in range(num):
    if i%3!=0 and i%5!=0:
        # logger.info(f"{i}", end= " ")
        print(i, end = " ")
        
