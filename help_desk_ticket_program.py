# FILE NAME - help_desk_ticket_program.py
# Remember to cite any sources you used to help you complete this project!

# NAME: Jorge Bustos
# DATE: 05/17/26
# BRIEF DESCRIPTION: Help desk ticket program where user can enter a computer problem then choose a category, see a basic troubleshooting suggestion, and save the ticket to a text file.

# Source: https://chatgpt.com/ I used ChatGPT to help brainstorm what program to write, help me figure out troubleshooting suggestions, and to then check my code for errors.


print("Welcome to the Basic Help Desk Ticket Program")

# lists used to store ticket information 

ticket_names = []
ticket_devices = []
ticket_categories = []
ticket_descriptions = []

# list used for the category menu

categories = ["Internet", "Printer", "Slow Computer", "Login Problem", "Other"]

running = True

while running:
    print("\nPlease choose from the menu:")
    print("1. Create a help desk ticket")
    print("2. View current tickets")
    print("3. Save tickets to file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nCreate a Help Desk Ticket")

        name = input("Enter the user's name: ")
        device = input("Enter the device type: ")
        description = input("Briefly describe the problem: ")

        print("\nChoose a problem category:")
        for i in range(len(categories)):
            print(str(i + 1) + ". " + categories[i])

        category_choice = input("Enter a category number: ")

        if category_choice == "1":
            category = "Internet"
            suggestion = "Check Wi-Fi, restart the router, and make sure airplane mode is off. If using Ethernet ensure that it's plugged in correctly."
        elif category_choice == "2":
            category = "Printer"
            suggestion = "Check ink/toner levels, update or reinstall printer drivers, and ensure proper connection settings."
        elif category_choice == "3":
            category = "Slow Computer"
            suggestion = "Close unnecessary background applications, run a malware scan, and consider upgrading your RAM or switching to an SSD for a speed boost."
        elif category_choice == "4":
            category = "Login Problem"
            suggestion = "Check the username, password, and caps lock key. "
        elif category_choice == "5":
            category = "Other"
            suggestion = "Restart the device and collect more information."
        else:
            category = "Invalid" 
            suggestion = "No Troubleshooting suggestion available."   

        ticket_names.append(name)
        ticket_devices.append(device)
        ticket_categories.append(category)
        ticket_descriptions.append(description)

        print("\nTicket created.")
        print("User: " + name)
        print("Device: " + device)
        print("Category: " + category)
        print("Problem: " + description)
        print("Suggested first step: " + suggestion)

    elif choice == "2":
        print("\nCurrent Tickets")

        if len(ticket_names) == 0:
            print("No tickets have been created yet.")
        else:
            for i in range(len(ticket_names)):
                print("\nTicket " + str(i + 1))
                print("User: " + ticket_names[i])
                print("Device: " + ticket_devices[i])
                print("Category: " + ticket_categories[i])
                print("Problem: " + ticket_descriptions[i])

    elif choice == "3":
        if len(ticket_names) == 0:
            print("\nThere are no tickets to save.")
        else:
            with open("help_desk_tickets.txt", "w") as file:
                for i in range(len(ticket_names)):
                    file.write("Ticket " + str(i + 1) + "\n")
                    file.write("User: " + ticket_names[i] + "\n")
                    file.write("Device: " + ticket_devices[i] + "\n")
                    file.write("Category: " + ticket_categories[i] + "\n")
                    file.write("Problem: " + ticket_descriptions[i] + "\n")
                    file.write("\n")

            print("\nTickets saved to help_desk_tickets.txt")

    elif choice == "4":
        print("\nThank you for using the Basic Help Desk Ticket Program.")
        running = False

    else:
        print("\nInvalid choice. Please try again.")


########################################
#          REFLECTION QUESTIONS
########################################

'''
Remember to cite any sources you used to help you complete this project.
You can do that here in this section or cite as comments throughout your code.

1. How did you choose the goal of your program?

I chose this program because I am interested in computers and in two of my other courses this semester i learned a lot about IT support
it also felt fitting because it allowed me to accomplish everything that was required in the rubric.


2. What part of this project challenged you the most? How did you work through that challenge?

The hardest part for me was keeping the ticket information organized in lists.

I had to make sure the name, device, category, and problem description all stayed in order. I worked through it by testing 
the program each time i added a menu option instead of checking at the end.


3. If you had 10 more hours to improve or expand your program, what would you change? Why?

If I had 10 more hours to work on improving this program i would add more problem categories and save the troubleshooting suggestion
with the rest of the ticket information. That would make the program more useful by reminding the user of what they have already done.
I could also add a way to show the already resolved ones in a log.
'''
