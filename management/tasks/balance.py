from utils.utils import get_provider
from utils.multicall.multicall import Multicall
from abi.others.ERC20 import ERC20 as ERC20_ABI
from fund.models import Asset

w3 = get_provider()

multicall = Multicall(w3, "fuji")
targets = list(Asset.objects.all())
balance_of_erc20_calls = []
for target in targets:
    target_asset = w3.eth.contract(address=target.address, abi=ERC20_ABI)
    balance_of_erc20_calls.append(
        multicall.create_call(
            target_asset,
            "balanceOf",
            ["0xA3579C4c2057b58244DBc7DF5411C79d5F63a8A7"],
        ),
    )
results = multicall.call(balance_of_erc20_calls)
print(results)
for i in range(0, len(results[1])):
    print(targets[i].name + ": " + str(int(results[1][i].hex(), 16) / 10**6))
print(len(results))
