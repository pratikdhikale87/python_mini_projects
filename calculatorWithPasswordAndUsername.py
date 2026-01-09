# make a calculator which will take username = "pratik" & password = "pratikdhikale" 
# properties :-
          # username = "pratik"
          # password = "pratikdhikale"
          # it will run continue

# actual hidden password and user name 
password = "pratikdhikale"
username = "pratik"

user_uname = input("Please enter the username :")

user_password = input("Please enter your password :")

if user_uname == username and user_password == password :
     #print test statement
     print("🥳🥳 Welcome to  premium calculator 🥳🥳🥳")
     # ye continue chalega

     while(True):
          print("Please select the operation :")
          print("1.Addition(+) \n2.Subtraction(-) \n3.Multiplication(*) \n4.Division(/)")
          print("For exit press... ctrl + c")

          choice  = int(input())

          # we should check the user doesn't make choice diff than specific listed options
          if choice > 4 :
               print("Invalid operation 👎❌....")
               break

          first_number = int(input("Enter first number : "))
          second_number = int(input("Enter second number :"))

          ans = None
          match choice:
               case 1:
                    ans = first_number + second_number
                    # break # this break is causing problem now  
               case 2:
                    ans = first_number - second_number
                    
               case 3:
                    ans = first_number * second_number
                    
               case 4:
                    ans = first_number / second_number
                    
               case _:   # this may never get execute
                    print("Invalid choice....❌")
          #last section printing the output

          # i think ans = None never be her (check if error)
          print(f"Result of operation: {ans} ")
else:
     print("🚫🚫⛔ You can't use this calculator.... 🚫🚫⛔")



     #point to be remember from this program : 

               # python don't uses the break in match as we use in java "switch" statement