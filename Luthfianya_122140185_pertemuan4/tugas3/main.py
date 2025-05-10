import math_operations

from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

sisi = 5
p, l = 10, 4
r = 7

print("=== PERHITUNGAN GEOMETRI ===")
print(f"Luas persegi (sisi={sisi}): {math_operations.luas_persegi(sisi)}")
print(f"Keliling persegi: {math_operations.keliling_persegi(sisi)}")
print(f"Luas persegi panjang ({p}x{l}): {math_operations.luas_persegi_panjang(p, l)}")
print(f"Keliling persegi panjang: {math_operations.keliling_persegi_panjang(p, l)}")
print(f"Luas lingkaran (r={r}): {math_operations.luas_lingkaran(r):.2f}")
print(f"Keliling lingkaran: {math_operations.keliling_lingkaran(r):.2f}")

c = 30
print("\n=== KONVERSI SUHU ===")
print(f"{c}°C ke Fahrenheit: {celsius_ke_fahrenheit(c)}°F")
print(f"{c}°C ke Kelvin: {celsius_ke_kelvin(c)} K")
