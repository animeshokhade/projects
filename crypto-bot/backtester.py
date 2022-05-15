import matplotlib.pyplot as plt 
import requests, json

def moving_averages(historical_data, ticker, cash):
    """
    If the 3 day average price of ETH is above the 5 day average price -> buy. 
    else -> sell
    """
    initial = int(cash)
    cash = int(cash)
    crypto = 0
    x_values = []
    y_values = []
    for place, data_set in enumerate(historical_data[5:-1]):
        three_day_average = get_average([historical_data[place - 1], historical_data[place - 2], historical_data[place - 3]])
        five_day_average = get_average([historical_data[place - 1],
                                        historical_data[place - 2],
                                        historical_data[place - 3],
                                        historical_data[place - 4],
                                        historical_data[place - 5]])
        if three_day_average > five_day_average:
            cash_used_to_buy = cash / 2
            price = float(data_set["close"])
            number_of_crypto_we_just_bought = cash_used_to_buy / price
            crypto += number_of_crypto_we_just_bought
            cash -= cash_used_to_buy
            print("Just purchased: " + str(number_of_crypto_we_just_bought) + " " + ticker)
        
        if crypto > 1 and three_day_average < five_day_average: 
            price = float(data_set["close"])
            number_of_crypto_being_sold = crypto / 2
            new_cash = number_of_crypto_being_sold * price
            cash += new_cash
            crypto -= number_of_crypto_being_sold
            print("Just sold: " + str(number_of_crypto_being_sold) + " " + ticker)
        
        portfolio_value = cash + (crypto * float(data_set["close"]))
        x_values.append(place)
        y_values.append(portfolio_value)

    print("Final portfolio value: " + str(portfolio_value))
    net = portfolio_value - initial
    if (net > 0): 
        print("You profited: " + str(net))
    else: 
        print("You lost: " + str(net))

    plot_graph(x_values, y_values)

def get_average(averages_list):
    """
    Gets the average of some numbers
    """
    total = 0
    for data_set in averages_list: 
        total += float(data_set["close"])
    return total / len(averages_list)

def plot_graph(x, y):
    """
    Plots the report
    """
    plt.plot(x, y)
    plt.xlabel("Minute")
    plt.ylabel("Portfolio Value") 
    plt.show()

def start(): 
    '''
    We ask the user for some basic input, fetch our historical data
    and determine what strategy to use. 
    '''
    print("Starting Crypto Backtester V1")

    ticker = input("Enter ticker: ").upper()
    data_url = 'https://min-api.cryptocompare.com/data/histominute?fsym=' + ticker + '&tsym=USD&limit=2000&aggregate=1'
    response = requests.get(data_url)

    try: 
        data = response.json()['Data']
    except: 
        print("Sorry, this crypto isn't supported!")
        quit()
    
    historical_data = data
    print("Fetched historical data for crypto: ") + ticker 
    cash = input("Enter initial investment: ") 

    strategy = input("Select (1) for the moving averages strategy: ")
    if strategy == '1':
        moving_averages(historical_data, ticker, cash)

start()