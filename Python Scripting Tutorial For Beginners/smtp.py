import smtplib

# Create a SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
s.starttls()

# Authentication
s.login("sender_email_id", "sender_email_id_password")

# Message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# terminating the session
s.quit()