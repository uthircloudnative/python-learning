from notification import Notification

class EmailNotification(Notification):
    
    def __init__(self, email_id):
        self.email_id = email_id
        
    def send(self,msg):
        print(f"Sending Email To : {self.email_id} with message {msg}")