import requests
import json
import base64
import hmac
import hashlib
import time


class API(object):
	""" Bitfinex cryptocurrency exchange API """
	def __init__(self, key='', secret=''):
		self.PROTOCOL = "https"
		self.HOST = "api.bitfinex.com"
		self.VERSION = "v1"
		self.URL = self.PROTOCOL + "://" + self.HOST + "/" + self.VERSION
		self.KEY = key
		self.SECRET = secret

	""" Load API key from file """
	def loadKey(self, path):
		with open(path) as secrets_file:
			secrets = json.load(secrets_file)
			self.KEY = secrets['key'] 
			self.SECRET = secrets['secret']

	""" Generate noce string in milliseconds for auth """
	def nonce(self):
		return str(time.time() * 1000000)

	""" Sign the payload for private requests """
	def sign_payload(self, payload):
		j = json.dumps(payload)
		data = base64.standard_b64encode(j.encode('utf8'))
		h = hmac.new(self.SECRET.encode('utf8'), data, hashlib.sha384)
		signature = h.hexdigest()
		return {"X-BFX-APIKEY": self.KEY, "X-BFX-SIGNATURE": signature, "X-BFX-PAYLOAD": data}


	'''
		PUBLIC REQUESTS
	'''
	def ticker(self, pair):
		url = self.URL + "/pubticker/"+pair
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def stats(self, pair):
		url = self.URL + "/stats/"+pair
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def lendbook(self, currency):
		url = self.URL + "/lendbook/"+currency
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def orderbook(self, pair):
		url = self.URL + "/book/"+pair
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def trades(self, pair):
		url = self.URL + "/trades/"+pair
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def lends(self, currency):
		url = self.URL + "/lends/"+currency
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def symbols(self):
		url = self.URL + "/symbols/"
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result

	def symbolsDetails(self):
		url = self.URL + "/symbols_details/"
		r = requests.get(url)
		result = json.loads((r.content.decode()))
		return result


	'''
		PRIVATE REQUESTS
	'''
	def accountInfo(self):
		payload = {"request": "/"+self.VERSION+"/account_infos", "nonce": self.nonce()}
		signed_payload = self.sign_payload(payload)
		r = requests.post(self.URL + "/account_infos", headers=signed_payload, verify=True)
		json_resp = r.json()
		return json_resp

	def accountFees(self):
		payload = {"request": "/"+self.VERSION+"/account_fees", "nonce": self.nonce()}
		signed_payload = self.sign_payload(payload)
		r = requests.post(self.URL + "/account_fees", headers=signed_payload, verify=True)
		json_resp = r.json()
		return json_resp

	def summary(self):
		payload = {"request": "/"+self.VERSION+"/summary", "nonce": self.nonce()}
		signed_payload = self.sign_payload(payload)
		r = requests.post(self.URL + "/summary", headers=signed_payload, verify=True)
		json_resp = r.json()
		return json_resp

	def balances(self):
		payload = {"request": "/"+self.VERSION+"/balances", "nonce": self.nonce()}
		signed_payload = self.sign_payload(payload)
		r = requests.post(self.URL + "/balances", headers=signed_payload, verify=True)
		json_resp = r.json()
		return json_resp
