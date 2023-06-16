#!/usr/local/lib/python3.9/dist-packages
import asyncio
import nats
import pyttsx3
import time
from nats.errors import  TimeoutError
# import playsound


async def main():
    
    nc = await nats.connect("nats.enin.io")
    # engine = pyttsx3.init("espeak")
    # voices = engine.getProperty('voices')
    # rate = engine.getProperty('rate')
    # engine.setProperty('voice',voices[54].id) #English
    # engine.setProperty('rate',120)

    async def message_handler(msg):
        # playsound.playsound('/home/sakshi/Python-3.6.0/nats-py-2.2.0/supermarket-pa-104750.mp3')
        engine = pyttsx3.init("espeak")
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('voice',voices[33].id) #English
        engine.setProperty('rate', 110)
    
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        hi = (f"{data}".format(subject=subject, data=data, reply=reply))
        print(hi)
        engine.say(hi)
        engine.runAndWait()
        # time.sleep()
    # playsound.playsound('/home/sakshi/Python-3.6.0/nats-py-2.2.0/supermarket-pa-104750.mp3')
    sub = await nc.subscribe("0987-guest-registration", cb=message_handler)
    await nc.publish("0987-guest-registration", b'Good Morning')
    await nc.publish("0987-guest-registration", 'स्वागत गृहस्थी'.encode())
    # await nc.request("0987-guest-registration", 'घरगुती स्वागत'.encode())
    

    
    try:
        # playsound.playsound('/home/sakshi/Python-3.6.0/nats-py-2.2.0/supermarket-pa-104750.mp3')
        response = await nc.request("0987-guest-registration", b'Please Wait', timeout=120)
        # playsound.playsound('/home/sakshi/Python-3.6.0/nats-py-2.2.0/supermarket-pa-104750.mp3')
        #     message=response.data.decode()))
    
    except TimeoutError:
        print("Request timed out")
    

    # await sub.unsubscribe()

    # Terminate connection to NATS.
    await nc.drain()

if __name__ == '__main__':
     asyncio.run(main())