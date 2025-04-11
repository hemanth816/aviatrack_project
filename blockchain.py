import json
from datetime import datetime
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        if not self.chain:  # Create only if chain is empty
            genesis_block = {"index": 0, "data": "Genesis Block"}
            self.chain.append(genesis_block)

    def add_block(self, data):
        block = {
            "index": len(self.chain),
            "data": data
        }
        self.chain.append(block)

    def save_chain(self, filename="blockchain_ledger.json"):
        with open(filename, "w") as f:
            json.dump(self.chain, f, indent=4)

    def load_chain(self, filename="blockchain_ledger.json"):
        try:
            with open(filename, "r") as f:
                self.chain = json.load(f)
        except FileNotFoundError:
            self.create_genesis_block()


BLOCKCHAIN_FILE = 'blockchain_ledger.json'

def write_to_blockchain(entry):
    """
    Simulate storing a log entry in blockchain.
    """
    entry['timestamp'] = datetime.now().isoformat()
    try:
        with open(BLOCKCHAIN_FILE, 'r') as f:
            ledger = json.load(f)
    except FileNotFoundError:
        ledger = []

    ledger.append(entry)

    with open(BLOCKCHAIN_FILE, 'w') as f:
        json.dump(ledger, f, indent=2)

    print("✔️ Entry logged to simulated blockchain.")
