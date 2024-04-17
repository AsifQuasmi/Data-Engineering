string = "10022001"
# string1 = string[::-1]
# if string1 == string:
#     print(f"String {string} is palindrom")
# else:
#     print(f"String {string} is not a palindrom")


low = 0
high = len(string)-1
print(high)
while low < high:
    if string[low] != string[high]:
        print(f"String  {string} is not an palindrome")
        break
    low = low+1
    high = high+1
else:
    print(f"String  {string} is palindrome")