# Loop
# print(f"USER ANNUAL SALARY = {user_annual_salary}")
try:
    user_annual_salary = int(input("Hello! Please input your annual salary: "))
    
    print(f"\nYour annual salary is ${user_annual_salary}!\n")

    if user_annual_salary >= 100000:
        print("***** ANNUALLY BREAK DOWN *****")
        print(f"  NEEDS (50%): {user_annual_salary * 0.5}")
        print(f"  WANTS (30%): {user_annual_salary * 0.3}")
        print(f"SAVINGS (20%): {user_annual_salary * 0.2}")

        print("\n***** MONTHLY BREAK DOWN *****")
        print(f"  NEEDS (50%): {user_annual_salary * 0.5 / 12}")
        print(f"  WANTS (30%): {user_annual_salary * 0.3 / 12}")
        print(f"SAVINGS (20%): {user_annual_salary * 0.2 / 12}")

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