def triangle(n) :
  bantu=0
  kosong=0
  for i in reversed(range(n)):
      for j in range(i+1):
          print('_', end='')
      for k in range(bantu+1):
          if k == 0:
              print('#', end='')
          else:
              print('_', end='')
      for l in range(bantu):
          if l == kosong:
              print('#', end='')
              kosong+=1
          else:
              print('_', end='')
      for j in range(i+1):
        print('_', end='')
      bantu+=1
      print()
  for i in range(n+1):
      print('# ', end='')
triangle(5)