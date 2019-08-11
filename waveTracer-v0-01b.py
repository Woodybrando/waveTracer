import pprint
import pywaves as pw
import os
import configparser
import csv
import time
import datetime
import requests
from termcolor import colored, cprint


class waveTracer:
    def __init__(self):
        self.log_file = "bot.log"
        self.node = "https://nodes.wavesnodes.com"
        self.chain = "mainnet"
        self.matcher = "https://matcher.wavesnodes.com"
        self.order_fee = 300000
        self.order_lifetime = 30 * 86400  # 30 days
        self.private_key = ""
        self.private_key_BTC = ""
        self.amount_asset = ""
        self.price_asset_id = ""
        self.price_asset = pw.Asset(self.price_asset_id)
        self.price_step = 0.005
        self.min_amount = 10000
        self.seconds_to_sleep = 15

    def log(self, msg):
        timestamp = datetime.datetime.utcnow().strftime("%b %d %Y %H:%M:%S UTC")
        s = "[{0}]:{1}".format(timestamp, msg)
        print(s)
        try:
            f = open(self.log_file, "a")
            f.write(s + "\n")
            f.close()
        except OSError:
            pass

    def read_config(self, cfg_file):
        if not os.path.isfile(cfg_file):
            self.log("Missing config file")
            self.log("Exiting.")
            exit(1)

        try:

            # Config File Stuff

            self.log("Reading config file '{0}'".format(cfg_file))
            config = configparser.RawConfigParser()
            config.read(cfg_file)

            # Get Matcher and Node

            self.node = config.get('main', 'node')
            self.chain = config.get('main', 'network')
            self.matcher = config.get('main', 'matcher')
            self.order_fee = config.getint('main', 'order_fee')
            self.order_lifetime = config.getint('main', 'order_lifetime')
            self.private_key = config.get('account', 'private_key')
            self.private_key_BTC = config.get('account', 'private_key_BTC')
            self.amount_asset_id = config.get('market', 'amount_asset')

            # Get Asset Pair

            self.amount_asset = pw.Asset(self.amount_asset_id)
            self.price_asset_id = config.get('market', 'price_asset')
            self.price_asset = pw.Asset(self.price_asset_id)

        except OSError:
            self.log("Error reading config file")
            self.log("Exiting.")
            exit(1)

def main():


    # add first time enter private key
    # and add copy paste of the code asking for it
    # remind people to keep it secret
    # add encryption to it

    #
    #
    #       Set Settings
    #
    #
    #

    configFile = "config-Multi-Matrix.cfg"


    bot = waveTracer()
    bot.read_config(configFile)
    pw.setNode(node=bot.node, chain=bot.chain)
    pw.setMatcher(node=bot.matcher)
    my_addressWaves = pw.Address(privateKey=bot.private_key)
    my_addressBTC = pw.Address(privateKey=bot.private_key_BTC)

    # Set Assets

    VST = pw.Asset("4LHHvYGNKJUg5hj65aGD5vgScvCBmLpdRFtjokvCjSL8")
    Waves = pw.Asset("")
    BTC = pw.Asset("8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS")
    BCH = pw.Asset("zMFqXuoyrn5w17PFurTqxB7GsS71fp9dfk6XFwxbPCy")
    XMR = pw.Asset("5WvPKSJXzVE2orvbkJ8wsQmmQKqTv9sGBPksV4adViw3")
    USD = pw.Asset("Ft8X1v1LTa1ABafufpaCWyVj8KkaxUWE6xBhW6sNFJck")

    # Set letter variables

    a = 1
    b = 2
    c = 3
    d = 4
    A = a
    B = b
    C = c
    D = d
    textO = ''
    account = ''

    # Set Pairs

    vst_waves = pw.AssetPair(VST, Waves)

    vst_btc = pw.AssetPair(VST, BTC)

    waves_btc = pw.AssetPair(Waves, BTC)

    waves_usd = pw.AssetPair(Waves, USD)

    bch_waves = pw.AssetPair(BCH, Waves)

    bch_usd = pw.AssetPair(BCH, USD)

    xmr_waves = pw.AssetPair(XMR, Waves)



    # Welcome aboard waveTracer

    cprint('\n'
           '\n'
        '.:( .:( .:(   Welcome to waveTracer   ):. ):. ):.', 'cyan', attrs=['blink'])

    # Read in account names from sheet

    accountsPairs = './matrices/Accounts-Pairs-d1b.csv'
    aPairs = csv.reader(open(accountsPairs))
    linesAP = list(aPairs)
    accountOne = linesAP[1][0]
    accountTwo = linesAP[2][0]
    accountThree = linesAP[3][0]
    accountFour = linesAP[4][0]

    # Set Account

    while account != 'exit' and account != 'a' and account != 'b':

        print('')
        cprint('Which Account to work with?', 'green')
        print('')
        cprint('a. ' + accountOne , 'white')
        cprint('b. ' + accountTwo, 'white')
        cprint('c. ' + accountThree , 'white')
        cprint('d. ' + accountFour , 'white')

        account = input('')

        if str(account) == 'a' or str(account) == 'A':
            my_address = my_addressWaves
            accountName = 'One'
            account = 'a'

        if str(account) == 'b' or str(account) == 'B':
            my_address = my_addressBTC
            accountName = 'Two'
            account = 'b'


    # Set Trading Pair

    # ADD - Set trading style
    # - scalp trace (.1 to .9) -
    # - simple retrace (minus 1) -
    # - bear retrace (minus 3 - 10) -
    # - spiderNade (8 sell #'s per buy) -
    # - multicoat retrace for instance 50 sell become 55 rebuy, become 52 sell + 2 and 1 to next 2

    # cprint('\n'
    #        'the year is 1978, and command prompt is the cutting edge of computer interfacing, enjoy.' '\n')
    #

    pairA = './matrices/VST-Waves-Matrix-d2b.csv'
    pairB = './matrices/VST-BTC-Matrix-d1b.csv'
    pairC = './matrices/WAVES-BTC-Matrix-d2b.csv'
    pairD = './matrices/BCH-WAVES-Matrix-d1b.csv'
    pairE = './matrices/XMR-WAVES-Matrix-d1b.csv'
    pairF = './matrices/Waves-USD-Matrix-d2b.csv'
    pairG = './matrices/BCH-USD-Matrix-d1b.csv'


    print('')
    cprint('Which pair do you want to work with?' '\n', 'green')
    cprint(         'a. VST / WAVES', 'grey', 'on_white')
    cprint(         'b. VST / BTC', 'grey', 'on_white')
    cprint(         'c. WAVES / BTC', 'grey', 'on_white')
    cprint(         'd. BCH / WAVES', 'grey', 'on_white')
    cprint(         'e. XMR / WAVES', 'grey', 'on_white')
    cprint(         'f. WAVES / USD ', 'grey', 'on_white')
    cprint(         'g. BCH / USD ', 'grey', 'on_white')
    pick = input('')
    cprint('\n', 'white')

    if str(pick) == 'a' or str(pick) == 'A':

        with open(pairA) as matrixVW:
            rVW = csv.reader(matrixVW)
            lines = list(rVW)

        pairName = 'VST / WAVES'
        pair = vst_waves
        pairCSV = pairA

    if str(pick) == 'b' or str(pick) == 'B':
        with open(pairB) as matrixVB:
            rVB = csv.reader(matrixVB)
            lines = list(rVB)

        pairName = 'VST / BTC'
        pair = vst_btc
        pairCSV = pairB


    if str(pick) == 'c' or str(pick) == 'C':

        with open(pairC) as matrixWB:
            rWB = csv.reader(matrixWB)
            lines = list(rWB)

        pairName = 'WAVES / BTC'
        pair = waves_btc
        pairCSV = pairC


    if str(pick) == 'd' or str(pick) == 'D':

        with open(pairD) as matrixBW:
            rBW = csv.reader(matrixBW)
            lines = list(rBW)

        pairName = 'BCH / WAVES'
        pair = bch_waves
        pairCSV = pairD


    if str(pick) == 'e' or str(pick) == 'E':

        with open(pairE) as matrixXW:
            rBW = csv.reader(matrixXW)
            lines = list(rBW)

        pairName = 'XMR / WAVES'
        pair = xmr_waves
        pairCSV = pairE


    if str(pick) == 'f' or str(pick) == 'F':

        with open(pairF) as matrixXW:
            rBW = csv.reader(matrixXW)
            lines = list(rBW)

        pairName = 'WAVES / USD'
        pair = waves_usd
        pairCSV = pairF



    if str(pick) == 'g' or str(pick) == 'G':

        with open(pairG) as matrixXW:
            rBW = csv.reader(matrixXW)
            lines = list(rBW)

        pairName = 'BCH / USD '
        pair = bch_usd
        pairCSV = pairG


    cprint('\n', 'white')


    #
    #    Order Spreadsheet Printer
    #

    # load order book

    order_book = pair.orderbook()


    # set CSV cells

    # decCSV csv value location
    decCSVRow = 0
    decCSVCol = 2

    dec = int(lines[decCSVRow][decCSVCol])


    # retraceCSV csv value location
    retraceCsvRow = 1
    retraceCsvCol = 2
    reTrace = int(lines[retraceCsvRow][retraceCsvCol])

    # priceAsset csv value location
    priceAssetRow = 0
    priceAssetCol = 4

    # amountAsset csv value location
    amountAssetRow = 1
    amountAssetCol = 4

    # pairString csv value location
    pairStringRow = 0
    pairStringCol = 6

    # pairName csv value location
    pairNameRow = 1
    pairNameCol = 6

    # topRow csv value location
    topRowRow = 0
    topRowCol = 8
    sellStopRow = int(lines[topRowRow][topRowCol])


    # bottomRow csv value location
    bottomRowRow = 1
    bottomRowCol = 8
    buyStopRow = int(lines[bottomRowRow][bottomRowCol])


    # lowSellRow csv value location
    lowSellCsvRow = 0
    lowSellCsvCol = 10
    lowSellRow = int(lines[lowSellCsvRow][lowSellCsvCol])


    # hiBuyRow csv value location
    hiBuyCsvRow = 1
    hiBuyCsvCol = 10
    hiBuyRow = int(lines[hiBuyCsvRow][hiBuyCsvCol])

    # Price Column
    priceCol = 1

    # ID Column
    csvIdCol = 4


    text2 = 'none'
    text3 = 'none'
    previousID = 'none'
    orderNum = 'enter'
    check = 'check'


    cprint('\n'
           '\n'
           '\n', 'blue')

    cprint('waveTracer v0.01a', 'cyan' )
    print("Account: " + accountName + ', Pair: ' + pairName)

    #print('ask: ' + str(order_book['asks'][00]['price']) + ', bid: ' + str(order_book['bids'][00]['price']) +  '\n')
    #print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: ' + str(order_book['bids'][00]['price'] / dec) +  '\n')
    cprint(            "' a. Set up initial matrix sell orders '", 'red')
    cprint(            "' b. Set up initial matrix buy orders '", 'green')
    cprint(            "' c. Start retrace engine '", 'cyan')
    cprint(            "' d. Work with orders '", 'grey', 'on_white')

    print('\n')


    text = input('')

    if text == 'a' or text == 'A':
        text = 'sells'

    if text == 'b' or text == 'B':
        text = 'buys'

    if text == 'c' or text == 'C':
        text = 'retrace'

    if text == 'd' or text == 'D':
        text = 'orders'

    textA = ''

    if text == 'orders':
        while textA != 'exit':
            text1 = ''
            textA = ''
            status = ''

            orderNum = 'enter'
            cprint('\n'
                   '\n'
                   '\n', 'blue')

            cprint('waveTracer v0.01a', 'cyan')
            print("Account: " + accountName + ', Pair: ' + pairName)

            print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                  + str(order_book['bids'][00]['price'] / dec) +  '\n')

            cprint("' a. Check on a single order id '", 'cyan')
            cprint("' b. Check last orders '", 'blue')
            cprint("' c. See your full order history or type filled, accepted or cancelled '", 'red')
            cprint("' d. Post a single order '", 'green')
            cprint("' e. Cancel orders '", 'magenta')
            cprint("' f. Data Transaction '", 'blue', 'on_white')
            cprint("' g. Get a Matrix from Data Transaction '", 'magenta', 'on_cyan')

            print('')
            textA = input('')

            if textA == 'a' or textA == 'A':
                text1 = 'order'

            if textA == 'b' or textA == 'B':
                text1 = 'lastorders'

            if textA == 'c' or textA == 'C':
                text1 = 'orders'

            if textA == 'd' or textA == 'D':
                text1 = 'post'

            if textA == 'e' or textA == 'E':
                text1 = 'cancel'

            if textA == 'f' or textA == 'F':
                text1 = 'data'

            if textA == 'g' or textA == 'G':
                text1 = 'getData'


            if textA == 'filled' or textA == 'FILLED':
                status = 'Filled'
                status2 = 'Stop'
                text1 = 'orders'
                textA = 'less'

            if textA == 'accepted' or textA == 'ACCEPTED':
                status = 'Accepted'
                status2 = 'PartiallyFilled'
                text1 = 'orders'
                textA = 'less'

            if textA == 'cancelled'  or textA == 'CANCELLED':
                status = 'Cancelled'
                status2 = 'Stop'
                text1 = 'orders'
                textA = 'less'


            if text1 == 'order':

                while text2 != 'exit':

                    cprint('waveTracer v0.01a', 'cyan')
                    print("Account: " + accountName + ', Pair: ' + pairName)

                    print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                    + str(order_book['bids'][00]['price'] / dec) +  '\n')
                    text2 = input('Enter orderId to check on:')

                    myOrders = my_address.getOrderHistory(assetPair=pair)
                    for row in myOrders:
                        if str(row['id']) == text2:
                            pprint.pprint(row)
                            orderTime = row['timestamp']
                            dt_object = datetime.datetime.fromtimestamp(orderTime/ 1e3)
                            print("Time order was " + row['status'] + " " + str(dt_object))
                            print('')


            if text1 == 'orders':
                while orderNum != 'exit':
                    myOrders = my_address.getOrderHistory(assetPair=pair)

                    if textA == 'c' or textA == 'C':
                        pprint.pprint(myOrders)
                        print('')

                        orderNum = 'exit'

                    if textA == 'less':

                        cprint('waveTracer v0.01a', 'cyan')
                        print("Account: " + accountName + ', Pair: ' + pairName)

                        print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                              + str(order_book['bids'][00]['price'] / dec) + '\n')

                        #print("did it work?")

                        matrix = {}
                        matrixList = []
                        rowMat = 0

                        for row in myOrders:
                            if str(row['status']) == status:

                                matrix['price'] = row['price']
                                matrix['amount'] = row['amount']
                                matrix['id'] = row['id']
                                matrix['type'] = row['type']
                                matrix['status'] = row['status']

                                matrixList.append(matrix.copy())

                                rowMat = rowMat + 1



                                orderNum = 'exit'

                            elif str(row['status']) == status2:

                                matrix['price'] = row['price']
                                matrix['amount'] = row['amount']
                                matrix['id'] = row['id']
                                matrix['type'] = row['type']
                                matrix['status'] = row['status']

                                matrixList.append(matrix.copy())

                                rowMat = rowMat + 1



                                orderNum = 'exit'

                        #print(matrixList)
                        sortedMatrix = sorted(matrixList, key=lambda k: k['price'], reverse=True)
                        for row in sortedMatrix:

                            print(str(row['type']) + ' @ price: ' + str(row['price']),
                                  ', amount: ' + str(row['amount']) + ' id: ' + str(row['id'])
                                  + ' status: ' + row['status'])

            if text1 == 'lastorders':

                while text3 != 'exit':

                    cprint('waveTracer v0.01a', 'cyan')
                    print("Account: " + accountName + ', Pair: ' + pairName + '\n')

                    text3 = input('Enter Order index 0 - 99 or exit:')

                    myOrders = my_address.getOrderHistory(assetPair=pair)
                    if text3 != 'exit':
                        text3 = int(text3)
                        order = myOrders[text3]

                        orderTime = order['timestamp']
                        dt_object = datetime.datetime.fromtimestamp(orderTime/ 1e3)
                        print("Time order was " + order['status'] + " " + str(dt_object))
                        pprint.pprint(order)
                        print('')

            if text1 == 'data':

                while text2 != 'exit':
                    text2 = input('Ready to send your current ' + pairName + ' Matrix data Transaction? yes or no')

                    if text2 == 'yes':
                        data = []
                        count = 0

                        with open(pairCSV, newline='') as matrixData:
                            rBW = csv.reader(matrixData)
                            lines2 = list(rBW)


                        for one in lines2:
                            #b = one
                            #print(b)

                            c = str(one)[1:-1]
                            #print(c)

                            matrixDict = {'type': 'string', 'key': str(count), 'value': c}

                            #case = {'key1': entry[0], 'key2': entry[1], 'key3': entry[2]}
                            #case_list.append(case)

                            data.append(matrixDict)
                            count = count + 1

                        pprint.pprint(data)
                        pprint.pprint(data)


                    #
                    # data = [{
                    #
                    #
                    #     'type': 'string',
                    #     'key': '0',
                    #     'value': '0,1-price,2-volume,3-wavesVol,4-floatVolume,5-orderID,6-lastRow',
                    # },
                    #     {
                    #
                    #
                    #     'type': 'string',
                    #     'key': '1',
                    #     'value': '1,1.581,15,23.715,,,decCSV',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '2',
                    #     'value': '2,1.518,12,18.216,,,100000000'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '3',
                    #     'value': '3,1.396,13,18.148,,,lowSellRow',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '4',
                    #     'value': '4,1.281,15,19.215,,,24'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '5',
                    #     'value': '5,1.118,17,19.006,,,hiBuyRow',
                    #
                    # },
                    # {
                    #
                    #     'type': 'string',
                    #     'key': '6',
                    #     'value': '6,1.016,19,19.304,,,26',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '7',
                    #     'value': '7,0.967,20,19.34,,,topRow'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '8',
                    #     'value': '8,0.919,21,19.299,,,1',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '9',
                    #     'value': '9,0.872,22,19.184,,,bottomRow'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '10',
                    #     'value': '10,0.826,23,18.998,,,38',
                    #
                    #     },
                    #     {
                    #
                    #
                    #     'type': 'string',
                    #     'key': '11',
                    #     'value': '11,0.774,24,18.576,,,retraceCSV',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '12',
                    #     'value': '12,0.724,25,18.1,,,1'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '13',
                    #     'value': '13,0.649,28,18.172,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '14',
                    #     'value': '14,0.575,31,17.825,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '15',
                    #     'value': '15,0.524,33,17.292,,,',
                    #
                    # },
                    # {
                    #
                    #     'type': 'string',
                    #     'key': '16',
                    #     'value': '16,0.474,35,16.59,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '17',
                    #     'value': '17,0.427,38,16.226,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '18',
                    #     'value': '18,0.392,41,16.072,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '19',
                    #     'value': '19,0.358,42,15.036,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '20',
                    #     'value': '20,0.325,43,13.975,,,',
                    #
                    # },
                    #     {
                    #
                    #
                    #     'type': 'string',
                    #     'key': '21',
                    #     'value': '21,0.292,44,12.848,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '22',
                    #     'value': '22,0.261,45,11.745,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '23',
                    #     'value': '23,0.23,46,10.58,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '24',
                    #     'value': '24,0.2,47,9.4,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '25',
                    #     'value': '25,0.166,50,8.3,,,',
                    #
                    # },
                    # {
                    #
                    #     'type': 'string',
                    #     'key': '26',
                    #     'value': '26,0.155,52,8.06,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '27',
                    #     'value': '27,0.144,60,8.64,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '28',
                    #     'value': '28,0.133,65,8.645,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '29',
                    #     'value': '29,0.122,70,8.54,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '30',
                    #     'value': '30,0.111,75,8.325,,,',
                    #
                    # },
                    #     {
                    #
                    #
                    #     'type': 'string',
                    #     'key': '31',
                    #     'value': '31,0.092,85,7.82,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '32',
                    #     'value': '32,0.087,90,7.83,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '33',
                    #     'value': '33,0.074,105,7.77,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '34',
                    #     'value': '34,0.061,115,7.015,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '35',
                    #     'value': '35,0.049,125,6.125,,,',
                    #
                    # },
                    # {
                    #
                    #     'type': 'string',
                    #     'key': '36',
                    #     'value': '36,0.035,150,5.25,,,',
                    # },
                    #
                    # {
                    #     'type': 'string',
                    #     'key': '37',
                    #     'value': '37,0.024,45,1.08,,,'
                    # },
                    # {
                    #     'type': 'string',
                    #     'key': '38',
                    #     'value': '38,0.01,78,0.78,,,',
                    #
                    # }]
                    #

                    dataOrder = my_address.dataTransaction(data)
                    pprint.pprint(dataOrder)

                    orderNum = 'exit'

                    #myOrders = my_address.getOrderHistory(assetPair=pair)
                    #pprint.pprint(myOrders[0])

            if text1 == 'getData':

                while text2 != 'exit':

                    cprint('waveTracer v0.01a', 'cyan')
                    print("Account: " + accountName + ', Pair: ' + pairName)

                    print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                          + str(order_book['bids'][00]['price'] / dec) + '\n')

                    text2 = input('Enter Data Transaction ID: i.e. Ga5bWqure9tDTuG5mjvbj7rkrgqtVZGWgDa1s7uCT48N '
                                    + 'or D7d1hEiqN91TBZz82PL4hxqura5eKkWwMZPW6oKfv647'
                                  + '\n' )

                    print('')

                    if text2 != 'exit':

                        dataMatrix = requests.get('https://api.wavesplatform.com/v0/transactions/data/' + text2)
                        jsonMatrix = dataMatrix.json()

                        #print(jsonMatrix['data']['data'])
                        with open('./matrices/temp-waves-btc-d1a.csv', 'wt', newline='\n') as matrixWrite:
                            writer = csv.writer(matrixWrite, quoting=csv.QUOTE_NONE, escapechar='\\')
                            count = 0
                            while count < 81:
                                writer.writerows([[jsonMatrix['data']['data'][count]['value']]])
                                count = count + 1
                                print(count)

                        with open('./matrices/temp-waves-btc-d1a.csv') as in_file,\
                                open('./matrices/new-waves-btc-d1b.csv', 'w') as out_file:
                            for line in in_file:
                                out_file.write(line.replace('\\', ''))


                        with open('./matrices/new-waves-btc-d1b.csv') as in_file,\
                                open('./matrices/temp-waves-btc-d1a.csv', 'w') as out_file:
                            for line in in_file:
                                out_file.write(line.replace("'", ''))


                        with open('./matrices/temp-waves-btc-d1a.csv') as in_file,\
                                open('./matrices/new-waves-btc-d1b.csv', 'w') as out_file:
                            for line in in_file:
                                out_file.write(line.replace(" ", ''))

                            # for row in jsonMatrix['data']['data']:
                            #     writer.writerows(row['value'])

                                #print(row['value'])

                        print('')
                        cprint('Commit Matrix to waveTracer for pair: ' + '\n' + '\n'
                               + pairName + '\n' + str(pair) + '\n' + '\n'
                               + ' WARNING: THIS WILL OVERWRITE YOUR LOCAL MATRIX FILE')

                        input('')
                        orderNum = 'exit'



            if text1 == 'post':

                myOrders = ''

                text4 = 'enter'

                while text4 != 'exit':

                    cprint('waveTracer v0.01a', 'cyan')
                    print("Account: " + accountName + ', Pair: ' + pairName)
                    print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                    + str(order_book['bids'][00]['price'] / dec) +  '\n')
                    print('')
                    cprint('Post a buy or sell?')
                    text4=input('')
                    type = text4


                    cprint("At what Price?",)
                    text4 = input('')
                    price = float(text4)

                    cprint("What amount?")
                    text4 = input('')
                    volume = float(text4) * 10e7
                    volume = int(volume)

                    print('')
                    cprint("Account: " + accountName + ', Pair: ' + pairName, 'cyan' )

                    cprint('Ready to ' + str(type) + ' ' + str(text4) + ' (posting as ' + str(volume) +
                           ') @ ' + str(price) + '? yes or no')
                    text4 = input('')

                    if text4 == 'yes':
                        if type == 'sell':
                            my_address.sell(assetPair=pair, amount=volume, price=price, matcherFee=bot.order_fee,
                                        maxLifetime=bot.order_lifetime)
                            myOrders = my_address.getOrderHistory(assetPair=pair)
                            pprint.pprint(myOrders[0])

                        if type == 'buy':
                            my_address.buy(assetPair=pair, amount=volume, price=price, matcherFee=bot.order_fee,
                                        maxLifetime=bot.order_lifetime)
                            myOrders = my_address.getOrderHistory(assetPair=pair)
                            pprint.pprint(myOrders[0])




            if text1 == 'cancel':

                cprint('waveTracer v0.01a', 'cyan')
                print("Account: " + accountName + ', Pair: ' + pairName)

                print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                      + str(order_book['bids'][00]['price'] / dec) +  '\n')

                cprint('\n'"a. Cancel sells", 'red')
                cprint("b. Cancel buys", 'green')
                cprint( "c. Cancel both?", 'blue')
                cprint( "d. Cancel single order by id?" '\n', 'cyan')

                cancelType = input('')

                if cancelType == 'a' or cancelType == 'A':
                    cancelType = 'sells'
                if cancelType == 'b' or cancelType == 'B':
                    cancelType = 'buys'
                if cancelType == 'c' or cancelType == 'C':
                    cancelType = 'both'
                if cancelType == 'd' or cancelType == 'D':
                    cancelType = 'single'

                myOrders = my_address.getOrderHistory(assetPair=pair)


                if str(cancelType) == 'sells':
                    print("I'm trying to cancel buys...")


                    for order in myOrders:
                        if order['type'] == 'sell' and order['status'] == 'Accepted':
                            orderIdentity = order['id']
                            pprint.pprint(order)
                            my_address.cancelOrderByID(assetPair=pair, orderId=orderIdentity)

                            print('Cancelling order #' + str(order['id']))


                if str(cancelType) == 'buys':
                    print("I'm trying to cancel buys...")

                    for order in myOrders:
                        if order['type'] == 'buy' and order['status'] == 'Accepted':
                            orderIdentity = order['id']
                            pprint.pprint(order)
                            my_address.cancelOrderByID(assetPair=pair, orderId= orderIdentity)


                            print('Cancelling order #' + str(order['id']))

                if str(cancelType) == 'both':
                    my_address.cancelOpenOrders(pair)


                if str(cancelType) == 'single':

                    cprint('waveTracer v0.01a', 'cyan')
                    print("Account: " + accountName + ', Pair: ' + pairName)

                    print('ask: ' + str(order_book['asks'][00]['price'] / dec) + ', bid: '
                          + str(order_book['bids'][00]['price'] / dec) +  '\n')
                    cancelId = ''
                    cancel = ''
                    cprint("Enter Order ID to Cancel:")
                    cancelId = input('')
                    myOrders = my_address.getOrderHistory(assetPair=pair)

                    for row in myOrders:
                        if str(row['id']) == cancelId:
                            pprint.pprint(row)
                            orderTime = row['timestamp']
                            dt_object = datetime.datetime.fromtimestamp(orderTime / 1e3)
                            print("Time order was " + row['status'] + " " + str(dt_object))
                            print('')
                    print('Is this the one to cancel? yes no')
                    cancel = input('')
                    if cancel == 'yes':
                        my_address.cancelOrderByID(assetPair=pair, orderId=cancelId)
                        myOrders = my_address.getOrderHistory(assetPair=pair)

                        for row in myOrders:
                            if str(row['id']) == cancelId:
                                pprint.pprint(row)
                                orderTime = row['timestamp']
                                dt_object = datetime.datetime.fromtimestamp(orderTime / 1e3)
                                print("Time order was " + row['status'] + " " + str(dt_object))
                                print('')


    if text == 'sells':

        row = lowSellRow
        previousId = 'none'

        print("Do you have your matrix open to double check the buy orders?")
        print("a. Yes")
        print("b. no")

        buyCheck = input('')

        if buyCheck == 'a' or buyCheck == 'A':

            while sellStopRow <= row <= lowSellRow :

                lowSellVol = float(lines[row][priceCol+1])
                volume = int(lowSellVol*dec)

                sellPrice = float(lines[row][priceCol])

                price = int(sellPrice * dec)
                price = price / dec


                if check != 'check':
                    print("Volume is " + str(volume))

                    print('Volume row is ' + str(row))
                    print('col is ' + str(priceCol + 1))

                    print('Price row is ' + str(row))
                    print('col is ' + str(priceCol))

                    cprint("price is " + str(price), 'green')
                    print("volume is " + str(volume))

                if check == 'check':
                    cprint('\n' 'This order is going to sell ' + str(volume/dec) + ' @ ' + str(price) + '\n', 'magenta')
                    cprint('Do you want to check each order before selling type: check', 'red')
                    cprint('Do you want to just auto set the rest of the orders: auto', 'green')

                    check = input('')

                if check == 'check' or check == 'auto':

                    my_address.sell(assetPair=pair, amount=volume, price=price, matcherFee=bot.order_fee,
                                                maxLifetime=bot.order_lifetime)

                    bot.log("Post Sell order with price: {0}, amount:{1}".format(price, volume))

                    myOrders = my_address.getOrderHistory(assetPair=pair)

                    pprint.pprint(myOrders[0])

                    idOrder = str(myOrders[0]['id'])

                    lines[int(row)][csvIdCol] = idOrder
                    cprint(lines[int(row)][csvIdCol], 'red')
                    print('')

                    row = row - 1

                    if previousId == idOrder:
                        idOrder = 'Error Writing this Order'
                        print("Error writing this order")
                        print("What next? retry, skip or exit?")
                        whatNext = input('')

                        if whatNext == 'retry':
                            row = row+1
                        if whatNext == 'skip':
                            row = row
                        if whatNext == 'exit':
                            row = 0

                    previousId = idOrder


                    with open(pairCSV, 'w') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerows(lines)


            # add orderID check,

            #col = 2
            #
            # if myOrders[0]['price'] == price:
            #     if myOrders[0]['status'] == 'Accepted':
            #         print('Order of ' + str(price) + ' ' + myOrders[0]['status'])
            #
            #

    # Initial Buy Orders Engine

    row = hiBuyRow
    col = 1

    # csvBuyCol is being put into the lower Buy column to prevent duplicate matches in the id column search for rebuys

    if text == 'buys':

        row = hiBuyRow
        previousId = 'none'

        print("Do you have your matrix open to double check the buy orders for " + pairName + "?")
        print("a. Yes")
        print("b. no")

        buyCheck = input('')



        if buyCheck == 'a' or buyCheck == 'A':

            while buyStopRow >= row >= hiBuyRow:

                # set buy volume

                hiBuyVol = float(lines[row][priceCol+1])
                volume = int(hiBuyVol*dec)

                # set buy price

                hiBuyPrice = float(lines[row][priceCol])

                price = int(hiBuyPrice * dec)
                price = price / dec

                if check != 'check':

                    print('Volume row is ' + str(row))
                    print('col is ' + str(priceCol + 1))
                    print('Price row is ' + str(row))
                    print('col is ' + str(priceCol))
                    cprint("price is " + str(price), 'green')
                    print("volume is " + str(volume))
                    print("Lifetime is " + str(bot.order_lifetime))

                if check == 'check':
                    cprint('\n' 'This order is going to buy ' + str(volume/dec) + ' @ ' + str(price) + '\n', 'magenta' )
                    cprint('Do you want to check each order before buying type: check', 'red')
                    cprint('Do you want to just autobuy the rest of the orders: auto', 'green')

                    check = input('')

                if check == 'check' or check == 'auto':

                    my_address.buy(assetPair=pair, amount=volume, price=price, matcherFee=bot.order_fee,
                                                maxLifetime=bot.order_lifetime)

                    bot.log("Post Buy order with price: {0}, amount:{1}".format(price, volume))

                    myOrders = my_address.getOrderHistory(assetPair=pair)

                    pprint.pprint(myOrders[0])

                    idOrder = str(myOrders[0]['id'])

                    lines[row][csvIdCol] = idOrder
                    cprint(lines[row][csvIdCol], 'green')
                    print('')

                    row = row + 1

                    # throw error in idOrder Column if id isn't new (only works for first dup, need better solution)

                    if previousId == idOrder:

                        cprint("Error writing this order", 'magenta')
                        cprint("What next? retry, skip or exit?", 'magenta')
                        whatNext = input('')

                        if whatNext == 'retry':
                            row = row + 1
                        if whatNext == 'skip':
                            row = row
                        if whatNext == 'exit':
                            row = 0

                    previousId = idOrder

                    with open(pairCSV, 'w') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerows(lines)


    if text == 'retrace':


        cprint('\n', 'blue')

        print("Account: " + accountName + ', Pair: ' + pairName)
        print('')
        cprint('a. Check each Retrace before placing a new order', 'red')
        cprint('b. Retrace automatically', 'green')
        switch = input('')

        if switch == 'a' or switch == 'A':
            check = 'check'
        if switch == 'b' or switch == 'B':
            check = 'auto'


        while __name__ == "__main__":

            # reload csv to lines

            with open(pairCSV) as matrixRT:
                rRT = csv.reader(matrixRT)
                lines = list(rRT)

            # set CSV cells

            # lowSellRow csv value location
            lowSellCsvRow = 0
            lowSellCsvCol = 10
            lowSellRow = int(lines[lowSellCsvRow][lowSellCsvCol])

            # hiBuyRow csv value location
            hiBuyCsvRow = 1
            hiBuyCsvCol = 10
            hiBuyRow = int(lines[hiBuyCsvRow][hiBuyCsvCol])

            # Price Column
            priceCol = 1

            # ID Column
            csvIdCol = 4

            # reload lowSellId/hiBuyId and lowSellPrice/hiBuyPrice

            lowSellId = lines[lowSellRow][csvIdCol]

            lowSellPrice = float(lines[lowSellRow][priceCol]) * dec

            hiBuyId = lines[hiBuyRow][csvIdCol]

            hiBuyPrice = float(lines[hiBuyRow][priceCol]) * dec

            # load order book

            order_book = pair.orderbook()

            # load Order History

            myOrders = my_address.getOrderHistory(assetPair=pair)
            #pprint.pprint(myOrders)

            cprint('\n' + 'waveTracer v0.01a', 'cyan')
            cprint('Account: ' + accountName + ', Pair is: ' + pairName, 'white')
            print('')

            # Print current market low ask and high bid

            print('\n' + "Lowest current market ask is " + str(order_book['asks'][00]['price']/dec) + ' Amount: '
                                    + str(order_book['asks'][00]['amount']/dec))
            cprint("Your Last Sell Id is " + lowSellId, 'red')

            for row in myOrders:
                if str(row['id']) == lowSellId:
                    lowSellPrice = row['price']

            cprint("Selling for the very reasonable price of " + str(lowSellPrice/dec), 'red')

            # check the status of the lowSellId to see if it's filled

            lowSellStatus = pw.Order(orderId=lowSellId, assetPair=pair, address=my_address).status()
            cprint(lowSellStatus, 'red')
            print('')

            # check the status of the hiBuyId to see if it's filled

            hiBuyStatus = pw.Order(orderId=hiBuyId, assetPair=pair, address=my_address).status()
            print("Highest current market buy is " + str(order_book['bids'][00]['price']/dec) + ' Amount: '
                  + (str(order_book['bids'][00]['amount']/dec)))
            cprint("Last Buy Id is " + hiBuyId, 'green')

            for row in myOrders:
                if str(row['id']) == hiBuyId:
                    hiBuyPrice = row['price']

            cprint("Buying for the very reasonable price of " + str(hiBuyPrice/dec) + '\n'
                   + hiBuyStatus, 'green')
            print('')

            # Is it time to reorder:

            # toggle to test with an 'Accepted' order
            #if lowSellStatus == 'Filled' or hiBuyStatus == 'Filled' or lowSellStatus == 'Accepted':
            if lowSellStatus == 'Filled' or hiBuyStatus == 'Filled':
                print('Time to retrace')

                # load orders by row

                for row in myOrders:
                    #print(row)

                    # loop through rows to find our 'Filled' highBuyId or lowSellId

                    if str(row['id']) == str(hiBuyId) or str(row['id']) == lowSellId:

                        if row['status'] == 'Filled':
                        # open csv matrix

                            with open(pairCSV) as f:
                                csv_f = csv.reader(f)

                                # loop through csv rows

                                for row2 in csv_f:

                                    # match csv orderId to myOrders 'id'

                                    if row2[csvIdCol] == row['id']:

                                        indexVal = int(row2[0])

                                        print("Row2 order info:")

                                        print(row2)

                                        print("row #" + str(indexVal) + " and id: " + str(row2[csvIdCol]))

                                        print("Old Price is " + str(row['price']))

                                        oldPrice = int(row['price'])
                                        oldVol = int(row['amount'])

                                        # to do: add fee to calc in waves not .9969
                                        #decFee = int(bot.order_fee)
                                        # oldFee = oldPrice * decFee

                                        oldVal = oldPrice * oldVol/dec
                                        oldNet = oldVal * .9969

                                        if row['type'] == 'sell' and row['status'] == 'Filled':
                                            newPrice = float(lines[indexVal+reTrace][priceCol])

                                            fltVol = round(oldNet / newPrice, 8)
                                            newVol = int(fltVol)

                                            newPrice = int(float(newPrice) * dec) / dec
                                            print("New Buy Price is " + str(newPrice))
                                            # newPrice = newDecPrice
                                            # newPrice = int(float(row2[1])*100)/100

                                            print("New Volume is " + str(newVol))

                                            if check == 'check':
                                                cprint('\n' 'This order is going to buy ' + str(newVol) + ' for '
                                                       + str(newPrice) + '\n', 'magenta')
                                                cprint('Do you want to check each order before buying: check',
                                                       'red')
                                                cprint('Do you want to just autobuy the rest of the orders: auto',
                                                       'green')

                                                check = input('')

                                            if check == 'check' or check == 'auto':

                                                my_address.buy(assetPair=pair, amount=newVol, price=newPrice,
                                                               matcherFee=bot.order_fee,
                                                               maxLifetime=bot.order_lifetime)

                                                bot.log("Post Buy order with price: {0}, amount:{1}".format(newPrice,
                                                                                                            newVol))

                                        if row['type'] == 'buy' and row['status'] == 'Filled':
                                            newDecPrice = lines[indexVal-reTrace][1]
                                            print("New Sell Price is " + str(newDecPrice))
                                            newPrice = int(float(newDecPrice)*dec)/dec

                                            newVol = row['amount']


                                            if check == 'check':
                                                cprint('\n' 'This order is going to sell ' + str(newVol) + ' for ' + str(
                                                    newPrice) + '\n', 'magenta')
                                                cprint('Do you want to check each order before selling: check', 'red')
                                                cprint('Do you want to just autosell the rest of the orders: auto', 'green')

                                                check = input('')

                                            if check == 'check' or check == 'auto':

                                                my_address.sell(assetPair=pair, amount=newVol, price=newPrice,
                                                               matcherFee=bot.order_fee,
                                                               maxLifetime=bot.order_lifetime)

                                                bot.log("Post Sell order with price: {0}, amount:{1}".format(newPrice, newVol))

                                        myOrders = my_address.getOrderHistory(assetPair=pair)

                                        pprint.pprint(myOrders[0])

                                        idOrder = str(myOrders[0]['id'])
                                        idType = str(myOrders[0]['type'])

                                        # set new sell order in orderId column

                                        if idType == 'sell' and row['status'] == 'Filled':

                                            # Store new sell id in orderId column

                                            newSellIdRow = indexVal - reTrace

                                            lines[newSellIdRow][csvIdCol] = idOrder
                                            print("New Lowest Sell Order:")
                                            print(lines[newSellIdRow][csvIdCol])
                                            print('')


                                            # erase old buy orderId near market id

                                            eraseOldIdRow = indexVal

                                            lines[eraseOldIdRow][csvIdCol] = "market"
                                            print("Orders Empty @")
                                            print(lines[eraseOldIdRow][csvIdCol])
                                            print('')


                                            # Store new lowSellIdRow in lowSellCsvRow, lowSellCsvCol

                                            lines[lowSellCsvRow][lowSellCsvCol] = newSellIdRow
                                            print("Current Lowest Sell Order stored in lowSellId:")
                                            print(lines[lowSellCsvRow][lowSellCsvCol])
                                            print(newSellIdRow)
                                            print('these two should match')
                                            print('')


                                            # store new hiBuyId in last

                                            newBuyIdRow = indexVal + 1

                                            lines[hiBuyCsvRow][hiBuyCsvCol] = newBuyIdRow
                                            print("Current highest Buy Order stored in hiBuyId:")
                                            print(lines[hiBuyCsvRow][hiBuyCsvCol])
                                            print(newBuyIdRow)
                                            print('these two should match')
                                            print('')

                                            # set last market sell id for lower right box of matrix file in buy col


                                        if idType == 'buy' and row['status'] == 'Filled':

                                            # Store new hiBuyOrder id in orderId column

                                            newBuyIdRow = indexVal + reTrace

                                            lines[newBuyIdRow][csvIdCol] = idOrder
                                            print("New Highest Buy Order:")
                                            print(lines[newBuyIdRow][csvIdCol])
                                            print('')

                                            # erase old sell orderId near market id

                                            eraseOldIdRow = indexVal

                                            lines[eraseOldIdRow][csvIdCol] = "market"
                                            print("Orders Empty @")
                                            print(lines[eraseOldIdRow][csvIdCol])
                                            print('')

                                            # Store new hiBuyIdRow in hiBuyCSV Cell

                                            lines[hiBuyCsvRow][hiBuyCsvCol] = newBuyIdRow
                                            print("Current Lowest Buy Order stored in lowSellId:")
                                            print(lines[hiBuyCsvRow][hiBuyCsvCol])
                                            print(newBuyIdRow)
                                            print('these two should match')
                                            print('')

                                            # store new lowSellId in lowSellIdRow Cell

                                            newSellIdRow = indexVal - 1

                                            lines[lowSellCsvRow][lowSellCsvCol] = newSellIdRow
                                            print(newSellIdRow)
                                            print(lines[lowSellCsvRow][lowSellCsvCol])
                                            print('these two should match')
                                            print('')

                                            # set last market sell id for lower right box of matrix file in buy col

                                        # f = open(pairCSV, 'w')
                                        # f.write(lines)
                                        # f.close()

                                        with open(pairCSV, 'w') as outfile:
                                            writer = csv.writer(outfile)
                                            writer.writerows(lines)

                                        print('')

            cprint("Well nothing left to do for now, guess I'll take a nap for 100 ticks starting @ %s" % time.ctime(),
                   'cyan')
            #cprint("Current Lowest Market ask for VST/Waves is " + str(order_book['asks'][00]['price']))
            #cprint("Current Highest Market bid for VST/Waves is " + str(order_book['bids'][00]['price']))

            time.sleep(10)
            cprint('zzz', 'blue')
            time.sleep(10)
            cprint('   zzz', 'blue')
            time.sleep(10)
            cprint('      zzz', 'blue')
            time.sleep(10)
            cprint('         zzz', 'blue')
            time.sleep(10)
            cprint('            zzz', 'blue')
            time.sleep(10)
            cprint('               zzz', 'blue')
            time.sleep(10)
            cprint('                  zzz', 'blue')
            time.sleep(10)
            cprint('                     zzz', 'blue')
            time.sleep(10)
            cprint('                        zzz', 'blue')
            time.sleep(10)
            cprint('                           zzz', 'blue')

            cprint("I'm up, what'd I miss? Let me check:", 'magenta')
            time.sleep(3)


while __name__ == "__main__":
    main()

    print('end' '\n')