from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.http import HttpResponse
from .models import Ticker
from .forms import Ticker_Create

# Create your views here.
import yahoo_fin.stock_info as si
import yahoo_fin.options as opt

import requests
import pandas as pd
import ftplib
import io
import requests_html
import requests
# Create your views here.
def RSI_calculator(close_prices):
    up_sum = 0
    down_sum = 0
    up_avg = 0
    down_avg = 0

    for i in range(0, len(close_prices) - 1):
        if (close_prices[len(close_prices) - 1 - i] - close_prices[len(close_prices) - 2 - i] > 0):
            # print("Seems like there was some up. The amount of the up is: ",close_prices[len(close_prices)-1-i]-close_prices[len(close_prices)-2-i],". I got it by subtracting",close_prices[len(close_prices)-2-i]," from",close_prices[len(close_prices)-1-i] )
            up_sum += close_prices[len(close_prices) - 1 - i] - close_prices[len(close_prices) - 2 - i]
        elif (close_prices[len(close_prices) - 1 - i] - close_prices[len(close_prices) - 2 - i] < 0):
            # print("Seems liks there was some down. The amount of down is: ",close_prices[len(close_prices)-1-i]-close_prices[len(close_prices)-2-i],". I got it by subtracting",close_prices[len(close_prices)-2-i]," from",close_prices[len(close_prices)-1-i])
            down_sum += abs(close_prices[len(close_prices) - 1 - i] - close_prices[len(close_prices) - 2 - i])

    up_avg = up_sum / 14
    down_avg = down_sum / 14
    RS = up_avg / down_avg
    RSI = 100 - 100 / (1 + RS)
    return RSI


nasdaq_tickers = ["tsla", "aapl", "msft", "cost", "fb", "ual", "gme", "amc", "pltr", "fubo", "amzn", "rblx", "amd",
                  "nvda", "qs", "ba", "spce", "lcid", "an", "azo", "nvr", "googl", "bkng", "gm", "r", "y", "re", "tw",
                  "ko", "ew"]
nasdaq_rsi = []
for ticker in nasdaq_tickers:
    stock_daily = si.get_data(ticker, start_date="12/16/2021", end_date="01/07/2022", interval="1d")
    nasdaq_rsi.append(RSI_calculator(stock_daily['close']))
#########################################################################################################################

import numpy as np
from sklearn.linear_model import LinearRegression




def ticker_show(request):
    if(request.method == "POST"):
        print("Yes it was Post")
    else:
        print("No it was not POST")
    ticker_name = request.POST.get("Ticker")
    starting_date = request.POST.get("start_date")
    ending_date = request.POST.get("ending_date")
    print(starting_date)
    print(ending_date)

    stock_daily = si.get_data(ticker_name, start_date=starting_date, end_date=ending_date, interval="1d")
    ticker_RSI = RSI_calculator(stock_daily['close'])

    new_model = LinearRegression()
    time_range = []
    for i in range(1,len(stock_daily['close'])+1):
        time_range.append(i)
    np_trange = np.array(time_range).reshape(-1,1)

    close_values = np.array(stock_daily['close'])
    new_model.fit(np_trange,close_values)

    predicted_value = new_model.predict([[len(stock_daily['close'])+7]])
    context = {
        'Ticker_name':ticker_name,
        'Ticker_RSI':ticker_RSI,
        'predicted_value':predicted_value

    }
    return render(request,"Stock_Info.html",context)
def home_show(request):
    context = {

    }
    return render(request,"home.html",context)

def image_html(request):
    context = {

    }
    return render(request,"image.html",context)

class new_Ticker(CreateView):
    model = Ticker
    fields = '__all__'


class show_Ticker(ListView):
    model = Ticker
    template_name = "show.html"


class ticker_Detail(DetailView):
    model = Ticker
    template_name = "detail.html"


class ticker_Update(UpdateView):
    model = Ticker
    template_name = "update.html"
    fields = ('Ticker_name','Price','Market_cap')