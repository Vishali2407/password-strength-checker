def pswrd_strgth(password):
    length=len(password)>=8
    uppercase=any(char.isupper()for char in password)
    lowercase=any(char.islower()for char in password)
    digit=any(char.isdigit()for char in password)
    special=any(char in "`~@$%^&*)#(_-+=}{][:;<,>.?/'" for char in password)

    if len(password)<8:
        return "weak"
    elif lowercase and uppercase and digit and special:
        return "strong"
    else:
        return "okay"

    
password=input("Enter the password: ")

strength= pswrd_strgth(password)
print("the strength of your password is:", strength)
