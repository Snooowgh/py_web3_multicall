# from kw3 import KWeb3
import json

from web3 import Web3

from web3_multicall import Multicall

http_rpc = "https://eth-mainnet.g.alchemy.com/v2/YourKey"
w3 = Web3(Web3.HTTPProvider(http_rpc))
usdt = w3.eth.contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                       abi=json.loads("""[{"inputs":[{"internalType":"address","name":"_l2Bridge","type":"address"},{"internalType":"address","name":"_l1Token","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_account","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_account","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"l1Token","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l2Bridge","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"_interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]"""))

print(usdt.functions.name().call())
multicall = Multicall(w3.eth) # address is not needed, unless you are on an unsupported  chain (check 'web3_multicall/models/enums/network.py')
multicall_result = multicall.aggregate([
    usdt.functions.name(),
    usdt.functions.symbol(),
    usdt.functions.decimals(),
    usdt.functions.totalSupply(),
    usdt.functions.balanceOf('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
])

multicall_result.jsonprint()
# Prints
# 
# {
#     "block_number": 7714239,
#     "results": [
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "name",
#             "inputs": [],
#             "results": [
#                 "BUSD Token"
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "symbol",
#             "inputs": [],
#             "results": [
#                 "BUSD"
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "decimals",
#             "inputs": [],
#             "results": [
#                 18
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "totalSupply",
#             "inputs": [],
#             "results": [
#                 4200999999996203280118545633
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "balanceOf",
#             "inputs": [
#                 {
#                     "name": "account",
#                     "value": "YOUR_ADDRESS",
#                     "solidity_type": "address"
#                 }
#             ],
#             "results": [
#                 0
#             ]
#         }
#     ]
# }