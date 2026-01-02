class Error(Exception):
    def __init__(self,error_code,error_msg):
        self.error_code = error_code
        self.error_msg = error_msg
    
    def __str__(self):  
        return f"{self.error_code}: {self.error_msg}"