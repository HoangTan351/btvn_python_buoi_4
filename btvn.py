# 1
def thaydoichucaidau():
    a = input("nhap: ")
    s= "$"
    for i in range(1,len(a)):
        if a[i] == a[0]:
            s+="$"
        else:
            s+=a[i]
    return s
print(f"chuoi: {thaydoichucaidau()}")

# 2
def xoabokitu():
    a = input("nhap chuoi: ")
    m = int(input("nhap thu tu muon xoa trong chuoi: "))
    s=  ""
    while m < 0:
        m= int(input("nhap lai: "))
    for i in range(len(a)):
        if i!=m:
            s+=a[i]
    return s
print(f"xuat chuoi: {xoabokitu()}")

# 3
def xoakitule(s):
    return s[::2]
s=input("Nhap chuoi: ")
print(xoakitule(s))

# 4
print("nhap chuoi: ",end="")
chuoi=str(input())
def dau_duoi(chuoi):
    print(chuoi[0:2]+chuoi[-2:])
    if len(chuoi)<2:
        print("chuoi rong")
dau_duoi(chuoi)

# 5
def sosanhkitu():
    chuoi = input("nhap chuoi: ")
    s=""
    for i in range(len(chuoi)):
        s+=chuoi[i] 
        chuoilon = max(chuoi)
        chuoibe = min(s)
    if chuoilon > chuoibe:
        print("ki tu lon nhat: ",chuoilon) 
        print("ki tu lon nhat: ",chuoibe)
sosanhkitu()

# 6
print("nhap chuoi: ",end="")
s=str(input())
def hoa(s):
    kq1=""
    for i in s:
        if i.islower():   
            kq1+=i.upper()
        else:
            kq1+=i.lower()
    return kq1
print(f"Hoa: {hoa(s)}")