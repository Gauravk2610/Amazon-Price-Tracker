# import the required packages
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# Your Twilio account Details
account_sid = "Your Twilio account sid "
auth_token = "Your Twilio auth token"
client = Client(account_sid, auth_token)

URL = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B07SDPTPC6/" # Url of the website you want to do webscrapping

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}

def send_message(title,price): # this function sends text messages to respective phone number
    message = client.messages.create(
        from_= '+16592013973', #Enter Your Twilio phone no
        body= "Price Drop Detected {} in{}".format(title, price), # The message you want to send
        to='+911234567890', #Enter the number you wan to send message to 
    )
    print(message.sid)

def price_tracker():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip() # finds the element by its respective id 

    price = soup.find(id="priceblock_ourprice").get_text().strip(",")[2:].split(".")[0] # finds the element by its respective id 

    coverted_price = int(price.replace(",", "")) # replaces the "," or removes the commas

    if coverted_price <= 165000:
        send_message(title, price) # If fall in price detected the send_message function is called 
    
    else: 
        print("No Price Drop Detected")

price_tracker()
