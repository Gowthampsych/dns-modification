from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.messages import encode_defunct

# Web3 provider
w3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/5e4qRq4bZrx8gOf5K6cDK8jJSIlFnzQK'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Smart contract details
contract_address = '0x0b1080891Ef5e1a7ce0A4E604f4B11d115F161fE'
abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "data",
                "type": "string"
            }
        ],
        "name": "CSVUploaded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "csvData",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getCSV",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_csvData",
                "type": "string"
            }
        ],
        "name": "uploadCSV",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)

# MetaMask private key
private_key = '045d7b28919e131ca606797c1f66b1fc49bb7416711390135f7f15f91b0f5838'

# Set default account
w3.eth.default_account = w3.eth.account.from_key(private_key).address

# Function to sign transactions
def sign_transaction(txn):
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    return signed_txn.rawTransaction

def upload():
    file_path = 'fastflex_ips.csv'
    csv_data = None
    with open(file_path, 'r') as file:
        csv_data = file.read()

    if csv_data:
        nonce = w3.eth.get_transaction_count(w3.eth.default_account)
        txn_data = contract.functions.uploadCSV(csv_data).build_transaction({
            'chainId': 11155111,
            'gas': 2000000,
            'gasPrice': Web3.to_wei(1, 'gwei'),
            'nonce': nonce,
        })
        signed_txn = sign_transaction(txn_data)
        txn_hash = w3.eth.send_raw_transaction(signed_txn)
        print(txn_hash.hex())
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
        print(receipt)

if __name__ == '__main__':
    upload()
