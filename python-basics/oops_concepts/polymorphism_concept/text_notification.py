from notification import Notification

class TextNotification(Notification):
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
        
    def send(self,msg):
        print(f"Send Text Message to {self.mobile_number} with msg {msg}")