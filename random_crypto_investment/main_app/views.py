from django.shortcuts import render
from django.http import HttpResponse
from binance.spot import Spot as Client
from django.template import loader
import secrets

# Create your views here.
def main_app(request):
    client = Client(api_key='BcwkUYItqUyNcowmSjBIS4YhKQwVuYzsXdh7Uvuqo3r9yYcmZ3GbEhMmoBhvfkG6', api_secret='lp6jQ7f8ZPTKoizCTx2oLSwMsRUAaAILYe9eFtqtKsCxoBeThiv1Pi87Lafk2903')
    market_pairs = client.exchange_info()
    
    sym = list()

    for s in market_pairs['symbols']:
        if s['symbol'].endswith('USDT'):
            sym.append(s['symbol'][:-4])

    coin = secrets.choice(sym)

    template = loader.get_template("main_app.html")

    context = {'coin': coin}
    return render(request, 'main_app.html', context)