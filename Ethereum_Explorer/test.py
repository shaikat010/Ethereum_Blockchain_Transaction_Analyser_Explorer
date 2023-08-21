
from web3 import Web3


w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/3beb35814f274c01996224de0c825f95"))

input_text = "0xa7446e885f81e9153f000541bdee82c93167b9038b8a19c8a65176aa51012922"
transaction = w3.eth.get_transaction(input_text)  
transaction = str(transaction)
print(transaction)