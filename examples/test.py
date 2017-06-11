import bitfinex

api = bitfinex.API()

'''
	PUBLIC REQUESTS
'''

# Request ticker
res = api.ticker("btcusd")
print(str(res))

'''
# Request stats
res = api.stats("btcusd")
print(str(res))

# Request lendbook
res = api.lendbook("btc")
print(str(res))

# Request orderbook
res = api.orderbook("btcusd")
print(str(res))

# Request trades
res = api.trades("btcusd")
print(str(res))

# Request lends
res = api.lends("btc")
print(str(res))

# Request symbols
res = api.symbols()
print(str(res))

# Request symbolsDetails
res = api.symbolsDetails()
print(str(res))
'''



'''
	PRIVATE REQUESTS
'''

# All private data requests need a valid key loaded
api.loadKey("keyfile.key")

# Request balances
res = api.balances()
print(str(res))

'''
# Request account info
res = api.accountInfo()
print(str(res))

# Request account fees
res = api.accountFees()
print(str(res))

# Request summary
res = api.summary()
print(str(res))
'''
