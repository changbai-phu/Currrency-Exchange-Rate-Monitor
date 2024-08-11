#CERM: currency exchange rate monitor 
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


class CurrencyMonitor:
    def __init__(self):
        self.send_email()

    # update the url for the corresponding currency rate page, this only scraping CAD and CNY
    def fetch_exchange_rate(self):
        url = "https://g.co/finance/CAD-CNY"  
        print("Fetching...")
        #headers = {}
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            soup_format = soup.prettify()
            #holders = soup.find_all('div', class_='YMlKec fxKbKc')
            div_element = soup.find('div', {'data-source':'CAD', 'data-target':'CNY'})
            if div_element:
                # print(div_element)
                last_price = div_element.get('data-last-price')
                last_market_timestamp = div_element.get('data-last-normal-market-timestamp')
                unix_timestamp = int(last_market_timestamp)
                last_timestamp_converted = datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"The last price is: {last_price} for date: {last_timestamp_converted}")
                return(last_timestamp_converted, last_price)
            else:
                print("No matching element")
            # In case if you want to output the reponse to a separate file instead showing in terminal, uncomment below
            # print("Writing to the text file response.txt...")
            # f = open('response.txt', 'w')
            # f.write(soup_format)
            # f.close()

    def send_email(self):
        # NOTE: if your are using outlook for sender email, you can keep smtp_server below unchanged, otherwise, update the value correspondingly
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        # update the path where your .env file located
        load_dotenv('/Users/Downloads/vscode/CurrencyMonitor/venv/.env')
       
        # update using your own sender and receiver email
        sender_email = 'yourownsenderemail@outlook.com'
        sender_email_password = os.getenv("password")
        receiver_email = 'yourownreceivereail@xxx.com'
        timestamp, price = self.fetch_exchange_rate()
        body = f"Here is the currency exchange rate of CAD to CNY: {price} for date: {timestamp}"
        print(body)
        
        # construct email content
        subject = 'Currency Exchange Rate Update'
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # send email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_email_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
        except Exception as e:
            print(f'Failed to send email: {e}')
        finally:
            server.quit()

if __name__== "__main__":
    CurrencyMonitor()
        

