"""
Create a password strength checker. 
Compare a given password with criteria: length > 8 characters, contains "123", 
check if it's the same as "password123", 
and compare two passwords to see if they're identical.
"""

def validate_password_stength(password) :
    if len(password) < 8 :
       print(f"Password not met lenghth criteria its length is {len(password)}")
       return False
       return False
    elif "password123" == password :
       print("Password is weak use different combination")
    elif password.find("123") != -1 :
       print("Password contain 123 sequence")
       return False
    else :
       return True

def is_password_identical(old_password, new_password) :
    return old_password == new_password

if __name__ == "__main__" :
    print("Password Checker Starts")
    new_password = input("Enter Your Password :")
    print(f"User's password is : {new_password}")
    
    is_strong_password = validate_password_stength(new_password)
    print(f"Is Strong Password : {is_strong_password}")

    if is_strong_password :
      print("This password is Strong")
      old_password = input("Enter your Old Password :")

      is_identical = is_password_identical(old_password,new_password)
      if is_identical : 
            print("Two password are Same")
      else :
            print("Two password is Different")
    print("Password Checker Ends")