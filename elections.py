# Import a few packages
import time
import matplotlib.pyplot as plt

# Initialise the lists to use
contestants = ['Kwiatowski', 'Lewandowski', 'Zajak', 'Tatomir\n']
polling_box = []

print("Welcome, everyone, to the Wrocław 2023 Municipal Elections! \nThis is the 69th time this election is being held and today, we have 4 worthy candidates contesting for the position of Head of State!\n")

# Loops through the block of code based on a set logical condition
while True:
    answer = input('Would you like to vote? \n--> ')
    answer = answer.lower()         # <--- Makes the input to the 'answer' variable case-insensitive
    # 'If/elif' statements to perform a set action depending on the input of 'answer'
    if answer == 'yes':
        print(f"That's great! :) Now then, here are today's contestants ")
        # A for loop to return all values of the 'contestants' list, with a 1-second time lag
        for c in contestants:
            time.sleep(1)
            print(f'--> {c}')
        vote = input('Cast your vote: ')
        # Nested if/elif statements to add the results to the 'polling_box' list depending on the candidate voted for
        if vote == '1':
            polling_box.append(contestants[0])
        elif vote == '2':
            polling_box.append(contestants[1])
        elif vote == '3':
            polling_box.append(contestants[2])
        elif vote == '4':
            polling_box.append(contestants[3])
        else:
            print('Invalid input. Not an option.')
    elif answer == 'no':
        print('Have a good day :)')
        break
    # Prints a message if the above 'if/elif' conditions are not met
    else:
        print("Please answer with either 'Yes' or 'No' :)")
print(polling_box)

# Plots a histogram of the values of the 'polling_box' list using the 'pyplot' subpackage of 'matplotlib'
plt.hist(polling_box, bins=4)
plt.show()
plt.clf()
