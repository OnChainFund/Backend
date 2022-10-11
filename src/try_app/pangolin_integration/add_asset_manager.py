# pyright: strict

from web3.contract import Contract
from abi.ocf.VaultLib import VaultLib
from try_app.multicall_write import Multicall
from utils.utils import get_provider
from fund.models import Fund
from decouple import config  # type: ignore
from utils.constants.addresses import addresses

w3 = get_provider()
multicall = Multicall(w3, "fuji")
# fund = Fund.objects.first()
vault_proxy: Contract = w3.eth.contract(  # type: ignore
    "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C", abi=VaultLib  # type: ignore
)


txn = vault_proxy.functions.addAssetManagers(
    ["0xcA11bde05977b3631167028862bE2a173976CA11"]
).buildTransaction(
    {
        "chainId": 43113,
        "gas": 7900000,
        # "maxFeePerGas": w3.toWei("30", "gwei"),
        # "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
        "nonce": w3.eth.getTransactionCount(addresses["user_1"]),  # type: ignore
    }
)
signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))  # type: ignore
w3.eth.sendRawTransaction(signed_txn.rawTransaction)  # type: ignore
