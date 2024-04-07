from flask import Flask, render_template, send_file
from web3 import Web3
from eth_account.messages import encode_defunct

app = Flask(__name__)

# Web3 provider
w3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/5e4qRq4bZrx8gOf5K6cDK8jJSIlFnzQK'))

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

@app.route('/')
def index():
    return render_template('retrieve.html')
import io

@app.route('/download', methods=['GET'])
def download():
    csv_data = contract.functions.getCSV().call()
    if csv_data:
        return send_file(
            io.BytesIO(csv_data.encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name='download.csv'
        )
    else:
        return "No CSV data available for download."

if __name__ == '__main__':
    app.run(debug=True)
