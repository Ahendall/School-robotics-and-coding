# Making the paragraph vars here so that they aren't affected by the indents later on (Tested it with the multiline print previously and the indenting affected it)
Part1Para = """
You are General Anakin Skywalker during the Battle Above Coruscant.
You and General Obi-Wan Kenobi are heading towards Separatist General Grievous' ship but
Kenobi's starfighter gets hit by Buzz Droids.
"""
#Part 2
Part2Branch1Para = """
With General Kenobi saved, Together you go to save the Chancellor.
When you find the Chancellor, Count Dooku (Leader of the seperatist army) is waiting for you.
After an agressive Duel, you have Dooku on his knees.
    
Will you follow the Chancellor's orders to kill Dooku, or will you
follow the Jedi Code? (Type: Chancellor's Orders/Jedi Code) """

Part2Branch2Para = """
The meme ending:
The wonderful subreddit of r/PrequelMemes ceases to exist without
their lord and savior *sniffle*.
"""
#Part 3
Part3Branch1Para = """
The snitch ending:
You and Obi-Wan take Dooku to the jedi council on Coruscant.
At trial, Count Dooku reveals the identity of the Sith Lord.
You and several Jedi Masters Confront Chancellor Palpatine in his office where
he swiftly escapes and executes Order 66.
Many Jedi are killed.
"""
Part3Branch2Para = """
Back on Coruscant, You start to have visions of your wife, Padme,
Dying during childbirth.
You confide in Chancellor Palpatine.

Palpatine then tells you the Tradgedy of Darth Plagueis the Wise
---
Did you ever hear the Tragedy of Darth Plagueis the wise?
I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force
to influence the midichlorians to create life...
He had such a knowledge of the dark side that he could even keep the ones he cared about from dying.
The dark side of the Force is a pathway to many abilities some consider to be unnatural.
He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did.
Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
Ironic... he could save others from death, but not himself.
---
[Press Enter to Continue]"""

Part3ContPara = """You figure out Palpatine is the Sith Lord and inform the Jedi Council.
You return to the Chancellors office where Mace Windu has
overpowered the chancelor.
"""

#Actual Code Parts
#Story Part 1
print(Part1Para)
print("Will you save General Kenobi? (Type: Yes/No)")
Choice1Completed = False
Choice1Ans = 0

while Choice1Completed == False:
    Choice1 = input()
    
    if Choice1.casefold() == "yes":
        print("You have saved General Kenobi!")
        Choice1Ans = 1
        Choice1Completed = True
    
    elif Choice1.casefold() == "no":
        print("You did not save General Kenobi, and he has been killed in action.")
        Choice1Ans = 0
        Choice1Completed = True

    else:
        print ("What you typed isn't an option! Try again.")

# Part 2 Branch 1
if Choice1Ans == 1:
    print(Part2Branch1Para)
    Choice2Completed = False
    Choice2Ans = 0

    while Choice2Completed == False:

        Choice2 = input()

        if Choice2.casefold() == "jedi code":
            print ("You have apprehended an unarmed Count Dooku.")
            Choice2Ans = 1
            Choice2Completed = True
        
        elif Choice2.casefold() == "chancellor's orders":
            print("You killed Count Dooku.")
            Choice2Ans = 0
            Choice2Completed = True

        else:
            print("What you typed isn't an option! Try again.")
    
    #Part 3 Branch 1
    if Choice2Ans == 1:
        print(Part3Branch1Para)

    #Part 3 Branch 2
    if Choice2Ans == 0:
        print(Part3Branch2Para)
        placeholder = input("\n")
        print(Part3ContPara)
        print("Will you cut off Windu's Hand or let him kill Palpatine? (Type: Cut Hand/Kill Palpatine)")

        Choice3Ans = 0
        Choice3Completed = False

        while Choice3Completed == False:
            Choice3 = input()

            if Choice3.casefold() == "cut hand":
                print("You cut off Mace Windu's Hand!")
                Choice3Ans = 1
                Choice3Completed = True
            
            elif Choice3.casefold() == "kill palpatine":
                print("You let Master Windu kill Chancellor Palpatine!")
                Choice3Ans = 0
                Choice3Completed = True

            else:
                print ("What you typed isn't an option! Try again.")


#Part 2 Branch 2
elif Choice1Ans == 0:
    print(Part2Branch2Para)
