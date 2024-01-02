from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY'))

# Replace 'YOUR_CONTRACT_ADDRESS' and 'YOUR_ABI' with the actual values
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = 'YOUR_ABI'

# Create a contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Example read-only function call to get data from the contract
result = contract.functions.yourReadOnlyFunctionName().call()

print(result)
