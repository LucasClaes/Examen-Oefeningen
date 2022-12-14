
lengte_a = int(input("Geef de lengte van doos a: "))
breedte_a = int(input("Geef de breedte van doos a: "))
hoogte_a = int(input("Geef de hoogte van doos a: "))

lengte_b = int(input("Geef de lengte van doos b: "))
breedte_b = int(input("Geef de breedte van doos b: "))
hoogte_b = int(input("Geef de hoogte van doos b: "))

volume_a = lengte_a * breedte_a * hoogte_a
volume_b = lengte_b * breedte_b * hoogte_b

print(f"De inhoud van doos A is,{volume_a}")
print(f"De inhoud van doos B is,{volume_b}")

if volume_a > volume_b:
    print("De inhoud van doos A is groter")
else:
    print("De inhoud van doos B is groter")
