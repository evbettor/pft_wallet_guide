# submit_handshake.py
from xrpl.clients import JsonRpcClient
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment

NODE_ADDRESS = "r4yc85M1hwsegVGZ1pawpZPwj65SVs8PzD"

def send_handshake(wallet_address, secret):
    client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
    wallet = Wallet(seed=secret)
    
    payment_tx = Payment(
        account=wallet_address,
        amount="1",
        destination=NODE_ADDRESS,
        memos=[{"Memo": {"MemoData": "HANDSHAKE"}}],
    )
    
    signed_tx = safe_sign_and_autofill_transaction(payment_tx, wallet, client)
    response = send_reliable_submission(signed_tx, client)
    print(f"Handshake submitted: {response['result']['hash']}")

if __name__ == "__main__":
    # Replace with actual wallet details
    send_handshake("rYourWalletAddress", "sYourSecret")
