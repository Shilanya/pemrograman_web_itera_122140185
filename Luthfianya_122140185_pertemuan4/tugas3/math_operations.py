PI = 3.14159 

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(p, l):
    return p * l

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_lingkaran(r):
    return PI * r * r

def keliling_lingkaran(r):
    return 2 * PI * r

# Fungsi konversi suhu
def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15
