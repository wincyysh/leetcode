def gcd(x, y):
  while y != 0:
    print("x, y, x%y", x, y, x%y)
    (x, y) = (y, x % y)
  return x

if __name__ == '__main__':
  gcd(336, 360)