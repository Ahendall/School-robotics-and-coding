"""
ROTS CYOA By Ahendall
#This is the Simple Answer (SA) Version.
This is exactly the same as the CA Version but easier to answer.
"""
#For the audio to work, You must download simpleaudio through pip
import simpleaudio as sa
import time


"""
Audio functions & vars
use var.play() to immideatly continue the code while the audio is playing
use var.play().wait_done() to  wait until audio is finished.
"""    

def DarthPlagueis():
    #Not Background Audio, Use wait_done()
    sa.stop_all()
    dpw = "DPW.wav"
    dpw_obj = sa.WaveObject.from_wave_file(dpw)
    dpw_obj.play().wait_done()

def DontTryIt():
    #Not background audio, use wait_done()
    sa.stop_all()
    dti = "DontTryIt.wav"
    dti_obj = sa.WaveObject.from_wave_file(dti)
    dti_obj.play().wait_done()

def MainTheme():
    #background audio, do not use wait_done()
    sa.stop_all()
    swt = "StarWarsTheme.wav"
    swt_obj = sa.WaveObject.from_wave_file(swt)
    swt_obj.play()
    
def Betrayal():
    #background audio, do not use wait_done()
    sa.stop_all()
    abt = "AnakinBetrayal.wav"
    abt_obj = sa.WaveObject.from_wave_file(abt)
    abt_obj.play()

def Cantina():
    #background audio, do not use wait_done()
    sa.stop_all()
    cm = "CantinaMusic.wav"
    cm_obj = sa.WaveObject.from_wave_file(cm)
    cm_obj.play()

def Deeds():
    #background audio, do not use wait_done()
    sa.stop_all()
    ddd = "DarkDeeds.wav"
    ddd_obj = sa.WaveObject.from_wave_file(ddd)
    ddd_obj.play()

def ImpMarch():
    #background audio, do not use wait_done()
    sa.stop_all()
    march = "ImperialMarch.wav"
    march_obj = sa.WaveObject.from_wave_file(march)
    march_obj.play()

def Immolation():
    #Not background Audio, use wait_done()
    sa.stop_all()
    chosen = "ChosenOne.wav"
    chosen_obj = sa.WaveObject.from_wave_file(chosen)
    chosen_obj.play().wait_done()

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
    
To follow the Chancellor's Orders and kill Dooku, type 1.
To follow the Jedi Code, type 2."""

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

You: No.

Palpatine: I thought not. It's not a story the Jedi would tell you. It's a Sith legend.
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

To kill the younglings, type 1.
To let them live, type 2."""

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
To try it, type 1.
To listen to literally the master of the high ground and retreat, type 2."""
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

To shout "I HATE YOU", type 1.
To stay silent, type 2."""

Part6Branch2Para = """
You leave Mustafar and return to Coruscant.
Now, you are more powerful than ever, and you have a major decision to make
To remain forever an apprentice, or to be free.

To kill Palpatine and become ruler of the galaxy, type 1.
To remain as his apprentice, type 2."""

IHateYou = """
--------------------------------------------------------------
Obi Wan: You were the chosen one!
It was said that you would destroy the sith not join them!
Bring balance to the force, not leave it in darkness!

You: I HATE YOU
                                                              
Obi Wan: You were my brother Anakin. I loved you.               
--------------------------------------------------------------
"""

#Part 7
JarJarEnding = """
The Jar Jar Ending
Darth Jar Jar, Dark Lord of the Sith, was the true mastermind behind it all.
Planning everything from the beginning.
He kills you without hesitation.
"""
OverPoweredEnding = """
The Overpowered Ending
You become a Dark Lord of the Sith, so powerful and so wise that
you can use the force to influence the midichlorians to bring back
George Lucas to the franchise.
"""

TragicHeroEnding = """
The Tragic Hero Ending
"You have become the very thing you swore to destroy"
"""



#Actual Code Parts
#Story Part 1
MainTheme()
print(Part1Para)
print("To save Keneral Kenobi, type the number 1.\n" + "To let his ship get destroyed by buzz droids, type 2.")
Choice1Completed = False

while Choice1Completed == False:
    Choice1 = input()
    
    if Choice1 == "1":
        print("You have saved General Kenobi!")
        Choice1Completed = True
    
    elif Choice1 == "2":
        print("You did not save General Kenobi, and he has been killed in action.")
        Choice1Completed = True

    else:
        print ("What you typed isn't an option! Try again.")

# Part 2 Branch 1
if Choice1 == "1":
    print(Part2Branch1Para)
    Choice2Completed = False

    while Choice2Completed == False:
        Choice2 = input()
        if Choice2 == "2":
            print ("You have apprehended an unarmed Count Dooku.")
            Choice2Completed = True

        elif Choice2 == "1":
            print("You killed Count Dooku.")
            Choice2Completed = True

        else:
            print("What you typed isn't an option! Try again.")
            Choice2Completed = False
    
    #Part 3 Branch 1
    if Choice2 == "2":
        print(Part3Branch1Para)
        time.sleep(15)
        sa.stop_all()

    #Part 3 Branch 2
    if Choice2 == "1":
        print(Part3Branch2Para)
        placeholder = input("\n")
        print(Part3ContPara)
        DarthPlagueis()
        print("To cut Windu's hand, type 1.\n" + "To let him kill Palpatine, type 2.")
        Choice3Completed = False

        while Choice3Completed == False:
            Choice3 = input()

            if Choice3 == "1":
                Betrayal()
                print("You cut off Mace Windu's Hand!")
                Choice3Completed = True
            
            elif Choice3 == "2":
                Cantina()
                print("You let Master Windu kill Chancellor Palpatine!")
                Choice3Completed = True

            else:
                print ("What you typed isn't an option! Try again.")

        #part 4 branch 1
        if Choice3 == "2":
            print(Part4Branch1Para)
            time.sleep(15)
            sa.stop_all()
        
        #part 4 branch 2
        elif Choice3 == "1":
            print(Part4Branch2Para)
            placeholder = input("\n")
            print(Part4Branch2Cont)
            Choice4Completed = False

            while Choice4Completed == False:
                Choice4 = input()

                if Choice4.casefold() == "1":
                    print("You have killed the younglings (lmao)!")
                    Choice4Completed = True

                elif Choice4.casefold() == "2":
                    print("You have spared the younglings!")
                    Choice4Completed = True

                else:
                    print("What you typed isn't an option! Try again.")

            #Part 5 Branch 1
            if Choice4 == "1":
                print(Part5Branch1Para)
                placeholder = input()
                print(Part5Branch1Cont)
                DontTryIt()
                print(Part5Branch1TryIt)
                Choice5Completed = False

                while Choice5Completed == False:
                    Choice5 = input()

                    if Choice5.casefold() == "1":
                        print("Uh Oh. Knowing full well Kenobi is the master of the High Ground, you tried it.")
                        Choice5Completed = True

                    elif Choice5.casefold() == "2":
                        print("You did not try it, and instead retreated.")
                        Choice5Completed = True

                    else:
                        print("What you typed isn't an option! Try Again.")
            
                #Part 6 Branch 1
                if Choice5 == "1":
                    print(Part6Branch1Para)
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "1":
                            print(IHateYou)
                            Immolation()
                            Choice6Completed = True

                        elif Choice6.casefold() == "2":
                            print("You stayed silent. Obi Wan watches in sadness as you get engulfed in flames.")
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    #Part 7 Branch 1
                    if Choice6 == "1":
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)
                        sa.stop_all()

                    #Part 7 Branch 2
                    if Choice6 == "2":
                        print(TragicHeroEnding)
                        Deeds()
                        time.sleep(15)
                        sa.stop_all()

                #Part 6 Branch 2
                if Choice5 == 0:
                    Deeds()
                    print(Part6Branch2Para)
                    Choice6Completed = False

                    while Choice6Completed == False:
                        Choice6 = input()

                        if Choice6.casefold() == "1":
                            print("You mercilessly killed Palpatine in his sleep.")
                            Choice6Completed = True

                        elif Choice6.casefold() == "2":
                            print("You stayed as Palpatine's apprentice!")
                            Choice6Completed = True

                        else:
                            print("What you typed isn't an option! Try Again.")

                    #Part 7 Branch 3
                    if Choice6 == "1":
                        ImpMarch()
                        print(JarJarEnding)
                        sa.stop_all()
                       
                    #Part 7 Branch 4
                    elif Choice6 == "2":
                        print(OverPoweredEnding)
                        sa.stop_all()

            #Part 5 Branch 2
            elif Choice4 == "2":
                ImpMarch()
                print(Part5Branch2Para)
                time.sleep(5)
                sa.stop_all()


#Part 2 Branch 2
elif Choice1 == "2":
    print(Part2Branch2Para)
    sa.stop_all()
