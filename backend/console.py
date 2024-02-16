from api.src.clients import FMPClient

client = FMPClient()
top_peers = client.request_sector_peers()