from twilio.rest import Client
import os

# Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_otp(to_phone_number, otp_code):
    try:
        message = client.messages.create(
            body=f"Your OTP code is: {otp_code}",
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        print(f"OTP sent to {to_phone_number}. Message SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send OTP: {e}")
        return False