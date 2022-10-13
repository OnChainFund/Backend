from decimal import Decimal
from web3.datastructures import AttributeDict
from utils.multicall.multicall import Call
from management.web3.multicall_custome import MulticallCustom as Multicall
from fund.models import Asset
from utils.utils import get_provider

w3 = get_provider()
# 取得所有 token
# 取得要計算 balance 的物件
def from_wei(value):
    return value / 1e18

def generate_multicall(call_list: list):
    multi = Multicall(call_list, _w3=w3)
    return multi

fund_vault_proxy_address = "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"

asset_data_list = list(Asset.objects.values_list("address", "name"))
test =[1,2,3]
multi = []
for asset_data in asset_data_list:
    # asset_address_list.append(asset_data[0])
    multi.append(
        Call(
            "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
            ["balanceOf(address)(uint256)", fund_vault_proxy_address],
            [[asset_data[1], from_wei]],
        )
    )
    # asset_name_list.append(asset_data[1])
data = generate_multicall(multi)

print(data())
