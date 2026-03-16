from solcx import compile_standard, install_solc
import json
import os

# ------------------- INSTALL SOLIDITY COMPILER -------------------
install_solc("0.8.17")  # match version of your contract

# ------------------- LOAD SOLIDITY CONTRACT -------------------
CONTRACT_FILE = "../blockchain/health_records.sol"  # path from backend folder

with open(CONTRACT_FILE, "r") as f:
    contract_source = f.read()

# ------------------- COMPILE CONTRACT -------------------
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"health_records.sol": {"content": contract_source}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.17",
)

# ------------------- SAVE ABI & BYTECODE -------------------
build_path = "./build"
os.makedirs(build_path, exist_ok=True)

# Full contract name
contract_name = "HealthRecord"

# ABI
abi_path = os.path.join(build_path, "health_record_abi.json")
with open(abi_path, "w") as f:
    json.dump(compiled_sol["contracts"]["health_records.sol"][contract_name]["abi"], f, indent=4)
print(f"✅ ABI saved at {abi_path}")

# Bytecode
bytecode_path = os.path.join(build_path, "health_record_bytecode.json")
with open(bytecode_path, "w") as f:
    json.dump(compiled_sol["contracts"]["health_records.sol"][contract_name]["evm"]["bytecode"]["object"], f)
print(f"✅ Bytecode saved at {bytecode_path}")
