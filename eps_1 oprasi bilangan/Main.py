# operasi arritmatika

a = 10
b = 5
 
# operasi penjumlahan 
hasil = a + b
print(a, '+',b,'=',hasil)

# operasi pengurangan 
hasil = a - b
print(a, '-',b,'=',hasil)

# operasi perkalian 
hasil = a * b
print(a, '*',b,'=',hasil)

# operasi pembagian 
hasil = a / b
print(a, '/',b,'=',hasil)

# operasi pangkat(eksponen) 
hasil = a ** b
print(a, '**',b,'=',hasil)

# operasi modulus(sisa pembagian) 
hasil = a % b
print(a, '%',b,'=',hasil)

# operasi floor division 
hasil = a // b
print(a, '//',b,'=',hasil)

# operasi prioritas
x =3 
y =2
z = 6

hasil =  x ** y * y + z - y // z * z
print(x,'**',y,'*','+',z,'-',y,'//',z,'*',z,'=',hasil) 

hasil =  x ** y * (y + z) - y // z * z
print(x,'**',y,'*','+',z,'-',y,'//',z,'*',z,'=',hasil) 

# prioritas 
''''
    1. ()
    2. eksponen **
    3. perkalian dan pembagian */
    4. pertambahan dan pengurangan +-
'''