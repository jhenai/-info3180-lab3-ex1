import smtplib
from_addr ='xxxxxx@gmail.com'
to_addr = 'xxxxx@gmail.com'
from_name='jhenai'
to_name='bob'
msg="hey gurl hey"
subject= "does this thing really work?"
message = """From: {} <{}>
            To: {} <{}> Subject: {}
            {}
            """

            
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
# Credentials (if needed)
username = 'jxxxxxxx@gmail.com'
password = 'xxxxxx'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 