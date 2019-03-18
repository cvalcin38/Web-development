movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["MIchael Palin", "John Cleese", "Terry Gilliam", "Erric Idle", "Terry Jones"]]]
type(movies)
def claudia():

  for each_items in movies:
    print(each_items)

  print(len(movies))

  for i, v in enumerate(movies):
    print(i,v)

  for each_items in movies:
    if isinstance(each_items, list):
      for nested_item in each_items:
        print(nested_item)
        

    else:
      print(each_items)

  claudia()


  




  
