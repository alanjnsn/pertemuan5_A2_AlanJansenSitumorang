banyak_data=int(input('masukkan banyak data: '))
data=0
data_nilai=[]
while data<banyak_data:
    nilai=int(input(f"masukkan nilai ke {data}: "))
    data_nilai.insert(data,nilai)
    data+=1

i=0
total=0
panjang_data=len(data_nilai)
while i < panjang_data:
    total+=data_nilai[i]
    i+=1




print(total/panjang_data)