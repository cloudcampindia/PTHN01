# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     res = a / b
#     print(res)
# except:
#     print("Entered numbers should be integers and greater than zero")


# builtins = locals()['__builtins__'].__dict__

# for x in builtins:
#     print(builtins[x])

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     res = a / b
#     print(res)
# except ValueError as e:
#     print(e)
#     print("Please only enter numbers")
#     # try:
#     #     print(10 / "5")
#     # except:
#     #     print("Exception inside exception")
# except ZeroDivisionError as z:
#     print(z)
# except:
#    print("Something else occurred")
# else:
#     print("Else block")
# finally:
#     print("Finally block")


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     res = a / b
#     print(res)
# except (ValueError, ZeroDivisionError) as e:
#     print(e)
#     print("Please only enter numbers")
# except:
#    print("Something else occurred")
