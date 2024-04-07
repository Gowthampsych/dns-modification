from flask import Flask, render_template, request
from web3 import Web3, HTTPProvider
import json

app = Flask(__name__)

# Connect to Ethereum node
web3 = Web3(HTTPProvider('http://localhost:8545'))

# Load contract ABI from JSON file
with open('FastFlexContract.json', 'r') as f:
    abi = json.load(f)

# Address of the deployed smart contract
contract_address = '0x5ac211369cA3b4A32142dB56d78A0fba81E9BF84'  # Replace with your contract address

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and store CSV data
@app.route('/store_csv', methods=['POST'])
def store_csv():
    if request.method == 'POST':
        csv_data = request.form['csv_data']
        try:
            # Store CSV data on the blockchain
            accounts = web3.eth.accounts
            tx_hash = contract.functions.storeCsv(csv_data).transact({'from': accounts[0]})
            return 'CSV data stored successfully! Transaction hash: {}'.format(tx_hash.hex())
        except Exception as e:
            return 'Error storing CSV data: {}'.format(e)

if __name__ == '__main__':
    app.run(debug=True)
