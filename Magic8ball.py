from random import randint
 
ball_spin = ["It is certain", "It is decidedly so", "Without a doubt",
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", 
"Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", 
"Ask again later", "Better not tell you now", "Cannot predict now",
"Concentrate and ask again", "Don't count on it", "My reply is no", 
"My sources say no", "Outlook not so good", "Very doubtful"]

def number(ball_spin):
    return randint(0,21)
    
my_number = number(ball_spin)
result = "The Magic 8 ball says: "
end = "***** Game Over! *****"
ques = "What is your YES or NO question: "
 
def outcome(my_number):
    print result + ball_spin[my_number]
    
"""
There are 20 possible outcomes and at most asks two times to play for the 
magic 8 ball. If the user wants to play it asks them for a YES/NO question, 
but what they type as a question really doesn't matter. It's more for UI.
""" 
for turn in range(1):
    start = raw_input('Do you want to shake the Magic 8 Ball? y/n: ').lower()
    if start != 'y' and start != 'n':
        print "You did not enter 'y' or 'n'"
        start
#If user wants to play, there are three options they can return    
    elif start == 'y':
        raw_input(ques)
        outcome(my_number) 
#If user says they don't want to play, I'll give them a second chance and ask one more time
    elif start == 'n':
        start_again = raw_input("Are you sure? Enter 'y' if you'd like to play and 'n' if you don't: ").lower()
        if start_again == 'y':
            raw_input(ques)
            outcome(my_number)
        elif start_again != 'y' and start_again != 'n':
            print "You did not enter 'y' or 'n'"
        elif start_again == 'n':
            print "Sorry you don't want to play :("
            
#when it's over, print GAME OVER  
while turn == 0:
            print end
            break