#--------------------------------------------------------------------------------------------
#Description   : For-else loop
#Functionality : Else will be executed only when for loop exits normally without break statement.
#Syntax : 
#     for num in nums:
#       statements;
#     else:
#       statements;
#--------------------------------------------------------------------------------------------
numbers = [12,19,67,33,89];

for num in numbers:
  if(num % 7 == 0):
    print(num);
    break;
else:
  print("Not Found");