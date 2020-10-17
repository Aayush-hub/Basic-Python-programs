#Simplest way to send emails using python
#Pip install yagmail

import yagmail
#For sending emails, one of your own email id and pass are required
email_id=#Enter Your email address
password=#Enter Your password
emailsend=input("Enter the email id You wanna send email to")
subject=inpurt("Enter the subject of the email")
contents=inpurt("Enter the message you wanna pass")
   
try:
    yag=yagmail.SMTP(email_id,password)
    yag.send(emailsend,subject,contents)
    print("Email has been sent!")

else:
    print("There's been an error")
    
