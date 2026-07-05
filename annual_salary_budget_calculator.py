# Loop
# print(f"USER ANNUAL SALARY = {user_annual_salary}")
try:
    user_annual_salary = int(input("Hello! Please input your annual salary: "))
    
    print(f"Your annual salary is ${user_annual_salary}!")
except ValueError:
    print("Invalid value! Please input a number for your salary.")

    # If invalid value
        # Print "Invalid value!"
    # Print entire budget
    # Ask user if they want to restart or end program (y/n)
    # If y
        # Restart program
    # Else
        # Terminate