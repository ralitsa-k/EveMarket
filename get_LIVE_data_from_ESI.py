from src.functions import ShipOrder

# provide system id, station id, item id
ship1 = ShipOrder('10000002','60003757','605')

regions_data = ship1.get_buy_sell()
print(regions_data)

