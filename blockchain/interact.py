from web3 import Web3
import json

# 👇 Connect to local Ethereum blockchain (Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
print("Connected:", w3.isConnected())

# 👇 Replace with your Ganache account private key
private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.accounts[0]

# 👇 Compile & deploy the contract (or use pre-deployed address)
with open("health_record_abi.json", "r") as f:
    abi = json.load(f)

contract_address = "YOUR_CONTRACT_ADDRESS"
contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to add patient
def add_patient(name, age, heart_rate, glucose, risk_status):
    txn = contract.functions.addPatient(
        name, age, heart_rate, glucose, risk_status
    ).buildTransaction({
        "from": account,
        "nonce": w3.eth.get_transaction_count(account),
        "gas": 3000000,
        "gasPrice": w3.toWei('20', 'gwei')
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Patient added! Transaction hash: {tx_hash.hex()}")

# Function to get patient by ID
def get_patient(patient_id):
    patient = contract.functions.getPatient(patient_id).call()
    print("Patient Info:", patient)

# Example usage
if __name__ == "__main__":
    # Add a patient
    add_patient("Vaishnavi Devi", 25, 85, 120, "low risk")

    # Retrieve patient
    get_patient(1)
