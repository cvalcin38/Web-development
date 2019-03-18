Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
>>> print (movies [1])
The Life of Brian
>>> movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]
>>> print (movies)
['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]
>>> fav_movies = ["The Holy Grail", "The Life of Brian"]
>>> print (fav_movies[1])
The Life of Brian
>>> print (fav_movies[0])
The Holy Grail
>>> for each_flick in fav_movies:
	print(each_flick)

	
The Holy Grail
The Life of Brian
>>> movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	      ["Graham Chapman", ["Michael Palin", "John Cleese",
				  "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
>>> print (movies)
['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
>>> for each_item in movies:
	print (each_item)

	
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> names = ['Michael', Terry']
	     
SyntaxError: EOL while scanning string literal
>>> names = ['Michael', 'Terry']
	     
>>> isinstance(names, list)
	     
True
>>> num_names = len(names)
	     
>>> isinstance(num_names, list)
	     
False
>>> for each_item in movies:
	     if isinstance(each_item, list):
	         for nested_item in each_item:
	                print(nested_item)
	     else:
	         print(each_item)

	     
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
>>> for each_item in movies:
	     print(each_item)

	     
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> for each_item in movies:
	     if isinstance(each_item, list):
	         for nested_item in each_item:
		     if isinstance(nested_item, list):
	     
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for each_item in movies:
	     if isinstance(each_item, list):
	        for nested_item in each_item:
	            if isinstance (nested_item, list):
	                for deeper_item in nested_item:
	                    print(deeper_item)
	     else:
	        print(each_item)

	     
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>> for each_item in movies:
	     if isinstance(each_item, list):
	         for nested_item in each_item:
	             if isinstance(nested_item, list):
	                 for deeper_item in nested_item:
	                     print(deeper_item)
	             else:
	                 print(nested_item)
	     else:
	         print(each_item)

	     
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>> def print_lol(the_list):
	     for each_item in the_list
	     
SyntaxError: invalid syntax
>>> def print_lol(the_list):
	     for each_item in the_list:
	         if isinstance(each_item, list):
	            print_lol(each_item)
	         else:
	            print(each_item)

	     
>>> print_lol(movies)
	     
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>>def print_lol(the_list):
             for each_item in the_list:
                 if isinstance(each_item, list):
                      print_lol(each_item)
             else:
                 print(each_item)


             




        


             
	     
