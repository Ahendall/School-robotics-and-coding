from playsound import playsound #using this for the movie-quoted parts
import time

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
The Meme Ending:
The wonderful subreddit of r/PrequelMemes ceases to exist without
their lord and savior *sniffle*.
"""
#Part 3
Part3Branch1Para = """
The Snitch Ending:
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

[Press Enter to Continue]"""

Part3ContPara = """
-----------------------------------------------------------------------------------------------------------------------
Palpatine: Did you ever hear the Tragedy of Darth Plagueis the wise?
I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force
to influence the midichlorians to create life...
He had such a knowledge of the dark side that he could even keep the ones he cared about from dying.

You: He could actually save people from dying?

Palpatine: The dark side of the Force is a pathway to many abilities some consider to be unnatural.

You: What happened to him?

Palpatine: He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did.
Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep.
Ironic... he could save others from death, but not himself.

You: Is it possible to learn this power?

Palpatine: Not from a Jedi.
------------------------------------------------------------------------------------------------------------------------
[Please wait for the Audio to finish]

You figure out Palpatine is the Sith Lord and inform the Jedi Council.
You return to the Chancellors office where Mace Windu has
overpowered the chancelor.
"""

#Part 4
Part4Branch1Para = """
The Happy Ending:
Without Palpatine manipulating you, you and Padme raise your children together and have a family.
Your children, Luke and Leia, become two of the most powerful Jedi in the galaxy alongside yourself.

(*Internally cries because this is what we all wanted for anakin*)
"""

Part4Branch2Para = """
Palpatine kills Windu with Force Lightning, Throwing him out of the office window.
With Windu dead, and the Jedi scattered across the Galaxy, Palpatine executes Order 66.
[Press Enter to Continue]
"""

Part4Branch2Cont = """
You and the 501st Clone Leigon have marched into the Jedi Temple, killing several Jedi Masters.
You go into the Jedi High Council Chamber, Where the younglings are hiding.

Will you kill the younglings (lmao)? Or will you spare them?
(Type: Kill/Spare)
"""

#Part 5
Part5Branch1Para = """
As per Sidious' (Formerly Palpatine's) orders, You go to the Mustafar planet system.
There, You kill the remaining Seperatist Leaders, essentially ending the war.

Through Padme, Obi Wan comes to you on Mustafar. After the most dangerous and difficult Lightsaber Duel
of your entire life, Obi Wan gains an advantage.
He has the High Ground.
[Press Enter to Continue]
"""
Part5Branch1Cont = """-----------------------------------------------------
Obi Wan: It's over, Anakin! I have the high ground!
You: You underestimate my power!
Obi Wan: Don't try it.
-----------------------------------------------------
[Please wait for the audio to finish]
"""

Part5Branch1TryIt = """
Will you test your ability, or will you listen to Obi Wan and retreat?
(Type: Try it/Don't Try It)"""
Part5Branch2Para = """
The Vader Ending
Remembering the younglings, you hesitate to jump over Obi Wan when you duel with him on Mustafar.
Instead, You retreat. Over many years, you train the younglings to be powerful Sith Inquisitors.
Once Sidious, formerly Palpatine, senses your betrayal, You and the inquisitors Ambush him.
You then take his place as the ruler of the Galaxy.
"""

#Part 6
Part6Branch1Para = """
Obi wan Cuts off both of your legs and your left arm. You're now withering in
pain by a lava river.

Will you shout "I HATE YOU" To Obi Wan, or will you stay silent whilst being engulfed in flames?
(Type: Hate/Silence)"""

Part6Branch2Para = """
You leave Mustafar and return to Coruscant.
Now, you are more powerful than ever, and you have a major decision to make
To remain forever an apprentice, or to be free.

Will you kill Palpatine and become the ruler of the Galaxy, or will you
remain as his apprentice?
(Type: kill/stay)"""

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
        
        elif Choice2.casefold() == "chancellor's orders" or "chancellors orders":
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
        playsound("DPW.mp3")
        time.sleep(2)
        print("Will you cut off Windu's Hand or let him kill Palpatine? (Type: Cut Hand/Kill Palpatine)")

        Choice3Ans = 0
        Choice3Completed = False

        while Choice3Completed == False:
            Choice3 = input()

            if Choice3.casefold() == "cut hand":
                print("You cut off Mace Windu's Hand!")
                Choice3Ans = 1
                Choice3Completed = True
            
            elif Choice3.casefold() == "kill palpatine" or "kill palps":
                print("You let Master Windu kill Chancellor Palpatine!")
                Choice3Ans = 0
                Choice3Completed = True

            else:
                print ("What you typed isn't an option! Try again.")

        #part 4 branch 1
        if Choice3Ans == 0:
            print(Part4Branch1Para)
        
        #part 4 branch 2
        elif Choice3Ans == 1:
            print(Part4Branch2Para)
            placeholder = input("\n")
            print(Part4Branch2Cont)
            Choice4Completed = False
            Choice4Ans = 0

            while Choice4Completed == False:
                Choice4 = input()

                if Choice4.casefold() == "kill":
                    print("You have killed the younglings (lmao)!")
                    Choice4Ans = 1
                    Choice4Completed = True

                elif Choice4.casefold() == "spare":
                    print("You have spared the younglings!")
                    Choice4Ans = 0
                    Choice4Completed = True

                else:
                    print("What you typed isn't an option! Try again.")

            #Part 5 Branch 1
            if Choice4Ans == 1:
                print(Part5Branch1Para)
                placeholder = input()
                print(Part5Branch1Cont)
                playsound("DontTryIt.mp3")
                time.sleep(2)
                print(Part5Branch1TryIt)
                Choice5Ans = 0
                Choice5Completed = False

                while Choice5Completed == False:
                    Choice5 = input()

                    if Choice5.casefold() == "try it":
                        print("Uh Oh. Knowing full well Kenobi is the master of the High Ground, you tried it.")
                        Choice5Ans = 1
                        Choice5Completed = True

                    elif Choice5.casefold() == "don't try it" or "dont try it":
                        print("You did not try it, and instead retreated.")
                        Choice5Ans = 0
                        Choice5Completed = True

                    else:
                        print("What you typed isn't an option! Try Again.")
            
                #Part 6 Branch 1
                if Choice5Ans == 1:
                    print(Part6Branch1Para)
                    Choice6Ans = 0
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "hate":
                            print("You: I HATE YOU")
                            print("Obi Wan: You were my brother anakin. I loved you.")
                            Choice6Ans = 1
                            Choice6Completed = True

                        elif Choice6.casefold() == "silence":
                            print("You stayed silent. Obi Wan watches in sadness as you get engulfed in flames.")
                            Choice6Ans = 0
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                if Choice5Ans == 0:
                    print(Part6Branch2Para)

            #Part 5 Branch 2
            elif Choice4Ans == 0:
                print(Part5Branch2Para)


#Part 2 Branch 2
elif Choice1Ans == 0:
    print(Part2Branch2Para)
