import random
import smtplib
from email.message import EmailMessage


#my email info has been removed, use your own if you want to test (line 37)


def confirmation_code():
    return str(random.randint(10000, 99999))

code = confirmation_code()

#print(code)

def send_verification_code(to_email, code):   
    
    msg = EmailMessage()
    msg['Subject'] = "AminoBank verification code"
    msg['From'] = ''
    msg['To'] = to_email
    
    msg.set_content(f"Your verification code is: {code}")
    msg.add_alternative(f"""
   <html>
     <body>
       <p>Your verification code is: <b>{code}</b></p>
     </body>
   </html>
   """, subtype='html')
    

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        #server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login('your_email_here', 'your_gmail_key')
        server.send_message(msg)
       
    print(f"Verification code sent to {to_email}")

