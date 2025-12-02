matrex = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#إضافة صف
matrex.append ([10,11,12])

#إضافة عمود
for i,v in enumerate ([10,20,30]):
    matrex[i].append(v)
    
# تعديل عتصر
    matrex[1][1]= 50

# بحث عن عنصر 4 
x=7
for i in range (len(matrex)):
    for j in range(len(matrex[i])):
        if matrex [i][j]==x:
            print("fount at :", i,j)

# حذف عمود 5 
col = 2
for row in matrex:
    del row [col]
    
# طباعة النتيجة النهائية
for r in matrex:
    print(r)