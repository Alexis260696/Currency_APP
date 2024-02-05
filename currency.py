import requests
from currency_config import *
from currency_funcions import *
import pandas as pd
from twilio.rest import Client

prices = []
data_DF = []
# Making our request
for i in CURRENCY:
    url = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/latest/' + i
    # Where use CURRENCY list like a base currency 
    response = requests.get(url)
    data = response.json()
    prices.append("el precio de " + i + " en 'MXN' es " + str(data["conversion_rates"]["MXN"]))
    data_DF.append(get_price_MXN(data, i))


col = ['Date', 'Currency', 'B.C', 'Price']
df = pd.DataFrame(data_DF,columns=col)


message = '\nHi! \n\n\n This is the price of the currencys  \n\n\n'+ str(df)
print(message)

"""Open code block in new page

from twilio.rest import Client

account_sid = 'AC44da1d587a0639b6e84ba2f6746b2807'
auth_token = '399c30e6a5298db8c4daf7abb224f9ff'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+5213330601213'
)

print(message.sid)"""