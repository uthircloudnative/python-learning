"""
Build a login validation system. 
Check if a user can access the system: 
 they must be 18 or older, 
 have a valid email (contains @ and .), 
 not be banned (banned_status = False), 
 and have either admin privileges OR regular user status
"""

def validate_user_age(age) :
    if age < 18 :
      print("User is not allowed")
      return False
    else :
      return True

def validate_user_email(email) :
    if email.find('@') == -1 or email.find('.') == -1 :
      print("User Email Id is not valid")
      return False
    else :
      return True

if __name__ == "__main__" :
    print("Login Validator Starts")
    age = int(input("Enter User Age :"))
    email = input("Enter User Email :")
    user_status = input("Enter User status :")
    user_role = input("Enter User Role :")

    if user_status != "Banned" and (user_role == "Admin" or user_role == "User") :
        is_valid_age = validate_user_age(age)
        if is_valid_age :
          is_valid_email = validate_user_email(email)
          if is_valid_email :
            print("User {} is allowed to login")
    else :
        print("User is Not allowed to login as User is either Banned or has Invalid Role")
       

    print("Login Validator Ends")