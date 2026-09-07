seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = (current_stock) and (seasonal < high_stock_threshold)
discount_eligible = not(selling_well) or (on_sale)
make_discount = (overstock_risk >= discount_eligible)
print("Should the item be discounted?",make_discount)
