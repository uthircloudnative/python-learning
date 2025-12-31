from notification import Notification
from email_notification import EmailNotification
from text_notification import TextNotification
from push_notification import PushNotification

def send_message(msg_channel, msg):
    msg_channel.send(msg)
        
if __name__ == "__main__":
    
    email = EmailNotification("test123@gmail.com")
    mobile = TextNotification('123-456-7890')
    device = PushNotification("ipad")
    
    msg = "Your transaction of $30 is posted"
    
    send_message(email,msg)
    send_message(mobile,msg)
    send_message(device,msg)
    