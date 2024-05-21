def mean(number):
  number = str(number)
  suma = 0
  for i in number:
    suma += int(i)
  return int(suma/len(number))

print(mean(42))
print(mean(12345))
print(mean(777))


