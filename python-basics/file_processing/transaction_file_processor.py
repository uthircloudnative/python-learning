from pathlib import Path
from error import Error
from datetime import datetime
import shutil


class TransactionFileProcessor:
  
  def __init__(self):
    pass

  def is_valid_date(self, date_str:str):
    try:
      datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
      return False
    else:
      return True

  def validate_header(self,header_str: str):
    #print(type(header_str))
    #print(header_str)

    headers = header_str.split(',')
    #print(headers[2])

    if headers[0] != 'account_number':
      return Error('1000',"account_number header is missing")

    if headers[1] != 'amount':
      return Error('1000',"amount header is missing")

    if headers[2] != 'date':
      return Error('1000',"date header is missing")

    return True 
    

  def validate_content_str(self,content_str: str):
    #print(type(content_str))
    #print(content_str)

    content_values = content_str.split(',')
    account_number = content_values[0]
    amount = content_values[1]
    date = content_values[2]

    if not (account_number.isnumeric() and len(str(account_number)) == 5):
      return Error('2000',"account_number has invalid value")

    if not amount.isnumeric():
      return Error('2000',"amount has invalid value")

    if not self.is_valid_date(date):
      return Error('2000',"date has invalid value")

    return True

  def write_file(self, file_path, content):
    try:
      file_path.parent.mkdir(parents=True, exist_ok=True)
      with file_path.open(mode="a", encoding="utf-8") as file:
        file.write(content)
    except Exception as e:
      print(e)


  def process_file(self,file_path):
    
    valid_file_path = file_path.with_name("valid_"+file_path.name)
    invalid_file_path = file_path.with_name("invalid_"+file_path.name)
    format_error_file_path = file_path.with_name("format_error_"+file_path.name)

    try:
    # This will read all the file content at once and bring into memory.
    # If we want to lazy load the content use open method on path
  
    #content = file_path.read_text(encoding="utf-8")

     with file_path.open(encoding="utf-8") as file_content:
       line_number = 1
       for content in file_content:
         print(content)
         original_content = content.strip()
         if line_number == 1:
           result = self.validate_header(original_content)
           if isinstance(result, Error):
             shutil.copy(file_path, format_error_file_path)
             raise result
           else:
             self.write_file(valid_file_path, original_content+"\n")
         else:
           result = self.validate_content_str(original_content)
           if isinstance(result, Error):
             self.write_file(invalid_file_path, original_content+"|"+result.error_code+"|"+result.error_msg+"\n")
             #raise result
           else:
             self.write_file(valid_file_path, original_content+"\n")
         line_number +=1
   
    except FileNotFoundError:
      print("File Not Found in given path")
    except Error as business_error:
      print(business_error)
    except Exception as e:
      print(e)

if __name__ == "__main__":
    file_path = Path("/Users/abc/Documents/file_disk")/"transactions.txt"
    file_processor = TransactionFileProcessor()
    file_processor.process_file(file_path) 
  