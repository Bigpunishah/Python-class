#vikel cunningham

def main():
    full_name = get_full_name()
    print()
    password = get_password()
    first_name = get_first_name(full_name)
    print()
    email = get_email()
    print()
    phoneNum = get_phone_num()
    print()
    print("Hi " + first_name + ", thanks for creating an account. We'll text")
    print("your confimration code to this number:", phoneNum)


def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password


def get_email():
    while True:
        email = input("Enter email address : \t").strip()
        if '@' in email and email[-4:] == '.com':
            return email
        else:
            print("Please enter a valid email address.")

def get_phone_num():
    while True:
        phone = input("Enter phone number : \t")
        digit=[]
        for i in phone:
            if i.isdigit():
                digit.append(i)
        if len(digit) !=10:
                print("Please enter a 10-digit phone number.")
        else:
            return ''.join(digit[:3])+'.'+''.join(digit[3:6])+'.'+''.join(digit[6:])    

if __name__ == "__main__":
    main()
