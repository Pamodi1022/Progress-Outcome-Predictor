def user():
    user_list = ['student','staff']
    input_user = input("If you are a student enter 'student' or you are a staff member enter 'staff':").lower()
    if input_user in user_list:
        return input_user
    else:
        return user()
input_user = user()
def outcome():
    #Initialze variables for counter and assign an empty list to store each data
    Total_count = 0
    Progress_count = 0
    Trailer_count = 0
    Retriever_count = 0
    Exclude_count = 0
    Outcomes = []

     #outer loop of the program to collect the data until user choice is q
    while True:
        def text_file():
            print("\nPart 3")
            with open('output.txt', 'w') as outfile:
                    for item in Outcomes:
                        outfile.write(f"{item}\n")

            with open('output.txt', 'r') as infile:
                    print(infile.read())
            # Function to get the user's choice
        def choice():
            print("\nWould you like to emter another set of data ?")
            choice_list = ['y','q']
            input_choice = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
            if input_choice in choice_list:
                return input_choice
            else:
                print("Invalid input")
                return choice()

        #Functions to get inputs with validation
        def credit_inputs(credit):
            while True:
                try:
                    inputs = int(input(credit))
                    if inputs in [0,20,40,60,80,100,120]:
                        return inputs
                    else:
                        print("Out of Range")

                except ValueError:
                    print("Integer Required")

        #Get inputs
        Pass_credits = credit_inputs("Enter your total PASS credits: ")
        Defer_credits = credit_inputs("Enter your total DEFER credits: ")
        Fail_credits = credit_inputs("Enter your total FAIL credits: ")

        #Calculate the Total credits
        credits_list = [Pass_credits, Defer_credits, Fail_credits]
        Credits = f"{credits_list[0]},{credits_list[1]},{credits_list[2]}"
        Total = (Pass_credits + Defer_credits + Fail_credits)

        #Check whether the Total eqauls to 120 or not
        if Total == 120:
            Total_count += 1
            if Pass_credits == 120:
                print("Progress")
                Progress = f"Progress - {Credits}"
                Outcomes.append(Progress)
                Progress_count += 1

            elif Pass_credits == 100:
                print("Progress (module trailer)")
                Trailer = f"Progress (module trailer) - {Credits}"
                Outcomes.append(Trailer)
                Trailer_count += 1

            elif Fail_credits >= 80:
                print("Exclude")
                Exclude = f"Exclude - {Credits}"
                Outcomes.append(Exclude)
                Exclude_count += 1

            else:
                print("Do not progress - module retriever")
                Retriever = f"Do not progress - module retriever - {Credits}"
                Outcomes.append(Retriever)
                Retriever_count += 1

        else:
            print("Total incorrect")

        if input_user == 'student':
            text_file()
            break
        
        #Call the function choice to continue or quit
        input_choice = choice()
        if input_choice == 'y':
            continue
        elif input_choice == 'q':
            text_file()
        break

outcome()
