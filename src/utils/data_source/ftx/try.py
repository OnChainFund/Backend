from client import FtxClient

ftx_client = FtxClient()
data = ftx_client.get_price("ETH/USD")
print(data)
