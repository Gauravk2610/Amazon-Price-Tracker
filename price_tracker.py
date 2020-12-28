import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = "AC7e50d4f036713c2d80a7fc5837c03de2"
auth_token = "04847618441ed3b66e70a91a0d04d7a7"
client = Client(account_sid, auth_token)

URL = "https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B07SDPTPC6/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}


def send_message(title,price):
    message = client.messages.create(
        from_= '+16592013973',
        body= "Price Drop Detected {} in{}".format(title, price),
        to='+919987882211',
    )
    print(message.sid)

def price_tracker():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()

    price = soup.find(id="priceblock_ourprice").get_text().strip(",")[2:].split(".")[0]

    coverted_price = int(price.replace(",", "")) 

    if coverted_price <= 165000:
        send_message(title, price)
    
    else: 
        print("No Price Drop Detected")

price_tracker()
