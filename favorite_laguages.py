favorite_languages = {
    'jen': ['python', 'ruby'], 
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
   print("\n" + name.title() + "'s favorite laguages are:")
   for language in languages:
      print("\t" + language.title())


      