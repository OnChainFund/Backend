a = [
    "AAPL/USD",
    "AAVE/USD",
    "AVAX/USD",
    "BTC/USD",
    "ETH/USD",
    "GLD/USD",
    "LINK/USD",
    "TSLA/USD",
    "TWTR/USD",
    "USDT/USD",
]
b = [
    "AAPL",
    "AAVE",
    "AVAX",
    "BTC",
    "ETH",
    "GLD",
    "LINK ",
    "TSLA",
    "TWTR",
    "USDT",
]
c = [
    "0x930b24b4b578409153501429cc256FBbDAB6e893",
    "0x9Bb8F40d53DA2796F34d85f5bf27C475Df03E70C",
    "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
    "0xbC9052c594261Acc1a26271567bDb72A8A1Acac9",
    "0x96058B65CE7d0DBa4B85DAf49E06663B97442137",
    "0x7D157E24f3D6FB7Bd8B3008A76DFBCde267daCa8",
    "0x5B3a2CAED90515e36830167529AFeDea75419b7a",
    "0x22044e0e4E2D774f34227FC8a1BF804Ff9Fc9A35",
    "0x181Bf62B82AFafa87630C819482ABbA819e49601",
    "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
]
d = [
    "AAPLDOWN",
    "AAVEDOWN",
    "AVAXDOWN",
    "BTCDOWN",
    "ETHDOWN",
    "GLDDOWN",
    "LINKDOWN",
    "TSLADOWN",
    "TWTRDOWN",
    "USDTDOWN",
]
e = [
    "0xC7c69FFC3561fb3284F4d6D25d8b69D8CB3b59e9",
    "0x0690b3F6f8271b000f800F051f82B65F41D29C5E",
    "0x33506d382684db988D9021A80dBEeEF46a5ABC3A",
    "0xE85e1219691aF541F064E111161174C1F7Db2e84",
    "0xB7B8E01a9F5dFe405c37b667E8F81a66D4f629EA",
    "0xFb1438372dB41dAFFcf4019e80eAE2D673B8c3b7",
    "0xA964EeaE6e77B1d01432942bc31186cB56eA5804",
    "0xa19baf63747637D0233702bA8F1eFcD6729db4DF",
    "0xe05F46AAfa9919f722bc83fbD2Bb7B3Ac23E1Bc2",
    "0x7f5BE805EFdbc5b42A3cfBC41B2961A0A9d9e3B2",
]
import pprint

asset = []
for i in range(0, len(a)):
    asset.append(
        {
            "ftx_pair_name": a[i],
            "positive": {"name": b[i], "address": c[i]},
            "negitive": {"name": d[i], "address": e[i]},
        }
    )
pprint.pprint(asset)