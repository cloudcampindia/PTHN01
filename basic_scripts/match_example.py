user_in = int(input("Enter a number: "))
print(type(user_in), user_in)
match user_in:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    # case 3:
    #     print("3+")
    case _: # '_' -> temporary variable, default
        print("Something else is entered")

print("completed")