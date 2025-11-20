"""
Build an email validator. 
Take an email address, check if it contains "@" and ".", extract the username (part before @), 
domain name, and convert everything to lowercase. 
Also count how many characters are in the email.
"""

def validate_email_address(email) :

    if email is None:
      return False
    elif len(email.strip()) == 0 :
      return False
    elif email.find('@') == -1 :
      return False
    elif email.find('.') == -1 :
      return False
    else :
      return True

def extract_username(email) :
    return email[0:email.index('@')]

def extract_domain(email) :
    return email[email.index('@')+1 : email.index('.')]

if __name__ == "__main__" :
    print("Email Validator Starts")
    email = 'A@gmail.com'

    is_valid_email = validate_email_address(email)
    print(f"Is Valid Email {is_valid_email}")

    if is_valid_email == True :
      total_number_of_characters = len(email)
      print(f"Total Number of Characters : {total_number_of_characters}")

      user_name = extract_username(email)
      print(f"User Name : {user_name.lower()}")

      domain_name = extract_domain(email)
      print(f"Domain Name : {domain_name.lower()}")
 
      print("Email Validator Ends")