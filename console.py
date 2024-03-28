from desktop import read_file

def verify_input(input):
    if (int(input) <1 or int(input) > 17):
        wrong_input()
    else:
        correct_input(input)
    
def correct_input(input):
    print(read_file(int(input)))

def wrong_input():
    articleAsked = input("Incorrect entry, please enter a number between 1 and 17 : ")
    verify_input(articleAsked)

articleAsked = input("Please select a number between 1 and 17 : ")
verify_input(articleAsked)