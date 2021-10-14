n = input("Введите число:")
try:
   n = abs(int(n))
except ValueError:
   print("Ошибка")
   exit()
mult = 1
while n > 0:
   digit = n % 10 
   if digit % 2 != 0:
         mult = mult * digit
   n = n // 10
print("Произведение цифр:", mult)