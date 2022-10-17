import web3
from web3.contract import Contract
from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from fund.models import Asset
from utils.constants.addresses import addresses
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider
import time
w3 = get_provider()

multicall = Multicall(w3, "fuji")
multicall_write = MulticallWrite(w3, "fuji")
targets = list(Asset.objects.all())
approve_erc20_calls = []
pangolin_liquidity_get_pair_reserve_calls = []
pangolin_liquidity_management_calls = []
ftx_prices = []
pangolin_router = w3.eth.contract(addresses["pangolin"]["Router"], abi=PangolinRouter)
# get pair
# get balance
def approve(token: Contract, spender_address, wallet_address, private_key):
    spender = spender_address
    max_amount = w3.toWei(2**64 - 1, "ether")
    nonce = w3.eth.getTransactionCount(wallet_address)

    tx = token.functions.approve(spender, max_amount).buildTransaction(
        {"from": wallet_address, "nonce": nonce}
    )

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)


multicall_address = "0xcA11bde05977b3631167028862bE2a173976CA11"
for target in targets:
    target_asset = w3.eth.contract(address=target.address, abi=ERC20_ABI)
    approve(
        token=target_asset,
        wallet_address="0xA3579C4c2057b58244DBc7DF5411C79d5F63a8A7",
        spender_address=multicall_address,
        private_key="baa235a9bb3244ee5b34c251a7a1fe3a4a65ace8aa22e33a443152f81015f714",
    )
    time.sleep(10)
