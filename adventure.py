import time
print("Hello, who are you?")
name = input()
print("Oh. Well it's nice to meet you,", name)

time.sleep(3)
print("Hey,", name, "are you still there?")
time.sleep(3)
print("Would you like to play a game? Y/N\nKeep in mind that all responses are case sensitive and must be capitalized for them to properly run")

choice = input()

def aLittleAdventure():
    mainTimeLine = input("You are a new adventurer who wants to join an upcoming guild.\nYou go to the guild hall when there is an old lady who asks for help. Will you help her? Y/N.")

    if (mainTimeLine == "Y"):

        timeLineA = input("You decide to help the old lady and go to her, asking what is wrong.\nShe claims that someone had stolen her purse, and points to an individual about half a block away who is running.\n Do you pursue them? Y/N")

        if (timeLineA == "Y"):
            print("""You quickly catch up to the man in an alley, the man looks to you, voice shaking and\n afraid, 'Please, I need to feed my family!' You don't care, the man still stole and you turn him\n into the guards. The guards tell you that you would make a great addition yourself. You join their\n ranks and become captain in a few short years. You still think back about what if you had become an adventurer though. MEH ENDING""")

        else: print("On second thought, you don't really feel like it. You walk away from the old woman and slip on a banana peel,   breaking your leg and your adventuring days are over. You become an obnoxious villager constantly telling new adventurers, 'I was once an adventurer like you, before I took a banana peel to the knee.' Your antics get so old so fast you are exiled from the village. BAD ENDING")
    
    else:

        timeLineB = input("You decide not to help the old lady and you continue down the road to the guild hall. Upon entering you see there aren't many people who are there, you are greeted by an old hunched over man who tells you that there is a quest he thinks is just for you, killing goblins. You groan and wish he had something more grandiose. Maybe you should ask? Y/N")

        if (timeLineB == "Y"):
            print("You ask for something more exciting and the man tells you that there is a quest to fight a legendary dragon, you eagerly accept and are on your way to fight it. It takes you two hours of treking there before you reach the destination. You confront the dragon when suddenly you remember: you forgot your gear. You die promptly and you are forever remembered as the unprepared adventurer. BAD ENDING")

        else: print("You decide to take the quest and pack your things, taking care of the problem swiftly, gaining knowledge and more combat experience under your belt. Before long you are the most renown adventurer of your village, taking more difficult quests and gaining legendary weapons and artifacts before you, yourself become a legend as well. GOOD ENDING")

# Had to declare the variable and else if after the function otherwise the function would run regardless of the user's choice
# Tried to make new lines to make code more readable but for some reason it skipped parts of the function, need to search more into it.
if(choice == "Y"):
    print("Very nice, then let's begin.")
    aLittleAdventure()
else:
    print("That's a shame. Well, goodbye then", name)

import sys
print("Thank you for playing this game,", name, "I hope to see you again soon.")
sys.exit()