mahasiswa = [
    {"nama": "Andi", "nim": "A001", "uts": 75, "uas": 80, "tugas": 70},
    {"nama": "Budi", "nim": "A002", "uts": 60, "uas": 65, "tugas": 60},
    {"nama": "Citra", "nim": "A003", "uts": 85, "uas": 90, "tugas": 80},
    {"nama": "Dina", "nim": "A004", "uts": 50, "uas": 55, "tugas": 50},
    {"nama": "Eka",  "nim": "A005", "uts": 40, "uas": 45, "tugas": 40},
]

for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs["uts"]) + (0.4 * mhs["uas"]) + (0.3 * mhs["tugas"])
    mhs["nilai_akhir"] = round(nilai_akhir, 2)

    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    mhs["grade"] = grade

print(f"{'Nama':<10} {'NIM':<6} {'UTS':<4} {'UAS':<4} {'Tugas':<6} {'Akhir':<6} {'Grade'}")
print("-" * 50)
for mhs in mahasiswa:
    print(f"{mhs['nama']:<10} {mhs['nim']:<6} {mhs['uts']:<4} {mhs['uas']:<4} {mhs['tugas']:<6} {mhs['nilai_akhir']:<6} {mhs['grade']}")

tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{tertinggi['nama']} ({tertinggi['nim']}) - Nilai Akhir: {tertinggi['nilai_akhir']} - Grade: {tertinggi['grade']}")

print("\nMahasiswa dengan nilai terendah:")
print(f"{terendah['nama']} ({terendah['nim']}) - Nilai Akhir: {terendah['nilai_akhir']} - Grade: {terendah['grade']}")
