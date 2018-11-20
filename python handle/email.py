import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("rockeythegreat.1@gmail.com", "Gmail@2018") 
message = "Message_you_need_to_send"
s.sendmail("rockeythegreat.1@gmail.com", "gupta.rajiv0703@gmail.com", message) 
s.quit() 