// Import web3 library
const Web3 = require('web3');
const fs = require('fs');

// Initialize Web3 with Metamask provider
const web3 = new Web3(window.ethereum);

// Load contract ABI from JSON file
const abi = JSON.parse(fs.readFileSync('FastFlexContract.json', 'utf8'));

// Address of the deployed smart contract on Sepolia testnet
const contractAddress = '0x5ac211369cA3b4A32142dB56d78A0fba81E9BF84'; // Replace with your contract address on Sepolia testnet

// Create an instance of the contract
const contract = new web3.eth.Contract(abi, contractAddress);

// Function to store CSV data to the smart contract
async function storeCsvData(csvData) {
    try {
        // Store CSV data on the blockchain
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        const result = await contract.methods.storeCsv(csvData).send({ from: accounts[0] });
        console.log('Transaction hash:', result.transactionHash);
        return result.transactionHash;
    } catch (error) {
        console.error('Error storing CSV data:', error);
        throw error;
    }
}

// Export function to be called from Python
module.exports = { storeCsvData };
