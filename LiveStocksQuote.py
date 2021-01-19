import requests
from bs4 import BeautifulSoup
import pyfiglet
from colorama import init
from termcolor import colored
init()

ascii_art=colored(pyfiglet.figlet_format("Get Live Stock Quotes!!!"),color='blue')
print(ascii_art)

print("Example: AMZN for Amazon, AAPL for Apple, etc.")
symbol=input("Enter a stock symbol/ticker here: ")

url=f"https://finance.yahoo.com/quote/{symbol.upper()}"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

print("\nCompany Details: ",soup.title.text)
print(soup.find("span",{"data-reactid":"35"}).text)
print("Price: ",soup.find("div",{"class":"D(ib) Mend(20px)"}).find_all("span")[0].text)
print("Changes: ",soup.find("div",{"class":"D(ib) Mend(20px)"}).find_all("span")[1].text)




	
