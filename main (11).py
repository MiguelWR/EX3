#Exercício 3

def T(n):
  if n == 2:
      return True
  elif n < 2:
      return False
  elif n % 2 == 0:
      return T(n // 2)
  else:
      return T(n - 3) and T((n - 3) // 2)

print(T(6))
print(T(7))
print(T(19))
print(T(12))