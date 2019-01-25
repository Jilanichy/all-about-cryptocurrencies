from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = api_request.json()

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,BCH,EOS,LTC,XLM&tsyms=USD")
    price = price_request.json()
    return render(request, 'home.html', {'price': price, 'news': news})


def prices(request):
    import json
    import requests
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = crypto_request.json()
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        empty = "Please enter a Cryptocurrency Name into the search box to see datails."
        return render(request, 'prices.html', {'empty': empty})
