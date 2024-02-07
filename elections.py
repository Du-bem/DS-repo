# Import a few packages
import time
import matplotlib.pyplot as plt
import functionality as fn

# Initialise the lists/create the variable to use
candidates = ['Kwiatowski', 'Lewandowski', 'Zajak', 'Tatomir']
polling_box = []
cand = "Here are today's candidates:"

print("Welcome, everyone, to the Wrocław 2023 Municipal Elections! \nThis is the 69th time this election is being held and today, we have 4 worthy candidates contesting for the position of Head of State!")

# Loops through the block of code based on a set logical condition
while True:
    answer = input('\nWould you like to vote?\n--> ')
    answer = answer.lower()         # <--- Makes the input to the 'answer' variable case-insensitive
    # 'If/elif' statements to perform a set action depending on the input of 'answer'
    if answer == 'yes':
        print(f"\nThat's great! :) Now then, here are today's candidates:")
        while True:
            # A for loop to return all values of the 'candidates' list, with a 1-second time lag
            for c in candidates:
                time.sleep(1)
                print(f'--> {c}')
            time.sleep(1.5)
            vote = input('Please cast your vote: ')
            vote = vote.lower()
            # Nested if/elif statements to add the results to the 'polling_box' list depending on the candidate voted for
            if vote == '1':
                polling_box.append(candidates[0])
                print(fn.thanks())
                time.sleep(1)
                print(cand)
            elif vote == '2':
                polling_box.append(candidates[1])
                print(fn.thanks())
                time.sleep(1)
                print(cand)
            elif vote == '3':
                polling_box.append(candidates[2])
                print(fn.thanks())
                time.sleep(1)
                print(cand)
            elif vote == '4':
                polling_box.append(candidates[3])
                print(fn.thanks())
                time.sleep(1)
                print(cand)
            elif vote == 'exit':
                break
            else:
                time.sleep(1.5)
                print("Invalid input. Input not an option.\nHere are today's candidates: ")
    elif answer == 'no':
        print('Have a good day :)')
        break
    # Prints a message if the above 'if/elif' conditions are not met
    else:
        print("Please answer either 'Yes' or 'No' :)")
print(polling_box)

# Plots a histogram of the values of the 'polling_box' list using the 'pyplot' subpackage of 'matplotlib'
plt.bar(candidates, len(polling_box), color="#4CAF50", width=0.4)
plt.show()
plt.clf()
