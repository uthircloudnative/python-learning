from electronics import Electronics
from cloths import Cloths

iphone = Electronics("iPhone", "$1000", "2 Years")
print(iphone)

iphone_display_info = iphone.display_info()
print(iphone_display_info)


tshirt = Cloths("Raymond", "$200", "L")

tshirt_display_inofo = tshirt.display_info()
print(tshirt_display_inofo)