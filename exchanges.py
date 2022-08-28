import ccxt

exchanges = {
    'gateio': ccxt.gate(),
    'hitbtc': ccxt.hitbtc(),
    'bitfinex': ccxt.bitfinex(),
    'poloniex': ccxt.poloniex(),
    'liquid': ccxt.liquid(),
    'coinbase': ccxt.coinbase(),
    # 'zb': ccxt.zb(), we don't have it in fee site
    # 'bigone': ccxt.bitfinex(),
    # 'bitstamp': ccxt.bitstamp(), don't apper in ouuputlist
    # 'Bitmex': ccxt.bitfinex(),
    # 'Gemini': ccxt.bitfinex(),
    'huobi': ccxt.huobi(),
    'okex': ccxt.okx(),
    # 'upbit global': ccxt.bitfinex(),
    # 'CeX.io': ccxt.bitfinex(),
    # 'kraken': ccxt.kraken(), don't apper in ouuputlist
    'binance': ccxt.binance(),
    'kucoin': ccxt.kucoin({
        'apiKey': '62ef70b36ad523000118beb6',
        'secret': '97609ac1-f4d5-4233-aff8-bd96a3cea580',
        'password': '8kngNKqhoRC5'
    }),
}
