have_length = False
up_case = False
low_case = False
low_num = False
no_of_strong_characteristics = 0
strong_characteristics = 3 # you left out this statement


  
have_length_check = input("Is password at least 6 characters? (yes or no):")
if have_length_check == "yes":
  have_length = True
  no_of_strong_characteristics += 1
  
  
upper_case_check = input("Does the password contain uppercase letters? (yes or no):")
if upper_case_check == "yes":
  have_length = True
  no_of_strong_characteristics += 1

lower_case_check = input("Does the password contain lowercase letters? (yes or no):")
if lower_case_check == 'yes':
  low_case = True
  no_of_strong_characteristics += 1
      
    
have_num_check = input("Does the password contain numbers? (yes or no):")
if have_num_check == "yes":
  low_num = True
  no_of_strong_characteristics += 1
  
  
if strong_characteristics > 2:
  print("This is a suitable password:") # Prints when user input does meet the requirements.

while strong_characteristics < 3:
  print("This is not a suitable password")  # Prints when user input does not meet the requirements.
  

    
    
