banyak_data=int(input('banyak data yang diinginkan: '))

total=0
for data in range(banyak_data):
    nilai=int(input(f"masukkan data ke {data}: "))
    total+=nilai

print(f"rata-rata= {total/banyak_data}")

