from fund.models import Asset, Price, Fund

t2 = Fund.objects.all().filter(name="T2").first()
print(t2)
t2_price = Price.objects.all().filter(fund=t2)
print(t2_price)
t2_price.update(nav_per_share=15)