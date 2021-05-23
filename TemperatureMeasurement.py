account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"               # Your Twillo Account sid
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"                      # Your Twillo Account Token
ph_no = "+XXXXXXXXXX"                                            # From Which you Want to send the message
device_to_contact = "+XXXXXXXXXXX"                               # To which you want to send the message

api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"                          # API key of the bolt device
device_id = "BOLTXXXXX"                                          # Your Unique Bolt Device ID        

chat_id = "@xxxxxx"                                              # Telegram Channel Unique ID where you want to send the message
telegram_id_api = "botxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # Telegram bot API key


import json
import time

import boltiot

import Information

minimum_limit = 15
maximum_limit = 20

bolt_connect = boltiot.Bolt(Information.api_key,Information.device_id)

response = bolt_connect.analogRead('A0')
result = json.loads(response)

sms = boltiot.Sms(Information.account_sid, Information.auth_token, Information.device_to_contact, Information.ph_no)


while True:

    response = bolt_connect.analogRead('A0')
    result = json.loads(response)
    temperature = int(result['value']) / 10.24
    print("Current Temperature reading : " + str(temperature) + ' C')
    try:
        if temperature > maximum_limit or temperature < minimum_limit :
            sms.send_sms("Temperature is not suitable please evacuate" + str(temperature) + ' C')
    except Exception as e:
        print("Error has occur :")
        print(e)

    time.sleep(20)
