Pass = { 'H':'P', 'Os':'F', 'C':'B'}
while True:
   print('Enter a Key: ')
   key = input()
   if key == '':
      break
   if key in Pass:
      print('welcome')
   else:
      print('not granted')

