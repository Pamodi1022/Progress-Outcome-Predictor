from graphics import*

#Function to get the user
def user():
    user_list = ['student','staff']
    input_user = input("If you are a student enter 'student' or you are a staff member enter 'staff':").lower()
    if input_user in user_list:
        return input_user
    else:
        return user()
input_user = user()

def outcome():
    #Initialize variables for counter and assign an empty list to store each data
    Total_count = 0
    Progress_count = 0
    Trailer_count = 0
    Retriever_count = 0
    Exclude_count = 0
    Outcome_list = []
    
    #outer loop of the program to collect the data until user choice is q
    while True:
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
                Outcome_list.append(Progress)
                Progress_count += 1

            elif Pass_credits == 100:
                print("Progress (module trailer)")
                Trailer = f"Progress (module trailer) - {Credits}"
                Outcome_list.append(Trailer)
                Trailer_count += 1

            elif Fail_credits >= 80:
                print("Exclude")
                Exclude = f"Exclude - {Credits}"
                Outcome_list.append(Exclude)
                Exclude_count += 1

            else:
                print("Do not progress - module retriever")
                Retriever = f"Do not progress - module retriever - {Credits}"
                Outcome_list.append(Retriever)
                Retriever_count += 1

        else:
            print("Total incorrect")
        
        if input_user == 'student':
            print("Part 2")
            for result in Outcome_list:
                print(result)
            break
        else:
            #Call the function choice to continue or quit
            input_choice = choice()
            if input_choice == 'y':
                continue
            elif input_choice == 'q':
                print("\nPart 2")
                #Display the list outcomes individually
                for result in Outcome_list:
                    print(result)
                break

    #Set up a window and display a histogram using graphics 
    win = GraphWin("Histogram",800,600)
    win.setBackground(color_rgb(255,255,255))

    #Display the title
    topic = Text(Point(100,25), "Histogram Results")
    topic.setTextColor(color_rgb(0,0,0))
    topic.setStyle("bold")
    topic.setSize(12)
    topic.draw(win)

    #Display the colors and diamensions for each bar
    bar_width = 80
    bar_height = 10
    progress_height = Progress_count * bar_height
    trailer_height = Trailer_count * bar_height
    exclude_height = Exclude_count * bar_height
    retriever_height = Retriever_count * bar_height

    #Display the total outcomes count
    total_count_text = Text(Point(100, 580), f"{Total_count} Outcomes in total")
    total_count_text.setTextColor(color_rgb(0, 0, 0))
    total_count_text.setStyle("bold")
    total_count_text.setSize(10)
    total_count_text.draw(win)

    #Draw a line
    aLine = Line(Point(30,500),Point(450,500))
    aLine.draw(win)

    #Difine a function to draw bars
    def bar(win,x,y,width,height,color,name,count):
        rect = Rectangle(Point(x,y), Point(x + width, y + height))
        rect.setFill(color)
        rect.draw(win)

        count = Text(Point(x + width/2, y - 20),str(count))
        count.setTextColor(color_rgb(0,0,0))
        count.setStyle("bold")
        count.setSize(10)
        count.draw(win)

        count_name = Text(Point(x + width/2, y + height + 20), name)
        count_name.setTextColor(color_rgb(0,0,0))
        count_name.setStyle("bold")
        count_name.setSize(10)
        count_name.draw(win)

    #Draw bars for each and every outcome
    bar(win,50,500 - progress_height, bar_width, progress_height, ("#9aff9a"), "Progress", Progress_count)
    bar(win, 150, 500 - trailer_height, bar_width, trailer_height, ("#7ccd7c"), "Trailer", Trailer_count)
    bar(win, 250, 500 - exclude_height, bar_width, exclude_height, ("#ACBF60"), "Exclude", Exclude_count)
    bar(win,350, 500 - retriever_height, bar_width, retriever_height, ("#eeb4b4"), "Retriever", Retriever_count)

    #Close the window by mouse click
    win.getMouse()
    win.close()

#Call the outcome function
outcome()
        

        
                       
    





























                    
                    
            

            
