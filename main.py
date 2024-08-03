
import requests
from bs4 import BeautifulSoup
import smtplib

yahoo_password = "your password" #generate an app password from the email provider after turning on 2FA or use regular password if 2FA not used
username = "your email"

amz_headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Accept-Language': 'en-US, en;q=0.5'
}

#place the link of a product you want to be notified of if it ever drops price
amz_url = "https://www.amazon.in/Robotic-Vacuum-Mop-Professional-Navigation-Assistant/dp/B0B52219KP/ref=sr_1_4?sr=8-4"

response = requests.get(
    url=amz_url,
    headers=amz_headers
).text

soup = BeautifulSoup(response, "html.parser")
current_price_list = soup.find(class_="a-price-whole").text.split(",")
current_price = int(current_price_list[0] + current_price_list[1])
print(current_price)
#current_price = 15000

if current_price < 20000:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=username, password=yahoo_password)
        connection.sendmail(from_addr=username,
                            to_addrs=username,
                            msg="Price drop alert!!!\nThe price of Mi Robotic Vaccum Mop Professional dropped under than 30000"
                            )
