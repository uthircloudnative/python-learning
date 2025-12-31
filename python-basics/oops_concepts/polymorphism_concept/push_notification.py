from notification import Notification

class PushNotification(Notification):
    def __init__(self,device_id):
        self.device_id = device_id
        
    def send(self,msg):
        print(f"Pushing Message to {self.device_id} with msg {msg}")