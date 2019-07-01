from IPython.display import clear_output
import time
correct_password = "Ianrulz"
incorrect = True

while incorrect:
    clear_output()
    attempt = input("Please enter the password: ")
    if attempt == correct_password:
        print("Thank you, that password is correct")
        time.sleep(2)
        incorrect = False
        break
    else:
        print("Sorry, that password is incorrect... Please try again.")
        time.sleep(2)
        continue

print("Welcome inside")
