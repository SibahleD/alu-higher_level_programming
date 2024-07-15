


  my_string = "Hello"
  print(id(my_string))     
  # Finding the Unique ID of the my_string
  139900022764400
  print(type(my_string))   
  # Finding the type of my_string
  <class 'str'>


Mutable objects


  my_list = [1, 2, 3]
  my_list.append(4)            
  # Modifies the list
  print(my_list)
  [1, 2, 3, 4]

  my_dict = {'a': 1, 'b': 2}
  my_dict['c'] = 3             
  # Adds a new key-value pair
  print(my_dict)
  {'a': 1, 'b': 2, 'c': 3}


immutable objects

  my_string = "I can't be edited"
  print("Original string: ", my_string) 
  "   Original String: I can't be edited   "

  # Attempts to add a value to the string
  new_string = my_string + ", I can only be duplicated"
  print("New string: ", new_string)
  "New string: I can't be edited, I can only be duplicated"





