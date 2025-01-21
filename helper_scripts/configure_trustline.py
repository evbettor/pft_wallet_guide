# configure_trustline.py
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.transactions import TrustSet
from xrpl.transaction import send_reliable_submission
from xrpl.utils import xrp_to_drops

PFT_ISSUER = "rnQUEEg8yyjrwk9FhyXpKavHyCRJM9BDMW"
PFT_CURRENCY = "PFT"

def configure_trustline(wallet_address, secret):
    client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
    wallet = Wallet(seed=secret)
    
    trust_set = TrustSet(
        account=wallet_address,
        limit_amount={"currency": PFT_CURRENCY, "value": "1000000", "issuer": PFT_ISSUER},
    )
    tx_response = send_reliable_submission(trust_set, client)
    print(f"Trustline configured: {tx_response}")

if __name__ == "__main__":
    # Replace with actual wallet details
    configure_trustline("rYourWalletAddress", "sYourSecret")
