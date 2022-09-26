from decimal import Decimal
from web3.datastructures import AttributeDict
from multicall import Call
from management.web3.multicall_custome import MulticallCustom
from fund.models import Asset
from utils.utils import get_provider

w3 = get_provider()
# 取得所有 token
# 取得要計算 balance 的物件
def from_wei(value):
    return value / 1e18


def generate_multicall(call_list: list):
    multi = MulticallCustom(call_list, _w3=w3)
    return multi


def fetch_data():
    data = multi()
    data["eth_fee"] = get_fee(data["base"], data["eth_jug"])
    data["bat_fee"] = get_fee(data["base"], data["bat_jug"])
    data["sai_fee"] = get_fee(data["base"], data["sai_jug"])
    data["pot_fee"] = calc_fee(data["dsr"])
    data["savings_dai"] = data["savings_pie"] * data["pie_chi"]
    data["eth_price"] = data["eth_mat"]["mat"] * data["eth_ilk"]["spot"]
    data["bat_price"] = data["bat_mat"]["mat"] * data["bat_ilk"]["spot"]
    data["sys_locked"] = (
        data["eth_price"] * data["eth_locked"]
        + data["bat_price"] * data["bat_locked"]
        + data["sai_locked"]
    )
    data["sys_surplus"] = data["vow_dai"] - data["vow_sin"]
    data["sys_debt"] = data["vow_sin"] - data["sin"] - data["ash"]
    return data


def get_data():
    data = fetch_data()
    data = AttributeDict.recursive(data)
    print("The Fundamental Equation of Dai")
    print(
        f"{data.eth_ilk.Art * data.eth_ilk.rate:,.0f} + {data.bat_ilk.Art * data.bat_ilk.rate:,.0f} + {data.sai_ilk.Art:,.0f} + {data.vice:,.0f} = {data.debt:,.0f}"
    )
    print("(Dai from ETH + Dai from BAT + Dai from Sai + System Debt) = Total Dai")
    print()
    print(f"Total Dai: {data.debt:,.0f}")
    print(f"Total Sai: {data.sai_supply:,.0f}")
    print(f"Dai + Sai: {data.debt + data.sai_supply:,.0f}")
    print(f"Total Chai: {data.chai_supply:,.0f}")
    print()
    print(
        f"Dai from ETH: {data.eth_ilk.Art * data.eth_ilk.rate:,.0f} ({data.eth_ilk.Art * data.eth_ilk.rate / data.debt:.2%})"
    )
    print(
        f"Dai from BAT: {data.bat_ilk.Art * data.bat_ilk.rate:,.0f} ({data.bat_ilk.Art * data.bat_ilk.rate / data.debt:.2%})"
    )
    print(
        f"Dai from SAI: {data.sai_ilk.Art * data.sai_ilk.rate:,.0f} ({data.sai_ilk.Art * data.sai_ilk.rate / data.debt:.2%})"
    )
    print()
    print(f"ETH Locked: {data.eth_locked:,.0f}")  # eth_supply missing
    print(
        f"ETH Ceiling: {data.eth_ilk.line:,.0f} Dai ({data.eth_ilk.Art * data.eth_ilk.rate / data.eth_ilk.line:.2%} util.)"
    )
    print(f"ETH Stability Fee: {data.eth_fee:.2f}%")
    print()
    print(
        f"BAT Locked: {data.bat_locked:,.0f} ({data.bat_locked / data.bat_supply:.2%} supply)"
    )
    print(
        f"BAT Ceiling: {data.bat_ilk.line:,.0f} Dai ({data.bat_ilk.Art * data.bat_ilk.rate / data.bat_ilk.line:.2%} util.)"
    )
    print(f"BAT Stability Fee: {data.bat_fee:.2f}%")
    print()
    print(
        f"Dai (ERC20) Supply: {data.dai_supply:,.0f} ({data.dai_supply / data.debt:.2%})"
    )
    print(f"Dai in DSR: {data.savings_dai:,.0f} ({data.savings_dai / data.debt:.2%})")
    print(f"Pie in DSR: {data.savings_pie:,.0f}")
    print(f"Dai Savings Rate: {data.pot_fee:.2f}%")
    print()
    print(f"ETH Price: ${data.eth_price:,.2f}")
    print(f"BAT Price: ${data.bat_price:,.4f}")
    print(f"Collat. Ratio: {data.sys_locked / data.debt:,.2%}")
    print(f"Total Locked: ${data.sys_locked:,.0f}")
    print()
    print(f"System Surplus: {data.sys_surplus:,.0f} Dai")
    print(f"Surplus Buffer: {data.surplus_buffer:,.0f}")
    print()
    print(f"Debt available to heal: {data.sys_debt:,.0f} Dai")
    print(f"Debt Buffer: {data.debt_size:,.0f}")
    print()
    print(f"Vaults Opened: {data.cdps:,d}")
    print()
    print(f"ETH Vault Auctions: {data.eth_kicks:,d}")
    print(f"BAT Vault Auctions: {data.bat_kicks:,d}")
    print()
    print(f"MKR Supply: {data.mkr_supply:,.2f}")
    print(f"MKR in Burner: {data.gem_pit:,.2f}")
    print()
    print(f"Dai in Uniswap: {data.uniswap_dai:,.0f}")


fund_vault_proxy_address = "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"

asset_data_list = list(Asset.objects.values_list("address", "name"))

multi = []
for asset_data in asset_data_list:
    # asset_address_list.append(asset_data[0])
    multi.append(
        Call(
            asset_data[0],
            ["balanceOf(address)(uint256)", fund_vault_proxy_address],
            [[asset_data[1], from_wei]],
        )
    )
    # asset_name_list.append(asset_data[1])
data = generate_multicall(multi)

print(data())
