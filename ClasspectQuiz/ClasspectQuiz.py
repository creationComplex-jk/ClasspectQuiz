#Add more questions (duh) (make aspects more equally represented, keep roles equally represented)
#Add something that shows your actpas score (compared to how active or passive your class is)
#Add destroyer class aspect reversal shenanigans
#Make lord and muse harder to come by
#In general you're gonna wanna add more nuance



import random

breath = 0
life = 0
light = 0
time = 0
heart = 0
rage = 0
blood = 0
doom = 0
void = 0
space = 0
mind = 0
hope = 0
restore = 0
guide = 0
wield = 0
steal = 0
destroy = 0
create = 0
rule = 0


aspect_list = [breath, blood, space, time, light, void, hope, rage, heart, mind, life, doom]
aspect_names = ["Breath", "Blood", "Space", "Time", "Light", "Void", "Hope", "Rage", "Heart", "Mind", "Life", "Doom"]
role_list = [restore, guide, wield, steal, destroy, create, rule]

def question_one(aspect_list, role_list):
    print("1")
    print("Which of these do you have the strongest relationship with?")
    print("A) The unknown and unknowable.")
    print("B) Who you are as a person.")
    print("C) Your own mortality.")
    print("D) Your creative drive.")
    print("E) How the world works.")
    print("F) Your dreams and ideals.")
    print("G) Your place in the world.")
    print("H) Your actions and decisions.")
    print("I) Your circle of relationships.")
    print("J) The society you live in.")
    print("K) Your faith in a higher power.")
    print("L) Your darkest fears and/or impulses.")
    print("M) Nothing in particular.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[5] += 2
        elif answer == "B" or answer == "b":
            aspect_list[8] += 2
        elif answer == "C" or answer == "c":
            aspect_list[11] += 2
            aspect_list[3] += 1
        elif answer == "D" or answer == "d":
            aspect_list[2] += 2
        elif answer == "E" or answer == "e":
            aspect_list[9] += 1
        elif answer == "F" or answer == "f":
            aspect_list[6] += 1
            aspect_list[10] += 1
        elif answer == "G" or answer == "g":
            aspect_list[4] += 2
        elif answer == "H" or answer == "h":
            aspect_list[0] += 1
            aspect_list[9] += 1
        elif answer == "I" or answer == "i":
            aspect_list[1] += 2
        elif answer == "J" or answer == "j":
            aspect_list[1] += 1
            aspect_list[10] += 1
        elif answer == "K" or answer == "k":
            aspect_list[6] += 2
        elif answer == "L" or answer == "l":
            aspect_list[7] += 2
        elif answer == "M" or answer == "m":
            aspect_list[5] += 1
            aspect_list[7] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_two(aspect_list, role_list):
    print("2")
    print("What role do you take in a group project?")
    print("A) I take charge of the situation.")
    print("B) I do what I'm told.")
    print("C) I let others do the work for me.")
    print("D) I try and keep everyone on task.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            actpas = 2
            return actpas
        elif answer == "B" or answer == "b":
            actpas = 1
            return actpas
        elif answer == "C" or answer == "c":
            actpas = 1
            return actpas
        elif answer == "D" or answer == "d":
            actpas = 2
            return actpas
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_three(aspect_list, role_list):
    print("3")
    print("What role do you think describes you the best?")
    print("A) I'm the one who who keeps things stable and cleans up messes.")
    print("B) I'm the planner, and the one who keeps things on track.'.")
    print("C) I'm the muscle, the fighter, the one you don't want to cross.")
    print("D) I'm the one gets things done, the problem solver, the resourceful one.")
    print("E) I'm the one who gets their hands on the resources needed.")
    print("F) I'm the one who has what is needed and can make more just in case.")
    print("G I'm the one in charge.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            role_list[0] += 1
        elif answer == "B" or answer == "b":
            role_list[1] += 1
        elif answer == "C" or answer == "c":
            role_list[4] += 1
        elif answer == "D" or answer == "d":
            role_list[2] += 1
        elif answer == "E" or answer == "e":
            role_list[3] += 1
        elif answer == "F" or answer == "f":
            role_list[5] += 1
        elif answer == "G" or answer == "g":
            role_list[6] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_four(aspect_list, role_list):
    print("4")
    print("When push comes to shove, what is your first response?")
    print("A) I would shove back.")
    print("B) I'd get the hell out of there.")
    print("C) I'd try and de-escalate the situation.")
    print("D) I'm the reason it came to this.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            role_list[4] += 1
            role_list[2] += 1
        elif answer == "B" or answer == "b":
            role_list[1] += 1
            role_list[3] += 1
        elif answer == "C" or answer == "c":
            role_list[0] += 1
            role_list[5] += 1
        elif answer == "D" or answer == "d":
            role_list[4] += 1
            role_list[5] += 1
            role_list[6] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_five(aspect_list, role_list):
    print("5")
    print("What draws you into a story the most?")
    print("A) A fleshed out and self-consistent setting.")
    print("B) An captivating and complex plot.")
    print("C) Interesting and deep characters.")
    print("D) The tone and mood of a story.")
    print("E) The underlying themes.")
    print("F) The relationships between characters.")
    print("G) The climax of the story.")
    print("H) The end of the story.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[2] += 2
            aspect_list[11] += 1
        elif answer == "B" or answer == "b":
            aspect_list[3] += 2
            aspect_list[9] += 2
        elif answer == "C" or answer == "c":
            aspect_list[8] += 2
        elif answer == "D" or answer == "d":
            aspect_list[6] += 2
            aspect_list[7] += 2
        elif answer == "E" or answer == "e":
            aspect_list[4] += 2
            aspect_list[10] += 1
        elif answer == "F" or answer == "f":
            aspect_list[1] += 2
        elif answer == "G" or answer == "g":
            aspect_list[10] += 2
        elif answer == "H" or answer == "h":
            aspect_list[11] += 2
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_six(aspect_list, role_list):
    print("6")
    print("What drives you more?")
    print("A) Friends and family.")
    print("B) My own whims.")
    print("C) Societal pressure.")
    print("D) My own convictions.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[1] += 2
        elif answer == "B" or answer == "b":
            aspect_list[0] += 2
        elif answer == "C" or answer == "c":
            aspect_list[1] += 1
        elif answer == "D" or answer == "d":
            aspect_list[0] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)    

def question_seven(aspect_list, role_list):
    print("7")
    print("What do you seek more?")
    print("A) To be the center of the world.")
    print("B) To be unknowable.")
    print("C) Somewhere inbetween.")
    print("D) Neither.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
             aspect_list[4] += 2
        elif answer == "B" or answer == "b":
            aspect_list[5] += 2
        elif answer == "C" or answer == "c":
            aspect_list[4] += 1
            aspect_list[5] += 1
        elif answer == "D" or answer == "d":
            aspect_list[4] += 0
            aspect_list[5] += 0
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_eight(aspect_list, role_list):
    print("8")
    print("How much control do you have over your own life?")
    print("A) A lot.")
    print("B) A little.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            actpas = 3
            return actpas
        elif answer == "B" or answer == "b":
            actpas = -3
            return actpas
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_nine(aspect_list, role_list):
    print("9")
    print("How has your life gone so far?")
    print("A) Perfectly, I wouldn't change a thing.")
    print("B) I've had some mild difficulty, nothing too bad.")
    print("C) I'm doing alright, but life's had its ups and downs..")
    print("D) There have been some serious rough patches, but I'm managing.")
    print("E) It's hard to imagine a future for myself some days.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[10] += 3
        elif answer == "B" or answer == "b":
            aspect_list[10] += 2
        elif answer == "C" or answer == "c":
            aspect_list[10] += 1
            aspect_list[11] += 1
        elif answer == "D" or answer == "d":
            aspect_list[11] += 2
        elif answer == "E" or answer == "e":
            aspect_list[11] += 3
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_ten(aspect_list, role_list):
    print("10")
    print("What's your opinion on the nature of the universe?")
    print("A) We are under the care and supervision of a just and loving god.")
    print("B) If there is a god, or multiple, then they're not worth worshipping.")
    print("C) The universe only exists because we believe it does, as does everything within it.")
    print("D) All of reality is a series of causal chains.")
    print("E) We live in a multiverse where all of our choices already exist, we need only make them.")
    print("F) The universe is a consequence of innumerable factors, we don't, and perhaps might never, fully understand.")
    print("G) I don't think about it.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[6] += 1
        elif answer == "B" or answer == "b":
            aspect_list[7] += 1
        elif answer == "C" or answer == "c":
            aspect_list[4] += 1
        elif answer == "D" or answer == "d":
            aspect_list[3] += 1
        elif answer == "E" or answer == "e":
            aspect_list[9] += 1
        elif answer == "F" or answer == "f":
            aspect_list[2] += 1
        elif answer == "G" or answer == "g":
            aspect_list[5] += 1
        else:
            print("Invalid Answer")
            valid = False
        #print(aspect_list)   

def question_eleven(aspect_list, role_list):
    print("11")
    print("Do you believe in free will?")
    print("A) Yes.")
    print("B) No.")
    print("C) I'm not sure.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            actpas = 2
            return actpas
        elif answer == "B" or answer == "b":
            actpas = -2
            return actpas
        elif answer == "C" or answer == "c":
            actpas = 0
            return actpas
    else:
        print("Invalid Answer")
        valid = False
    #print(aspect_list)

def question_twelve(aspect_list, role_list):
    print("12")
    print("Which of these subjects interests you more?")
    print("A) The Arts, and other creative subjects.")
    print("B) Technology and/or Engineering")
    print("C) Languages, foreign or otherwise.")
    print("D) History and other Social Studies.")
    print("E) Math and/or Science.")
    print("F) Business and Finance.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[2] += 1
        elif answer == "B" or answer == "b":
            aspect_list[5] += 1
        elif answer == "C" or answer == "c":
            aspect_list[10] += 1
        elif answer == "D" or answer == "d":
            aspect_list[3] += 1
        elif answer == "E" or answer == "e":
            aspect_list[11] += 1
        elif answer == "F" or answer == "f":
            aspect_list[9] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_thirteen(aspect_list, role_list):
    print("13")
    print("What do you envision your future to be like?")
    print("A) A life of success, fame, and fortune.")
    print("B) I'm going to die unfulfilled.")
    print("C) My life will be long and fruitful.")
    print("D) My life is gonna fucking suck and I'm gonna live it anyway.")
    print("E) I believe I am going to achieve my dreams.")
    print("F) My future will be the best I can make it.")
    print("G) I'll find myself out there, somewhere.")
    print("H) I'll keep my head down and carve my own pocket of stability.")
    print("I) I'll go wherever the wind takes me and adapt to whatever life throws my way.")
    print("J) The world will end before I do.")
    print("K) The world will end and take me with it.")
    print("L) I have no idea.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[4] += 1
        elif answer == "B" or answer == "b":
            aspect_list[11] += 1
        elif answer == "C" or answer == "c":
            aspect_list[10] += 1
        elif answer == "D" or answer == "d":
            aspect_list[7] += 1
        elif answer == "E" or answer == "e":
            aspect_list[6] += 1
        elif answer == "F" or answer == "f":
            aspect_list[9] += 1
        elif answer == "G" or answer == "g":
            aspect_list[8] += 1
        elif answer == "H" or answer == "h":
            aspect_list[1] += 1
        elif answer == "I" or answer == "i":
            aspect_list[0] += 1
        elif answer == "J" or answer == "j":
            aspect_list[3] += 1
        elif answer == "K" or answer == "k":
            aspect_list[2] += 1
        elif answer == "L" or answer == "l":
            aspect_list[5] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_fourteen(aspect_list, role_list):
    print("14")
    print("How do you handle stress or adversity?")
    print("A) I remove the source.")
    print("B) I put on a brave face and push through.")
    print("C) I try and avoid it where possible.")
    print("D) I ask for help.")
    print("E) I ignore it.")
    print("F) I figure out a way past it.")
    print("G) What adversity?")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            role_list[4] += 1
        elif answer == "B" or answer == "b":
            role_list[2] += 1
        elif answer == "C" or answer == "c":
            role_list[5] += 1
        elif answer == "D" or answer == "d":
            role_list[0] += 1
        elif answer == "E" or answer == "e":
            role_list[3] += 1
        elif answer == "F" or answer == "f":
            role_list[1] += 1
        elif answer == "G" or answer == "g":
            role_list[6] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_fifteen(aspect_list, role_list):
    print("15")
    print("What is your opinion on yourself?")
    print("A) I'm fairly average.")
    print("B) I think very highly of myself.")
    print("C) I despise myself.")
    print("D) I certainly have my flaws.")
    print("E) I'd say I'm above some.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            lunarsway = 0
            return lunarsway
        elif answer == "B" or answer == "b":
            lunarsway = 2
            return lunarsway
        elif answer == "C" or answer == "c":
            lunarsway = -2
            return lunarsway
        elif answer == "D" or answer == "d":
            lunarsway = -1
            return lunarsway
        elif answer == "E" or answer == "e":
            lunarsway = 1
            return lunarsway
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_sixteen(aspect_list, role_list):
    print("16")
    print("How do you respond to crisis?")
    print("A) Logically, thoughtfully, carefully.")
    print("B) As quickly as I can, the sooner, the faster, the better.")
    print("C) Whatever my gut feeling is.")
    print("D) I'll put it off or leave someone else to handle it.")
    print("E) I'll go and grab help as soon as I can.")
    print("F) I'd stew in misery for not stopping it.")
    print("G) I'd assert control over every aspect of the situation.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            role_list[1] += 1
        elif answer == "B" or answer == "b":
            role_list[3] += 1
        elif answer == "C" or answer == "c":
            role_list[2] += 1
        elif answer == "D" or answer == "d":
            role_list[5] += 1
        elif answer == "E" or answer == "e":
            role_list[0] += 1
        elif answer == "F" or answer == "f":
            role_list[4] += 1
        elif answer == "G" or answer == "g":
            role_list[6] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_seventeen(aspect_list, role_list):
    print("17")
    print("Where do most of your problems come from?")
    print("A) From myself, my thoughts, feelings, actions, etc. I'm my own worst enemy.")
    print("B) From external circumstance, Things happen to me, and I'm left dealing with the fallout.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            lunarsway = -1
            return lunarsway
        elif answer == "B" or answer == "b":
            lunarsway = 1
            return lunarsway
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_eighteen(aspect_list, role_list):
    print("18")
    print("What are you more instinctually knowledgeable about?")
    print("A) Your identity and emotions, your internal motivations and inhibitions.")
    print("B) Your actions and the way they effect people, how you navigate the world.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            lunarsway = -1
            return lunarsway
        elif answer == "B" or answer == "b":
            lunarsway = 1
            return lunarsway
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_nineteen(aspect_list, role_list):
    print("19")
    print("What shapes someone the most as a person?")
    print("A) Their family and.or friends.")
    print("B) The way they're treated.")
    print("C) The consequences of their actions.")
    print("D) Their own nature.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            lunarsway = 1
            actpas = 1
            return lunarsway, actpas
        elif answer == "B" or answer == "b":
            lunarsway = 1
            actpas = -1
            return lunarsway, actpas
        elif answer == "C" or answer == "c":
            lunarsway = -1
            actpas = 1
            return lunarsway, actpas
        elif answer == "D" or answer == "d":
            lunarsway = -1
            actpas = -1
            return lunarsway, actpas
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def question_twenty(aspect_list, role_list):
    print("20")
    print("What holds the most information about a person.")
    print("A) Their goals.")
    print("B) Their relationships.")
    print("C) Their secrets.")
    print("D) Their actions.")
    print("E) Their words.")
    print("F) Their thoughts.")
    print("G) Their feelings.")
    print("H) The interaction between all of these.")
    #print(aspect_list)
    valid = False
    while valid == False:
        answer = str(input(""))
        valid = True
        if answer == "A" or answer == "a":
            aspect_list[6] += 1
        elif answer == "B" or answer == "b":
            aspect_list[1] += 1
        elif answer == "C" or answer == "c":
            aspect_list[5] += 1
        elif answer == "D" or answer == "d":
            aspect_list[0] += 1
        elif answer == "E" or answer == "e":
            aspect_list[7] += 1
        elif answer == "F" or answer == "f":
            aspect_list[9] += 1
        elif answer == "G" or answer == "g":
            aspect_list[8] += 1
        elif answer == "H" or answer == "h":
            aspect_list[2] += 1
        else:
            print("Invalid Answer")
            valid = False
    #print(aspect_list)

def tally_up(aspect_list, role_list, aspect_names, lunarsway, actpas, restore, guide, wield, steal, destroy, create, rule, breath, blood, space, time, light, void, life, doom, hope, rage, mind, heart):

    if actpas == 0:
        x = random.randomint(0, 1)
        if x == 0:
            actpas -= 1
        else:
            actpas += 1
    
    aspect = aspect_names[(aspect_list.index((max(aspect_list))))]

    if max(restore, guide, wield, steal, destroy, create, rule) == rule:
        if actpas > 0:
            Class = "Lord"
        elif actpas < 0:
            Class = "Muse"

    elif max(restore, guide, wield, steal, destroy, create, rule) == create:
        if actpas > 0:
            Class = "Witch"
        elif actpas < 0:
            Class = "Heir"

    elif max(restore, guide, wield, steal, destroy, create, rule) == destroy:
        if actpas > 0:
            Class = "Prince"
        elif actpas < 0:
            Class = "Bard"

    elif max(restore, guide, wield, steal, destroy, create, rule) == steal:
        if actpas > 0:
            Class = "Thief"
        elif actpas < 0:
            Class = "Rogue"

    elif max(restore, guide, wield, steal, destroy, create, rule) == wield:
        if actpas > 0:
            Class = "Knight"
        elif actpas < 0:
            Class = "Page"

    elif max(restore, guide, wield, steal, destroy, create, rule) == guide:
        if actpas > 0:
            Class = "Mage"
        elif actpas < 0:
            Class = "Seer"

    elif max(restore, guide, wield, steal, destroy, create, rule) == restore:
        if actpas > 0:
            Class = "Sylph"
        elif actpas < 0:
            Class = "Maid"

    print("Congratulations! You are a(n)", Class, "of", aspect,"!")

    if lunarsway > 0:
        print("Your moon is Prospit")
    elif lunarsway < 0:
        print("Your moon is Derse")
    else:
        x = random.randomint(0, 1)
        if x == 0:
            print("Your moon is Derse")
        else:
            print("Your moon is Prospit")

    #print(aspect_list)
    #print(role_list)
    #print(actpas)
    #print(lunarsway)

def quiz(aspect_list, role_list, aspect_names):
    questions = 20
    question1 = True
    question2 = True
    question3 = True
    question4 = True
    question5 = True
    question6 = True
    question7 = True
    question8 = True
    question9 = True
    question10 = True
    question11 = True
    question12 = True
    question13 = True
    question14 = True
    question15 = True
    question16 = True
    question17 = True
    question18 = True
    question19 = True
    question20 = True

    actpas = 0
    lunarsway = 0

    while questions != 0:
        x = random.randint(1, 20)
        if x == 1:
            #print(question1)
            if question1 == True:
                question_one(aspect_list, role_list)
                questions -= 1
                question1 = False

        elif x == 2:
            #print(question2)
            if question2 == True:
                actpas += question_two(aspect_list, role_list)
                questions -= 1
                question2 = False

        elif x == 3:
            #print(question3)
            if question3 == True:
                question_three(aspect_list, role_list)
                questions -= 1
                question3 = False

        elif x == 4:
            #print(question4)
            if question4 == True:
                question_four(aspect_list, role_list)
                questions -= 1
                question4 = False

        elif x == 5:
            #print(question5)
            if question5 == True:
                question_five(aspect_list, role_list)
                questions -= 1
                question5 = False

        elif x == 6:
            #print(question6)
            if question6 == True:
                question_six(aspect_list, role_list)
                questions -= 1
                question6 = False

        elif x == 7:
            #print(question7)
            if question7 == True:
                question_seven(aspect_list, role_list)
                questions -= 1
                question7 = False

        elif x == 8:
            #print(question8)
            if question8 == True:
                actpas += question_eight(aspect_list, role_list)
                questions -= 1
                question8 = False

        elif x == 9:
            #print(question9)
            if question9 == True:
                question_nine(aspect_list, role_list)
                questions -= 1
                question9 = False

        elif x == 10:
            #print(question10)
            if question10 == True:
                question_ten(aspect_list, role_list)
                questions -= 1
                question10 = False

        elif x == 11:
            #print(question11)
            if question11 == True:
                actpas += question_eleven(aspect_list, role_list)
                questions -= 1
                question11 = False

        elif x == 12:
            #print(question12)
            if question12 == True:
                question_twelve(aspect_list, role_list)
                questions -= 1
                question12 = False

        elif x == 13:
            #print(question13)
            if question13 == True:
                question_thirteen(aspect_list, role_list)
                questions -= 1
                question13 = False

        elif x == 14:
            #print(question14)
            if question14 == True:
                question_fourteen(aspect_list, role_list)
                questions -= 1
                question14 = False

        elif x == 15:
            #print(question15)
            if question15 == True:
                lunarsway += question_fifteen(aspect_list, role_list)
                questions -= 1
                question15 = False

        elif x == 16:
            #print(question16)
            if question16 == True:
                question_sixteen(aspect_list, role_list)
                questions -= 1
                question16 = False

        elif x == 17:
            #print(question17)
            if question17 == True:
                lunarsway += question_seventeen(aspect_list, role_list)
                questions -= 1
                question17 = False

        elif x == 18:
            #print(question18)
            if question18 == True:
                lunarsway += question_eighteen(aspect_list, role_list)
                questions -= 1
                question18 = False

        elif x == 19:
            #print(question19)
            if question19 == True:
                (lunarswayadd, actpasadd) = question_nineteen(aspect_list, role_list)
                actpas += actpasadd
                lunarsway += lunarswayadd
                questions -= 1
                question19 = False

        elif x == 20:
            #print(question20)
            if question20 == True:
                question_twenty(aspect_list, role_list)
                questions -= 1
                question20 = False

                
        breath = aspect_list[0]
        blood = aspect_list[1]
        space = aspect_list[2]
        time = aspect_list[3]
        light = aspect_list[4]
        void = aspect_list[5]
        hope = aspect_list[6]
        rage = aspect_list[7]
        heart = aspect_list[8]
        mind = aspect_list[9]
        life = aspect_list[10]
        doom = aspect_list[11]

        restore = role_list[0]
        guide = role_list[1]
        wield = role_list[2]
        steal = role_list[3]
        destroy = role_list[4]
        create = role_list[5]
        rule = role_list[6]

    tally_up(aspect_list, role_list, aspect_names, lunarsway, actpas, restore, guide, wield, steal, destroy, create, rule, breath, blood, space, time, light, void, life, doom, hope, rage, mind, heart)


quiz(aspect_list, role_list, aspect_names)
