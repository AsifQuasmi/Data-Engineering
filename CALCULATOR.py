from loguru import logger

number1 = int(input("Enter the number: "))
oprator_symbol = input("Enter the operator eg: + , - ,* , / :")
#number2 = int(input("Enter the number"))
calucated_value = 0
while oprator_symbol != "=":
    number2 = int(input("Enter the number: "))
    if oprator_symbol == "+":
        calucated_value = number1+number2
        logger.info(calucated_value)
    elif oprator_symbol == "-":
        calucated_value = number1-number2
        logger.info(calucated_value)
    elif oprator_symbol == "*":
        calucated_value = number1*number2
        logger.info(calucated_value)
    elif oprator_symbol == "/":
        calucated_value = number1/number2
        logger.info(calucated_value)
    oprator_symbol = input("Enter the operator eg: + , - ,* , / :")
    number1 = calucated_value