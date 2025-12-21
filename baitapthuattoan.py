
def Bai2(a):
    s=0
    for i in a:
        s+=i
    return s/len(a)

def Bai3(a):
    S=0
    for i in a:
        if i%2==0:
            S+=1
    return S


def Bai4(a):
    Max=a[0]
    Min=a[0]
    for i in a:
        if i>Max:
            Max=i
        if i<Min:
            Min=i
    return Max, Min

def Bai5(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

def Bai6(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Bai6(n-1)
    
def Bai7(a,b):
    return -b/a
    
a=[int(x) for x in input("Nhập dãy số: ").split()]
n=int(input("Nhập số để tính giai thừa: "))
print("Bài 2: Trung bình cộng của dãy số là:",Bai2(a))
print("Bài 3: Số lượng số chẵn có trong dãy số là:",Bai3(a))
Max, Min = Bai4(a)
print("Bài 4: Giá trị lớn nhất và nhỏ nhất trong dãy số là:",Max, Min)
print("Bài 5: Dãy số sau khi sắp xếp là:",Bai5(a))
print("Bài 6: Giai thừa của",n,"là:",Bai6(n))
print("Bài 7: Nghiệm phương trình bậc nhất là:",Bai7(float(input("Nhập hệ số a: ")),float(input("Nhập hệ số b: "))))