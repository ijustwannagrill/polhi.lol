from pyscript import document, display, window

def injS(string, pos, char):
    string = str(string)
    pos = int(pos)
    char = str(char)
    string = string[:pos] + char + string[pos:]
    return string

def threeLines(diaParam):
    while len(diaParam) < 99:
        diaParam = diaParam + " "
    for i in range(len(diaParam) // 33):
        if i == 0:
            lineSelected = diaParam[0:33]
        elif i > 0:
            lineStart = i * 33
            lineEnd = (i * 33) + 33
            lineSelected = diaParam[lineStart:lineEnd]
        if lineSelected[32] != " ":
            lastSpace = lineSelected.rfind(" ")
            if lastSpace != -1:
                mech = "bicurious"
                while mech == "bicurious":
                    lineSelected = injS(lineSelected, lastSpace, " ")
                    if lineSelected[32] == " ":
                        mech = "gay"
            else:
                lineSelected = injS(lineSelected, 32, "-")
        if i == 0:
            diaParam = lineSelected + diaParam[33:]
        elif i == 1:
            diaParam = diaParam[:33] + lineSelected + diaParam[66:]
        elif i == 2:
            diaParam = diaParam[:66] + lineSelected + diaParam[99:]
    while diaParam[-1:] == " ":
        diaParam = diaParam[0:len(diaParam) - 1]
    if len(diaParam) > 99:
        threeLeftovers = diaParam[99:]
        diaParam = diaParam[:99]
        while diaParam[-1:] == " ":
            diaParam = diaParam[0:len(diaParam) - 1]
        return diaParam + "☺" + threeLeftovers
    else:
        return diaParam

def soymat(chud, soy):
    mech = "bicurious"
    while mech == "bicurious":
        threeDialogue = threeLines(soy)
        if "☺" in threeDialogue:
            fdialogue = threeDialogue[:threeDialogue.find("☺")]
            leftovers = threeDialogue[(threeDialogue.find("☺") + 1):]
            inject.append("whotalking_")
            inject.append(chud)
            inject.append("rundialogue_")
            inject.append(fdialogue)
            inject.append("dialoguenext_")
            soy = leftovers
        else:
            fdialogue = threeDialogue
            inject.append("whotalking_")
            inject.append(chud)
            inject.append("rundialogue_")
            inject.append(fdialogue)
            inject.append("dialoguenext_")
            mech = "gay"

def jakstein(char, dialogue):
    dialogue = str(dialogue)
    charERR = ""
    for i in range(len(dialogue)):
        acceptedChars = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '…', '?', '!', '’', '‘', "'", '"', '“', '”', '-', '~', '[', ']', '(', ')', ':', ';', '%', '$', '@', '`', '#', '+', '=', '*', '/', '\\', ' ']
        if not dialogue[i] in acceptedChars:
            charERR += f"['{dialogue[i]}' at {i}] "
    if charERR != "":
        output_div = document.querySelector("#output")
        output_div.innerText = f"FATAL: {dialogue}: character(s) {charERR} unsupported! Sorry sweaty!"
        global terminated
        terminated = True
        #sys.tracebacklimit = 0
        #raise TypeError(f"{dialogue}: character(s) {charERR} unsupported! Sorry sweaty!")
        #print(f"Jakstein: {dialogue}: Character(s) {charERR} unsupported! Sorry sweaty!")
    else:
        dialogue = dialogue.replace('"', '”')
        dialogue = dialogue.replace("'", "’")
        #print()
        soymat(char, dialogue)

def charJoin(char, pos, onStageCount, yn):
    global toBeAdded
    global posNearLeft
    global posFarLeft
    global posNearRight
    global posFarRight
    char = char.capitalize()
    pos = pos.lower()
    onStageCount = int(onStageCount)
    if onStageCount > 3 and "lastTalked" in globals():
        inject.append("swap_")
        if "Teacher" in posFarLeft and "Teacher" != lastTalked:
            inject.append("Teacher")
            inject.append(char)
            toBeAdded.append("Teacher")
            posFarLeft = char
        elif "Teacher" in posNearLeft:
            inject.append("Teacher")
            inject.append(char)
            toBeAdded.append("Teacher")
            posNearLeft = char
        elif "Teacher" in posNearRight:
            inject.append("Teacher")
            inject.append(char)
            toBeAdded.append("Teacher")
            posNearRight = char
        elif "Teacher" in posFarRight:
            inject.append("Teacher")
            inject.append(char)
            toBeAdded.append("Teacher")
            posFarRight = char

        elif "Bread" in posFarLeft and "Bread" != lastTalked:
            inject.append("Bread")
            inject.append(char)
            toBeAdded.append("Bread")
            posFarLeft = char
        elif "Bread" in posNearLeft:
            inject.append("Bread")
            inject.append(char)
            toBeAdded.append("Bread")
            posNearLeft = char
        elif "Bread" in posNearRight:
            inject.append("Bread")
            inject.append(char)
            toBeAdded.append("Bread")
            posNearRight = char
        elif "Bread" in posFarRight:
            inject.append("Bread")
            inject.append(char)
            toBeAdded.append("Bread")
            posFarRight = char

        elif lastTalked == posNearLeft:
            inject.append(posNearRight)
            inject.append(char)
            toBeAdded.append(posNearRight)
            posNearRight = char
        elif lastTalked == posFarLeft:
            inject.append(posFarRight)
            inject.append(char)
            toBeAdded.append(posFarRight)
            posFarRight = char
        elif lastTalked == posNearRight:
            inject.append(posNearLeft)
            inject.append(char)
            toBeAdded.append(posNearLeft)
            posNearLeft = char
        elif lastTalked == posFarRight:
            inject.append(posFarLeft)
            inject.append(char)
            toBeAdded.append(posFarLeft)
            posFarLeft = char
        if char in toBeAdded:
            toBeAdded.remove(char)
    elif onStageCount > 3 and (not "lastTalked" in globals()):
        toBeAdded.append(char)
    elif onStageCount < 4:
        inject.append("join_")
        inject.append(char)
        if pos == "auto":
            if posNearLeft == "0":
                inject.append("nearleft")
                posNearLeft = char
                onStageCount += 1
            elif posNearRight == "0":
                inject.append("nearright")
                posNearRight = char
                onStageCount += 1
            elif posFarLeft == "0":
                inject.append("farleft")
                posFarLeft = char
                onStageCount += 1
            elif posFarRight == "0":
                inject.append("farright")
                posFarRight = char
                onStageCount += 1
            inject.append(yn)
        elif pos == "nearleft":
            inject.append("nearleft")
            posNearLeft = char
            onStageCount += 1
            inject.append(yn)
        elif pos == "nearright":
            inject.append("nearright")
            posNearRight = char
            onStageCount += 1
            inject.append(yn)
        elif pos == "farleft":
            inject.append("farleft")
            posFarLeft = char
            onStageCount += 1
            inject.append(yn)
        elif pos == "farright":
            inject.append("farright")
            posFarRight = char
            onStageCount += 1
            inject.append(yn)
        if char in toBeAdded:
            toBeAdded.remove(char)
    if yn == "y":
        inject.append("wait_")
        inject.append(".6")
    return onStageCount

def backGround(bkg):
    bkg = bkg.lower()
    if "computer" in bkg:
        inject.append("background_")
        inject.append("bg_computadora_b")
    elif "courtyard" in bkg or "school center" in bkg or \
         "schoolyard" in bkg:
        inject.append("background_")
        inject.append("bg_courtyard1_b")
    elif "chalkboard" in bkg or "front of class" in bkg or \
         "front of the class" in bkg:
        inject.append("background_")
        inject.append("bg_classroom3_b")
    elif "cafe" in bkg or "cafeteria" in bkg or \
         "school cafeteria" in bkg or "lunchroom" in bkg or \
         "school cafe" in bkg or "school lunchroom" in bkg or \
         "lunch room" in bkg or "school lunch room" in bkg or \
         "lunch table" in bkg or "lunch tables" in bkg:
        inject.append("background_")
        inject.append("bg_cafeteria_b")
    elif "school night" in bkg or "school - night" in bkg or \
         "school nighttime" in bkg or "school - nighttime" in bkg:
        inject.append("background_")
        inject.append("bg_school_night_b")
    elif "class" in bkg or "chemistry" in bkg or \
       "school" in bkg or "default" == bkg:
        inject.append("background_")
        inject.append("bg_classroom1_b")
    elif "hallway" in bkg or "corridor" in bkg or \
         "balcony" in bkg:
        inject.append("background_")
        inject.append("bg_hallway1_b")
    elif "library" in bkg or "books" in bkg:
        inject.append("background_")
        inject.append("bg_librarby_b")
    elif "black" in bkg or "none" in bkg or \
         "blank" in bkg or "null" in bkg:
        inject.append("background_")
        inject.append("black")
    elif "white" in bkg or "light" in bkg:
        inject.append("background_")
        inject.append("white")
    elif "mechroom" in bkg or "mech room" in bkg or \
         "mech's room" in bkg or "mech’s room" in bkg or \
         "mechs room" in bkg or "mech bedroom" in bkg or \
         "mech's bedroom" in bkg or "mech’s bedroom" in bkg or \
         "mechs bedroom" in bkg:
        inject.append("background_")
        inject.append("bg_mechroom1_b")
    elif "bedroom night" in bkg or "moss's bedroom night" in bkg or \
         "moss’s bedroom night" in bkg or "moss’ bedroom night" in bkg or \
         "moss' bedroom night" in bkg or "moss bedroom night" in bkg or \
         "bedroom - night" in bkg or "moss's bedroom - night" in bkg or \
         "moss’s bedroom - night" in bkg or "moss’ bedroom - night" in bkg or \
         "moss' bedroom - night" in bkg or "moss bedroom - night" in bkg:
        inject.append("background_")
        inject.append("bg_bedroom_night_b")
    elif "bedroom" in bkg or "moss's bedroom" in bkg or \
         "moss’s bedroom" in bkg or "moss’ bedroom" in bkg or \
         "moss' bedroom" in bkg or "moss bedroom" in bkg:
        inject.append("background_")
        inject.append("bg_bedroom_b")
    elif "porch" in bkg or "mech porch" in bkg or \
         "mech's porch" in bkg or "mech’s porch" in bkg or\
         "mechs porch" in bkg:
        inject.append("background_")
        inject.append("bg_mechporch_b")
    elif "mechhouse" in bkg or "mech house" in bkg or \
         "mech's house" in bkg or "mech’s house" in bkg or\
         "mechs house" in bkg:
        inject.append("background_")
        inject.append("bg_mechstairs_b")
    elif "tree" in bkg or "mitsuu" in bkg or \
         "mitsuu tree" in bkg or "alone" in bkg:
        inject.append("background_")
        inject.append("bg_conflicttree_b")
    elif "store" in bkg or "shoestore" in bkg or \
         "shoe store" in bkg or "department store" in bkg:
        inject.append("background_")
        inject.append("bg_shoesahahyes1")
    elif "foodcourt" in bkg or "food court" in bkg or \
         "mall food court" in bkg:
        inject.append("background_")
        inject.append("bg_foodcourt")
    elif "mall" in bkg or "plaza" in bkg or \
         "the mall" in bkg:
        inject.append("background_")
        inject.append("bg_mall")
    elif "kiss" in bkg:
        inject.append("background_")
        inject.append("justtwobros")
    elif "cashier" in bkg or "cash register" in bkg or \
         "checkout" in bkg:
        inject.append("background_")
        inject.append("bg_shoesahahyes2")
    elif "ice cream" in bkg or "icecream" in bkg:
        inject.append("background_")
        inject.append("bg_icecreamshop")
    elif "text" in bkg or "messages" in bkg:
        inject.append("background_")
        inject.append("tecksts")
    elif "corner" in bkg:
        inject.append("background_")
        inject.append("bg_corner_b")
    else:
        output_div = document.querySelector("#output")
        output_div.innerText += f"WARNING: Unknown background {bkg}! Ignoring..." + "\n"

def music(track):
    track = track.lower()
    if "main theme" in track or "maintheme" in track or \
       "the start of a greatest journey" in track:
        inject.append("maintheme")
    elif "default" == track or "1" in track or \
       "let it sit" in track:
        inject.append("bgm1")
    elif "let it sit 2" in track or "2" in track or \
       "let it sit (super ultra omega ball blasting pussy remix)" in track:
        inject.append("bgm2")
    elif "mitsuu" in track or "mitsuu's theme" in track or \
       "shady" in track or "mitsuu’s theme" in track:
        inject.append("mitsuu")
    elif "drums" in track or "drums… just drums" in track or \
       "drums... just drums" in track:
        inject.append("drums")
    elif "erwin" in track or "erwin's theme" in track or \
       "hot jazz" in track or "erwin’s theme" in track:
        inject.append("erwin")
    elif "mech" in track or "mech's theme" in track or \
       "mechanicalphoenix" in track or "mech’s theme" in track:
        inject.append("mech")
    elif "sincerity" in track or "mech's reflection" in track or \
       "incel mech" in track or "mech’s reflection" in track:
        inject.append("Sincerity")
    elif "tension" in track or "tense" in track or \
       "stress" in track:
        inject.append("tension")
    elif "justice" in track or "fuck mitsuu" in track or \
       "busting mitsuu" in track:
        inject.append("justice")
    elif "mitsuu date" in track or "cucking erwin" in track or \
       "sushihouse" in track:
        inject.append("sushihouse")
    elif "true ending" in track or "trueending" in track or \
       "reflection" in track:
        inject.append("Reflection")
    elif "sad" in track or "bad ending" in track or \
       "spingle" in track:
        inject.append("spingle")
    elif "good ending" in track or "mech ending" in track or \
       "cucked" in track:
        inject.append("cucked")
    elif "mute" in track or "silence" in track or \
       "none" in track or "clear" in track:
        inject.append("")
    else:
        output_div = document.querySelector("#output")
        output_div.innerText += f"WARNING: Unknown track argument {track}! Ignoring..." + "\n"

def soyFaceLookup(char, soyFace):
    soyFace = soyFace.lower()
    char = char.capitalize()
    if char == "Mech":
        if soyFace == "blush" or soyFace == "blushing" or \
           soyFace == "flirty" or soyFace == "flushed" or \
           soyFace == "excited" or soyFace == "happy" or \
           soyFace == "flirting":
            inject.append("mech_blush")
        elif soyFace == "cry" or soyFace == "crying" or \
           soyFace == "teary" or soyFace == "weeping" or \
           soyFace == "spingle":
            inject.append("mech_crying")
        elif soyFace == "smug" or soyFace == "douche" or \
           soyFace == "douchebag" or soyFace == "annoying" or \
           soyFace == "arrogant" or soyFace == "prideful":
            inject.append("mech_dbag")
        elif soyFace == "evil" or soyFace == "shady" or \
           soyFace == "disappointed" or soyFace == "mean":
            inject.append("mech_disappointed")
        elif soyFace == "embarrassed" or soyFace == "suspicious" or \
           soyFace == "embarassed" or soyFace == "angry":
            inject.append("mech_embarassed")
        elif soyFace == "frustrated" or soyFace == "stressed" or \
           soyFace == "annoyed" or soyFace == "pissed":
            inject.append("mech_frustrated")
        elif soyFace == "guilty" or soyFace == "nervous" or \
           soyFace == "sweating" or soyFace == "sweaty" or \
           soyFace == "uncomfortable" or soyFace == "awkward" or \
           soyFace == "humiliated" or soyFace == "scared" or \
           soyFace == "terrified" or soyFace == "concerned":
            inject.append("mech_guilty")
        elif soyFace == "intrigued" or soyFace == "neutral" or \
           soyFace == "curious" or soyFace == "thinking" or \
           soyFace == "thoughtful" or soyFace == "thinks" or \
           soyFace == "content" or soyFace == "fine" or \
           soyFace == "aloof" or soyFace == "confused":
            inject.append("mech_intrigued")
        elif soyFace == "shocked" or soyFace == "surprised" or \
           soyFace == "flabbergasted" or soyFace == "alerted":
            inject.append("mech_shocked")
        elif soyFace == "uwu" or soyFace == "gay":
            inject.append("mech_uwu")
        else:
            inject.append("mech_intrigued")
            output_div = document.querySelector("#output")
            output_div.innerText += f"WARNING: Unknown emotion {soyFace} for Mech! Using default..." + "\n"
            
    elif char == "Moss":
        if soyFace == "blush" or soyFace == "blushing" or \
           soyFace == "flirty" or soyFace == "flushed" or \
           soyFace == "flirting":
            inject.append("moss_blush")
        elif soyFace == "cry" or soyFace == "crying" or \
           soyFace == "teary" or soyFace == "weeping" or \
           soyFace == "embarrassed" or soyFace == "embarassed" or \
           soyFace == "concerned" or soyFace == "terrified" or \
           soyFace == "guilty" or soyFace == "nervous" or \
           soyFace == "sweating" or soyFace == "sweaty" or \
           soyFace == "uncomfortable" or soyFace == "awkward" or \
           soyFace == "humiliated" or soyFace == "scared" or \
           soyFace == "spingle" or soyFace == "confused":
            inject.append("moss_concerned")
        elif soyFace == "smug" or soyFace == "douche" or \
           soyFace == "douchebag" or soyFace == "annoying" or \
           soyFace == "arrogant" or soyFace == "prideful" or \
           soyFace == "silly" or soyFace == "goofy" or \
           soyFace == "trollface" or soyFace == "excited" or \
           soyFace == "happy":
            inject.append("moss_silly")
        elif soyFace == "evil" or soyFace == "shady" or \
           soyFace == "disappointed" or soyFace == "mean" or \
           soyFace == "angry":
            inject.append("moss_angry")
        elif soyFace == "frustrated" or soyFace == "stressed" or \
           soyFace == "annoyed" or soyFace == "pissed":
            inject.append("moss_annoyed")
        elif soyFace == "intrigued" or soyFace == "neutral" or \
           soyFace == "curious" or soyFace == "thinking" or \
           soyFace == "thoughtful" or soyFace == "thinks" or \
           soyFace == "content" or soyFace == "fine" or \
           soyFace == "aloof":
            inject.append("moss_neutral")
        elif soyFace == "shocked" or soyFace == "surprised" or \
           soyFace == "flabbergasted" or soyFace == "alerted":
            inject.append("moss_shocked")
        else:
            inject.append("moss_neutral")
            output_div = document.querySelector("#output")
            output_div.innerText += f"WARNING: Unknown emotion {soyFace} for Moss! Using default..." + "\n"
            
    elif char == "Mitsuu":
        if soyFace == "blush" or soyFace == "blushing" or \
           soyFace == "flirty" or soyFace == "flushed" or \
           soyFace == "flirting":
            inject.append("mitsuu_blush")
        elif soyFace == "intrigued" or soyFace == "annoyed" or \
           soyFace == "curious" or soyFace == "thinking" or \
           soyFace == "thoughtful" or soyFace == "thinks" or \
           soyFace == "attentive" or soyFace == "irritated" or \
           soyFace == "confused":
            inject.append("mitsuu_attentive")
        elif soyFace == "cry" or soyFace == "crying" or \
           soyFace == "teary" or soyFace == "weeping" or \
           soyFace == "spingle":
            inject.append("mitsuu_crying")
        elif soyFace == "evil" or soyFace == "shady" or \
           soyFace == "disappointed" or soyFace == "mean":
            inject.append("mitsuu_disappointed")
        elif soyFace == "excited":
            inject.append("mitsuu_excited")
        elif soyFace == "guilty" or soyFace == "nervous" or \
           soyFace == "sweating" or soyFace == "sweaty" or \
           soyFace == "uncomfortable" or soyFace == "awkward" or \
           soyFace == "humiliated" or soyFace == "scared" or \
           soyFace == "terrified" or soyFace == "embarassed" or \
           soyFace == "embarrassed" or soyFace == "alerted" or \
           soyFace == "shocked" or soyFace == "surprised" or \
           soyFace == "flabbergasted":
            inject.append("mitsuu_guilty")
        elif soyFace == "happy" or soyFace == "smiling" or \
           soyFace == "cheerful":
            inject.append("mitsuu_happy")
        elif soyFace == "neutral" or soyFace == "aloof" or \
           soyFace == "content" or soyFace == "fine":
            inject.append("mitsuu_neutral")
        elif soyFace == "sad" or soyFace == "disheartened" or \
           soyFace == "frowning":
            inject.append("mitsuu_sad")
        elif soyFace == "smug" or soyFace == "douche" or \
           soyFace == "douchebag" or soyFace == "annoying" or \
           soyFace == "arrogant" or soyFace == "prideful":
            inject.append("mitsuu_smug")
        else:
            inject.append("mitsuu_neutral")
            output_div = document.querySelector("#output")
            output_div.innerText += f"WARNING: Unknown emotion {soyFace} for Mitsuu! Using default..." + "\n"
            
    elif char == "Erwin":
        if soyFace == "angry" or soyFace == "pissed" or \
           soyFace == "pissy" or soyFace == "fuming" or \
           soyFace == "enraged" or soyFace == "annoyed":
            inject.append("erwin_angry")
        elif soyFace == "blush" or soyFace == "blushing" or \
           soyFace == "flushed":
            inject.append("erwin_blush")
        elif soyFace == "uwu" or soyFace == "gay" or \
             soyFace == "owo" or soyFace == "douche" or \
           soyFace == "douchebag" or soyFace == "annoying" or \
           soyFace == "arrogant" or soyFace == "prideful" or \
           soyFace == "smug" or soyFace == "flirty" or \
           soyFace == "flirting":
            inject.append("erwin_owo")
        elif soyFace == "intrigued" or soyFace == "neutral" or \
           soyFace == "curious" or soyFace == "thinking" or \
           soyFace == "thoughtful" or soyFace == "thinks" or \
           soyFace == "content" or soyFace == "fine" or \
           soyFace == "aloof" or soyFace == "confused":
            inject.append("erwin_confused")
        elif soyFace == "evil" or soyFace == "shady" or \
           soyFace == "disappointed" or soyFace == "mean":
            inject.append("erwin_disappointed")
        elif soyFace == "embarrassed" or soyFace == "embarassed" or \
           soyFace == "concerned" or soyFace == "terrified" or \
           soyFace == "guilty" or soyFace == "nervous" or \
           soyFace == "sweating" or soyFace == "sweaty" or \
           soyFace == "uncomfortable" or soyFace == "awkward" or \
           soyFace == "humiliated" or soyFace == "scared" or \
           soyFace == "shocked" or soyFace == "surprised" or \
           soyFace == "flabbergasted" or soyFace == "alerted":
            inject.append("erwin_embarassed")
        elif soyFace == "happy" or soyFace == "smiling" or \
           soyFace == "cheerful":
            inject.append("erwin_happy")
        elif soyFace == "sad" or soyFace == "disheartened" or \
           soyFace == "frowning" or soyFace == "spingle" or \
           soyFace == "cry" or soyFace == "crying" or \
           soyFace == "teary" or soyFace == "weeping":
            inject.append("erwin_sad")
        elif soyFace == "red" or soyFace == "baka":
            inject.append("erwin_baka")
        else:
            inject.append("erwin_confused")
            output_div = document.querySelector("#output")
            output_div.innerText += f"WARNING: Unknown emotion {soyFace} for Erwin! Using default..." + "\n"

def charEmotion(char, soyLine):
    global toBeAdded
    global onStageCount
    if soyLine[0:5].capitalize() == "Mech " and ("):" in soyLine.split()[1] and \
                                                 "(" in soyLine.split()[1]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find("):")
        jakStart = soyEnd + soyLine.find(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Mech")
        soyFaceLookup("Mech", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
        if soyLine[(jakStart - 1)] == " ":
            jakstein("Mech", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Mech", soyLine[(jakStart - 1):-1])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
    elif soyLine[0:5].capitalize() == "Mech " and \
         (")" in soyLine.split()[1] and ":" in soyLine.split()[2]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find(")")
        jakStart = len(soyLine.split()[0]) + len(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Mech")
        soyFaceLookup("Mech", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Mech", soyLine[(soyLine.find(" " + soyLine.split()[3]) + 1):-1])
        else:
            jakstein("Mech", soyLine[jakStart:-1])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
    elif soyLine[0:4].capitalize() == "Mech" and ("):" in soyLine.split()[0] and \
                                                  "(" in soyLine.split()[0]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find("):")
        inject.append("emotion_")
        inject.append("Mech")
        soyFaceLookup("Mech", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
        if soyLine[(soyEnd + 2)] == " ":
            jakstein("Mech", soyLine[(soyLine.find(" " + soyLine.split()[1]) + 1):-1])
        else:
            jakstein("Mech", soyLine[(soyEnd + 2):-1])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
    elif soyLine[0:4].capitalize() == "Mech" and \
         ("(" in soyLine.split()[0] and ")" in soyLine.split()[0] and \
          ":" in soyLine.split()[1]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find(")")
        jakStart = soyLine.find(soyLine.split()[1]) + 1
        inject.append("emotion_")
        inject.append("Mech")
        soyFaceLookup("Mech", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Mech", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Mech", soyLine[jakStart:-1])
        if "Mech" in toBeAdded:
            onStageCount = charJoin("Mech", "auto", onStageCount, "y")

    elif soyLine[0:5].capitalize() == "Moss " and ("):" in soyLine.split()[1] and \
                                                 "(" in soyLine.split()[1]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find("):")
        jakStart = soyEnd + soyLine.find(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Moss")
        soyFaceLookup("Moss", soyTarget[(soyStart + 1):(soyEnd)])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
        if soyLine[(jakStart - 1)] == " ":
            jakstein("Moss", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Moss", soyLine[(jakStart - 1):-1])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
    elif soyLine[0:5].capitalize() == "Moss " and \
         (")" in soyLine.split()[1] and ":" in soyLine.split()[2]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find(")")
        jakStart = len(soyLine.split()[0]) + len(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Moss")
        soyFaceLookup("Moss", soyTarget[(soyStart + 1):(soyEnd)])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Moss", soyLine[(soyLine.find(" " + soyLine.split()[3]) + 1):-1])
        else:
            jakstein("Moss", soyLine[jakStart:-1])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
    elif soyLine[0:4].capitalize() == "Moss" and ("):" in soyLine.split()[0] and \
                                                  "(" in soyLine.split()[0]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find("):")
        inject.append("emotion_")
        inject.append("Moss")
        soyFaceLookup("Moss", soyTarget[(soyStart + 1):(soyEnd)])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
        if soyLine[(soyEnd + 2)] == " ":
            jakstein("Moss", soyLine[(soyLine.find(" " + soyLine.split()[1]) + 1):-1])
        else:
            jakstein("Moss", soyLine[(soyEnd + 2):-1])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
    elif soyLine[0:4].capitalize() == "Moss" and \
         ("(" in soyLine.split()[0] and ")" in soyLine.split()[0] and \
          ":" in soyLine.split()[1]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find(")")
        jakStart = soyLine.find(soyLine.split()[1]) + 1
        inject.append("emotion_")
        inject.append("Moss")
        soyFaceLookup("Moss", soyTarget[(soyStart + 1):(soyEnd)])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Moss", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Moss", soyLine[jakStart:-1])
        if "Moss" in toBeAdded:
            onStageCount = charJoin("Moss", "auto", onStageCount, "y")

    elif soyLine[0:7].capitalize() == "Mitsuu " and ("):" in soyLine.split()[1] and \
                                                 "(" in soyLine.split()[1]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find("):")
        jakStart = soyEnd + soyLine.find(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Mitsuu")
        soyFaceLookup("Mitsuu", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
        if soyLine[(jakStart - 1)] == " ":
            jakstein("Mitsuu", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Mitsuu", soyLine[(jakStart - 1):-1])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
    elif soyLine[0:7].capitalize() == "Mitsuu " and \
         (")" in soyLine.split()[1] and ":" in soyLine.split()[2]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find(")")
        jakStart = len(soyLine.split()[0]) + len(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Mitsuu")
        soyFaceLookup("Mitsuu", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Mitsuu", soyLine[(soyLine.find(" " + soyLine.split()[3]) + 1):-1])
        else:
            jakstein("Mitsuu", soyLine[jakStart:-1])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
    elif soyLine[0:6].capitalize() == "Mitsuu" and ("):" in soyLine.split()[0] and \
                                                  "(" in soyLine.split()[0]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find("):")
        inject.append("emotion_")
        inject.append("Mitsuu")
        soyFaceLookup("Mitsuu", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
        if soyLine[(soyEnd + 2)] == " ":
            jakstein("Mitsuu", soyLine[(soyLine.find(" " + soyLine.split()[1]) + 1):-1])
        else:
            jakstein("Mitsuu", soyLine[(soyEnd + 2):-1])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
    elif soyLine[0:6].capitalize() == "Mitsuu" and \
         ("(" in soyLine.split()[0] and ")" in soyLine.split()[0] and \
          ":" in soyLine.split()[1]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find(")")
        jakStart = soyLine.find(soyLine.split()[1]) + 1
        inject.append("emotion_")
        inject.append("Mitsuu")
        soyFaceLookup("Mitsuu", soyTarget[(soyStart + 1):(soyEnd)])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Mitsuu", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Mitsuu", soyLine[jakStart:-1])
        if "Mitsuu" in toBeAdded:
            onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")

    elif soyLine[0:6].capitalize() == "Erwin " and ("):" in soyLine.split()[1] and \
                                                 "(" in soyLine.split()[1]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find("):")
        jakStart = soyEnd + soyLine.find(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Erwin")
        soyFaceLookup("Erwin", soyTarget[(soyStart + 1):(soyEnd)])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
        if soyLine[(jakStart - 1)] == " ":
            jakstein("Erwin", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Erwin", soyLine[(jakStart - 1):-1])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
    elif soyLine[0:6].capitalize() == "Erwin " and \
         (")" in soyLine.split()[1] and ":" in soyLine.split()[2]):
        soyTarget = soyLine.split()[1]
        soyStart = soyLine.split()[1].find("(")
        soyEnd = soyLine.split()[1].find(")")
        jakStart = len(soyLine.split()[0]) + len(soyLine.split()[1]) + 3
        inject.append("emotion_")
        inject.append("Erwin")
        soyFaceLookup("Erwin", soyTarget[(soyStart + 1):(soyEnd)])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Erwin", soyLine[(soyLine.find(" " + soyLine.split()[3]) + 1):-1])
        else:
            jakstein("Erwin", soyLine[jakStart:-1])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
    elif soyLine[0:5].capitalize() == "Erwin" and ("):" in soyLine.split()[0] and \
                                                  "(" in soyLine.split()[0]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find("):")
        inject.append("emotion_")
        inject.append("Erwin")
        soyFaceLookup("Erwin", soyTarget[(soyStart + 1):(soyEnd)])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
        if soyLine[(soyEnd + 2)] == " ":
            jakstein("Erwin", soyLine[(soyLine.find(" " + soyLine.split()[1]) + 1):-1])
        else:
            jakstein("Erwin", soyLine[(soyEnd + 2):-1])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
    elif soyLine[0:5].capitalize() == "Erwin" and \
         ("(" in soyLine.split()[0] and ")" in soyLine.split()[0] and \
          ":" in soyLine.split()[1]):
        soyTarget = soyLine.split()[0]
        soyStart = soyLine.split()[0].find("(")
        soyEnd = soyLine.split()[0].find(")")
        jakStart = soyLine.find(soyLine.split()[1]) + 1
        inject.append("emotion_")
        inject.append("Erwin")
        soyFaceLookup("Erwin", soyTarget[(soyStart + 1):(soyEnd)])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
        if soyLine[jakStart] == " ":
            jakstein("Erwin", soyLine[(soyLine.find(" " + soyLine.split()[2]) + 1):-1])
        else:
            jakstein("Erwin", soyLine[jakStart:-1])
        if "Erwin" in toBeAdded:
            onStageCount = charJoin("Erwin", "auto", onStageCount, "y")

def specPos(char, posLine, onStageCount):
    char = char.capitalize()
    twordCheck = ['FAR', 'NEAR']
    posList = ['FARLEFT', 'FAR LEFT', 'NEARLEFT', 'NEAR LEFT', 'NEARRIGHT', 'NEAR RIGHT', 'FARRIGHT', 'FAR RIGHT']
    if (not (posLine.split()[2].upper() in posList)) and (not (posLine.split()[2].upper() in twordCheck)):
        output_div = document.querySelector("#output")
        output_div.innerText = f"FATAL: {posLine}: {posLine.split()[2]}: position invalid!"
        global terminated
        terminated = True
        #sys.tracebacklimit = 0
        #raise TypeError(f"{posLine}: {posLine.split()[2]}: position invalid!")
    elif posLine.split()[2].upper() == "FARLEFT":
        onStageCount = charJoin(char, "farleft", onStageCount, "y")
    elif posLine.split()[2].upper() == "NEARLEFT":
        onStageCount = charJoin(char, "nearleft", onStageCount, "y")
    elif posLine.split()[2].upper() == "NEARRIGHT":
        onStageCount = charJoin(char, "nearright", onStageCount, "y")
    elif posLine.split()[2].upper() == "FARRIGHT":
        onStageCount = charJoin(char, "farright", onStageCount, "y")

    elif not posLine.split()[2].upper() + posLine.split()[3].upper() in posList:
        output_div = document.querySelector("#output")
        output_div.innerText = f"FATAL: {posLine}: position invalid!"
        terminated = True
        #sys.tracebacklimit = 0
        #raise TypeError(f"{posLine}: {posLine.split()[2] + " " + posLine.split()[3]}: position invalid!")
    elif posLine.split()[2].upper() + posLine.split()[3].upper() == "FARLEFT":
        onStageCount = charJoin(char, "farleft", onStageCount, "y")
    elif posLine.split()[2].upper() + posLine.split()[3].upper() == "NEARLEFT":
        onStageCount = charJoin(char, "nearleft", onStageCount, "y")
    elif posLine.split()[2].upper() + posLine.split()[3].upper() == "NEARRIGHT":
        onStageCount = charJoin(char, "nearright", onStageCount, "y")
    elif posLine.split()[2].upper() + posLine.split()[3].upper() == "FARRIGHT":
        onStageCount = charJoin(char, "farright", onStageCount, "y")
    return onStageCount

def scanUnCalled(sceneNum):
    global toBeAdded
    global posFarLeft
    global posNearLeft
    global posNearRight
    global posFarRight
    global modTitle
    global modAuthor
    global modDesc
    posFarLeft = "0"
    posNearLeft = "0"
    posNearRight = "0"
    posFarRight = "0"
    toBeAdded = []
    preJoin = []
    charCalled = []
    jumpToScene = sceneNum
    backGroundFound = 0
    for i, line in enumerate(BoyMOD):
        if line != "" and line[-1] != "\n":
            line += "\n"
        if line == "" or line == "\n":
            pass

        elif line[0] == "<":
            pass
        elif line[0:7].upper() == ">TITLE ":
            modTitle = line[7:-1]
        elif line[0:8].upper() == ">AUTHOR ":
            modAuthor = line[8:-1]
        elif line[0:6].upper() == ">DESC ":
            modDesc = line[6:-1]
        elif line[0:13].upper() == ">DESCRIPTION ":
            modDesc = line[13:-1]

        elif jumpToScene == -1 and line[1:7].upper() == "SCENE ":
            pass
        elif jumpToScene == -1 and line[1:13].upper() == "START SCENE ":
            pass
        elif line[1:7].upper() == "SCENE ":
            if jumpToScene == line.split()[1]:
                jumpToScene = -1
        elif line[1:13].upper() == "START SCENE ":
            if jumpToScene == line.split()[2]:
                jumpToScene = -1
        elif jumpToScene != -1:
            pass

        elif line[0] == ">":
            if (line[1:6].upper() == "MECH " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MECH"):
                if not "Mech" in charCalled:
                    if "Mech" in preJoin:
                        preJoin.remove("Mech")
                    charCalled.append("Mech")
            elif (line[1:6].upper() == "MOSS " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MOSS"):
                if not "Moss" in charCalled:
                    if "Moss" in preJoin:
                        preJoin.remove("Moss")
                    charCalled.append("Moss")
            elif (line[1:8].upper() == "MITSUU " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MITSUU"):
                if not "Mitsuu" in charCalled:
                    if "Mitsuu" in preJoin:
                        preJoin.remove("Mitsuu")
                    charCalled.append("Mitsuu")
            elif (line[1:7].upper() == "ERWIN " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "ERWIN"):
                if not "Erwin" in charCalled:
                    if "Erwin" in preJoin:
                        preJoin.remove("Erwin")
                    charCalled.append("Erwin")
            elif (line[1:9].upper() == "TEACHER " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "TEACHER"):
                if not "Teacher" in charCalled:
                    if "Teacher" in preJoin:
                        preJoin.remove("Teacher")
                    charCalled.append("Teacher")
            elif (line[1:7].upper() == "BREAD " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "BREAD"):
                if not "Bread" in charCalled:
                    if "Bread" in preJoin:
                        preJoin.remove("Bread")
                    charCalled.append("Bread")
            elif line[1:7].upper() == "BREAD ":
                if (line[1:13].upper() == "BREAD EATER " and line.split()[2].upper() == "ENTERS") or \
                   (line[1:7].upper() == "ENTER " and \
                    line.split()[1].upper() + line.split()[2].upper() == "BREADEATER"):
                    if not "Bread" in charCalled:
                        if "Bread" in preJoin:
                            preJoin.remove("Bread")
                        charCalled.append("Bread")

            elif line[1:6].upper() == "INT. " or line[1:6].upper() == "EXT. ":
                if backGroundFound == 0:
                    preJoin.append(line[6:-1])
                    backGroundFound = 1
            elif line[1:10].upper() == "INTERIOR " or line[1:10].upper() == "EXTERIOR " or \
                 line[1:10].upper() == "BACKDROP ":
                if backGroundFound == 0:
                    preJoin.append(line[10:-1])
                    backGroundFound = 1
            elif line[1:12].upper() == "BACKGROUND ":
                if backGroundFound == 0:
                    preJoin.append(line[12:-1])
                    backGroundFound = 1

            elif line[1:5].upper() == "JUMP " or line[1:7].upper() == "GO TO " or \
                 line[1:6].upper() == "GOTO ":
                break
            elif line[1:12].upper() == "NOAUTOJOIN " or line[1:14].upper() == "NO AUTO JOIN " or \
                 line[1:13].upper() == "NO AUTOJOIN ":
                preJoin = []
                charCalled = []
                toBeAdded = []
                break

        elif (line[0:5].upper() == "MECH " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:4].upper() == "MECH" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:4].upper() == "MECH" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Mech" in preJoin) and (not "Mech" in charCalled):
                preJoin.append("Mech")
        elif (line[0:5].upper() == "MOSS " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:4].upper() == "MOSS" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:4].upper() == "MOSS" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Moss" in preJoin) and (not "Mech" in charCalled):
                preJoin.append("Moss")
        elif (line[0:7].upper() == "MITSUU " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:6].upper() == "MITSUU" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:6].upper() == "MITSUU" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Mitsuu" in preJoin) and (not "Mitsuu" in charCalled):
                preJoin.append("Mitsuu")
        elif (line[0:6].upper() == "ERWIN " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:5].upper() == "ERWIN" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:5].upper() == "ERWIN" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Erwin" in preJoin) and (not "Erwin" in charCalled):
                preJoin.append("Erwin")
        elif (line[0:8].upper() == "TEACHER " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:7].upper() == "TEACHER" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:7].upper() == "TEACHER" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Teacher" in preJoin) and (not "Teacher" in charCalled):
                preJoin.append("Teacher")
        elif (line[0:6].upper() == "BREAD " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:5].upper() == "BREAD" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:5].upper() == "BREAD" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if (not "Bread" in preJoin) and (not "Bread" in charCalled):
                preJoin.append("Bread")
        
        elif (line[0:5].upper() == "MECH:") or \
           (line.split()[0].upper() == "MECH" and ":" in line.split()[1].upper()):
            if (not "Mech" in preJoin) and (not "Mech" in charCalled):
                preJoin.append("Mech")
        elif (line[0:5].upper() == "MOSS:") or \
           (line.split()[0].upper() == "MOSS" and ":" in line.split()[1].upper()):
            if (not "Moss" in preJoin) and (not "Moss" in charCalled):
                preJoin.append("Moss")
        elif (line[0:7].upper() == "MITSUU:") or \
           (line.split()[0].upper() == "MITSUU" and ":" in line.split()[1].upper()):
            if (not "Mitsuu" in preJoin) and (not "Mitsuu" in charCalled):
                preJoin.append("Mitsuu")
        elif (line[0:6].upper() == "ERWIN:") or \
           (line.split()[0].upper() == "ERWIN" and ":" in line.split()[1].upper()):
            if (not "Erwin" in preJoin) and (not "Erwin" in charCalled):
                preJoin.append("Erwin")
        elif (line[0:8].upper() == "TEACHER:") or \
           (line.split()[0].upper() == "TEACHER" and ":" in line.split()[1].upper()):
            if (not "Teacher" in preJoin) and (not "Teacher" in charCalled):
                preJoin.append("Teacher")
        elif (line[0:6].upper() == "BREAD:") or \
           (line.split()[0].upper() == "BREAD" and ":" in line.split()[1].upper() and \
            (not "*" in line.split()[1].upper())):
            if (not "Bread" in preJoin) and (not "Bread" in charCalled):
                preJoin.append("Bread")
        elif line[0:6].upper() == "BREAD " and 3 <= len(line.split()):
            if ((line.split()[0].upper() + line.split()[1].upper()) == "BREADEATER:") or \
               ((line.split()[0].upper() + line.split()[1].upper()) == "BREADEATER" and \
               ":" in line.split()[2].upper()):
                if (not "Bread" in preJoin) and (not "Bread" in charCalled):
                    preJoin.append("Bread")

        elif line[0:6].upper() == "BREAD " and 4 <= len(line.split()):
            if (line[0:12].upper() == "BREAD EATER " and ("):" in line.split()[2] or \
                 (")" in line.split()[2] and ":" in line.split()[3]))) or \
                 (line[0:11].upper() == "BREAD EATER" and ("):" in line.split()[1] and \
                                                  "(" in line.split()[1])) or \
                 (line[0:11].upper() == "BREAD EATER" and ("(" in line.split()[1] and \
                                                   ")" in line.split()[1] and \
                                                   ":" in line.split()[2])):
                if (not "Bread" in preJoin) and (not "Bread" in charCalled):
                    preJoin.append("Bread")

    if backGroundFound == 0:
        preJoin.append("class")

    return preJoin

bMVersion = "1.0"
print(f"BoyMODder - v{bMVersion} - Written by Terry A. Davis 2017")

####################### COMPILER ###########################################################

def compile_boymod(event):
    print("Compiling BoyMOD file...")

    global BoyMOD
    global inject
    global onStageCount
    global toBeAdded
    global posFarLeft
    global posNearLeft
    global posNearRight
    global posFarRight
    global ignoreBack
    global jumpToScene
    global preJoin
    global terminated
    global lastTalked
    

    input_text = document.querySelector("#input")
    BoyMOD = input_text.value.split("\n")

    output_div = document.querySelector("#output")
    output_div.innerText = ""
    output_div.style= ""

    inject = []

    terminated = False
    onStageCount = 0
    toBeAdded = 0
    posFarLeft = "0"
    posNearLeft = "0"
    posNearRight = "0"
    posFarRight = "0"
    ignoreBack = "0"
    jumpToScene = -1
    inject.append("leave_")
    inject.append("all")
    inject.append("n")
    inject.append("")
    inject.append("emotion_")
    inject.append("Mech")
    inject.append("mech_intrigued")
    inject.append("emotion_")
    inject.append("Moss")
    inject.append("moss_neutral")
    inject.append("emotion_")
    inject.append("Mitsuu")
    inject.append("mitsuu_neutral")
    inject.append("emotion_")
    inject.append("Erwin")
    inject.append("erwin_confused")
    preJoin = scanUnCalled(jumpToScene)
    for i in range(len(preJoin)):
        if preJoin[i] == "Mech" or preJoin[i] == "Moss" or preJoin[i] == "Mitsuu" or \
           preJoin[i] == "Erwin" or preJoin[i] == "Bread" or preJoin[i] == "Teacher":
            onStageCount = charJoin(preJoin[i], "auto", onStageCount, "n")
        else:
            backGround(preJoin[i])
            ignoreBack = preJoin[i]
    inject.append("wait_")
    inject.append(".205")
    for i, line in enumerate(BoyMOD): # Always keep this line of ifs and elifs in order!
        if line != "" and line[-1] != "\n":
            line += "\n"
        if line == "" or line == "\n":
            pass

        elif line[0] == "<":
            pass
        elif line[0:6].upper() == ">TITLE":
                pass
        elif line[0:7].upper() == ">AUTHOR":
                pass
        elif line[0:5].upper() == ">DESC":
                pass
        elif jumpToScene == -1 and line[1:7].upper() == "SCENE ":
            pass
        elif jumpToScene == -1 and line[1:13].upper() == "START SCENE ":
            pass
        elif line[1:7].upper() == "SCENE ":
            if jumpToScene == line.split()[1]:
                preJoin = scanUnCalled(jumpToScene)
                for i in range(len(preJoin)):
                    if preJoin[i] == "Mech" or preJoin[i] == "Moss" or preJoin[i] == "Mitsuu" or \
                       preJoin[i] == "Erwin" or preJoin[i] == "Bread" or preJoin[i] == "Teacher":
                        onStageCount = charJoin(preJoin[i], "auto", onStageCount, "n")
                    else:
                        backGround(preJoin[i])
                        ignoreBack = preJoin[i]
                jumpToScene = -1
                inject.append("wait_")
                inject.append(".205")
        elif line[1:13].upper() == "START SCENE ":
            if jumpToScene == line.split()[2]:
                preJoin = scanUnCalled(jumpToScene)
                for i in range(len(preJoin)):
                    if preJoin[i] == "Mech" or preJoin[i] == "Moss" or preJoin[i] == "Mitsuu" or \
                       preJoin[i] == "Erwin" or preJoin[i] == "Bread" or preJoin[i] == "Teacher":
                        onStageCount = charJoin(preJoin[i], "auto", onStageCount, "n")
                    else:
                        backGround(preJoin[i])
                        ignoreBack = preJoin[i]
                jumpToScene = -1
                inject.append("wait_")
                inject.append(".205")
        elif jumpToScene != -1:
            pass

        elif line[0] == ">":
            if (line[1:6].upper() == "MECH " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MECH"):
                if line[6:-1].upper() == "ENTERS" or line[7:-1].upper() == "MECH":
                    onStageCount = charJoin("Mech", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Mech", line, onStageCount, "y")
            elif (line[1:6].upper() == "MOSS " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MOSS"):
                if line[6:-1].upper() == "ENTERS" or line[7:-1].upper() == "MOSS":
                    onStageCount = charJoin("Moss", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Moss", line, onStageCount, "y")
            elif (line[1:8].upper() == "MITSUU " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "MITSUU"):
                if line[8:-1].upper() == "ENTERS" or line[7:-1].upper() == "MITSUU":
                    onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Mitsuu", line, onStageCount, "y")
            elif (line[1:7].upper() == "ERWIN " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "ERWIN"):
                if line[7:-1].upper() == "ENTERS" or line[7:-1].upper() == "ERWIN":
                    onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Erwin", line, onStageCount, "y")
            elif (line[1:9].upper() == "TEACHER " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "TEACHER"):
                if line[7:-1].upper() == "ENTERS" or line[7:-1].upper() == "TEACHER":
                    onStageCount = charJoin("Teacher", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Teacher", line, onStageCount, "y")
            elif (line[1:7].upper() == "BREAD " and line.split()[1].upper() == "ENTERS") or \
               (line[1:7].upper() == "ENTER " and line.split()[1].upper() == "BREAD"):
                if line[7:-1].upper() == "ENTERS" or line[7:-1].upper() == "BREAD":
                    onStageCount = charJoin("Bread", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Bread", line, onStageCount, "y")
            elif (line[1:13].upper() == "BREAD EATER " and line.split()[2].upper() == "ENTERS") or \
                (line[1:7].upper() == "ENTER " and \
                line.split()[1].upper() + line.split()[2].upper() == "BREADEATER"):
                if line[13:-1].upper() == "ENTERS" or line[7:-1].upper() == "BREAD EATER":
                    onStageCount = charJoin("Bread", "auto", onStageCount, "y")
                else:
                    onStageCount = specPos("Bread", line, onStageCount, "y")

            elif (line[1:6].upper() == "MECH " and line[6:-1].upper() == "LEAVES") or \
               (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "MECH") or \
               (line[1:6].upper() == "MECH " and line[6:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Mech")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Mech" in posFarLeft:
                    posFarLeft = "0"
                elif "Mech" in posNearLeft:
                    posNearLeft = "0"
                elif "Mech" in posNearRight:
                    posNearRight = "0"
                elif "Mech" in posFarRight:
                    posFarRight = "0"
            elif (line[1:6].upper() == "MOSS " and line[6:-1].upper() == "LEAVES") or \
               (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "MOSS") or \
               (line[1:6].upper() == "MOSS " and line[6:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Moss")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Moss" in posFarLeft:
                    posFarLeft = "0"
                elif "Moss" in posNearLeft:
                    posNearLeft = "0"
                elif "Moss" in posNearRight:
                    posNearRight = "0"
                elif "Moss" in posFarRight:
                    posFarRight = "0"
            elif (line[1:8].upper() == "MITSUU " and line[8:-1].upper() == "LEAVES") or \
               (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "MITSUU") or \
               (line[1:8].upper() == "MITSUU " and line[8:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Mitsuu")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Mitsuu" in posFarLeft:
                    posFarLeft = "0"
                elif "Mitsuu" in posNearLeft:
                    posNearLeft = "0"
                elif "Mitsuu" in posNearRight:
                    posNearRight = "0"
                elif "Mitsuu" in posFarRight:
                    posFarRight = "0"
            elif (line[1:7].upper() == "ERWIN " and line[7:-1].upper() == "LEAVES") or \
                (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "ERWIN") or \
               (line[1:7].upper() == "ERWIN " and line[7:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Erwin")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Erwin" in posFarLeft:
                    posFarLeft = "0"
                elif "Erwin" in posNearLeft:
                    posNearLeft = "0"
                elif "Erwin" in posNearRight:
                    posNearRight = "0"
                elif "Erwin" in posFarRight:
                    posFarRight = "0"
            elif (line[1:9].upper() == "TEACHER " and line[7:-1].upper() == "LEAVES") or \
                (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "TEACHER") or \
               (line[1:9].upper() == "TEACHER " and line[7:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Teacher")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Teacher" in posFarLeft:
                    posFarLeft = "0"
                elif "Teacher" in posNearLeft:
                    posNearLeft = "0"
                elif "Teacher" in posNearRight:
                    posNearRight = "0"
                elif "Teacher" in posFarRight:
                    posFarRight = "0"
            elif (line[1:7].upper() == "BREAD " and line[7:-1].upper() == "LEAVES") or \
               (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "BREAD") or \
                (line[1:7].upper() == "BREAD " and line[7:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Bread")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Bread" in posFarLeft:
                    posFarLeft = "0"
                elif "Bread" in posNearLeft:
                    posNearLeft = "0"
                elif "Bread" in posNearRight:
                    posNearRight = "0"
                elif "Bread" in posFarRight:
                    posFarRight = "0"
            elif (line[1:13].upper() == "BREAD EATER " and line[13:-1].upper() == "LEAVES") or \
               (line[1:6].upper() == "EXIT " and line[6:-1].upper() == "BREAD EATER") or \
               (line[1:13].upper() == "BREAD EATER " and line[13:-1].upper() == "EXITS"):
                inject.append("leave_")
                inject.append("Bread")
                inject.append("y")
                inject.append("turn")
                inject.append("wait_")
                inject.append(".6")
                if onStageCount > 0:
                    onStageCount -= 1
                if "Bread" in posFarLeft:
                    posFarLeft = "0"
                elif "Bread" in posNearLeft:
                    posNearLeft = "0"
                elif "Bread" in posNearRight:
                    posNearRight = "0"
                elif "Bread" in posFarRight:
                    posFarRight = "0"

            elif line[0:13].upper() == ">MECH APPEARS" or line[0:13].upper() == ">MOSS APPEARS" or \
                 line[0:15].upper() == ">MITSUU APPEARS" or line[0:14].upper() == ">ERWIN APPEARS" or \
                 line[0:14].upper() == ">BREAD APPEARS" or line[0:20].upper() == ">BREAD EATER APPEARS" or \
                 line[0:16].upper() == ">TEACHER APPEARS":
                if line[-8:-1].upper() == "APPEARS":
                    onStageCount = charJoin(line.split()[0][1:].capitalize(), "auto", onStageCount, "n")
                else:
                    onStageCount = specPos(line.split()[0][1:].capitalize(), line, onStageCount, "n")

            elif line[:-1].upper() == ">MECH DISAPPEARS" or line[:-1].upper() == ">MOSS DISAPPEARS" or \
                 line[:-1].upper() == ">MITSUU DISAPPEARS" or line[:-1].upper() == ">ERWIN DISAPPEARS" or \
                 line[:-1].upper() == ">BREAD DISAPPEARS" or line[:-1].upper() == ">BREAD EATER DISAPPEARS" or \
                 line[:-1].upper() == ">TEACHER DISAPPEARS":
                inject.append("leave_")
                inject.append(line.split()[0][1:].capitalize())
                inject.append("n")
                inject.append("")
                if onStageCount > 0:
                    onStageCount -= 1
                if line.split()[0][1:].capitalize() in posFarLeft:
                    posFarLeft = "0"
                elif line.split()[0][1:].capitalize() in posNearLeft:
                    posNearLeft = "0"
                elif line.split()[0][1:].capitalize() in posNearRight:
                    posNearRight = "0"
                elif line.split()[0][1:].capitalize() in posFarRight:
                    posFarRight = "0"

            elif line[1:5].upper() == "TOP " or line[1:7].upper() == "FRONT ":
                inject.append("whotalking_")
                if line[1:5].upper() == "TOP " and line[5:-1].upper() == "MECH" or \
                   line[5:-1].upper() == "MOSS" or line[5:-1].upper() == "MITSUU" or \
                   line[5:-1].upper() == "ERWIN" or line[5:-1].upper() == "BREAD" or \
                   line[5:-1].upper() == "BREAD EATER" or line[5:-1].upper() == "TEACHER":
                    inject.append(line[5:-1].capitalize())
                elif line[7:-1].upper() == "MECH" or \
                   line[7:-1].upper() == "MOSS" or line[7:-1].upper() == "MITSUU" or \
                   line[7:-1].upper() == "ERWIN" or line[7:-1].upper() == "BREAD" or \
                   line[7:-1].upper() == "BREAD EATER" or line[7:-1].upper() == "TEACHER":
                    inject.append(line[7:-1].capitalize())
                inject.append("whotalking_")
                inject.append("")

            elif line[1:-1].upper() == "CLEAR" or line[1:-1].upper() == "EMPTY":
                inject.append("leave_")
                inject.append("all")
                inject.append("n")
                inject.append("")
                posFarLeft = "0"
                posNearLeft = "0"
                posNearRight = "0"
                posFarRight = "0"

            elif line[1:12] == "MECH FEELS " or line[1:9] == "MECH IS ":
                inject.append("emotion_")
                inject.append("Mech")
                soyFaceLookup("Mech", line.split()[2])
            elif line[1:12] == "MOSS FEELS " or line[1:9] == "MOSS IS ":
                inject.append("emotion_")
                inject.append("Moss")
                soyFaceLookup("Moss", line.split()[2])
            elif line[1:14] == "MITSUU FEELS " or line[1:11] == "MITSUU IS ":
                inject.append("emotion_")
                inject.append("Mitsuu")
                soyFaceLookup("Mitsuu", line.split()[2])
            elif line[1:13] == "ERWIN FEELS " or line[1:10] == "ERWIN IS ":
                inject.append("emotion_")
                inject.append("Erwin")
                soyFaceLookup("Erwin", line.split()[2])

            elif line[1:6].upper() == "INT. " or line[1:6].upper() == "EXT. ":
                if ignoreBack != line[6:-1]:
                    backGround(line[6:-1])
                    ignoreBack = 0
            elif line[1:10].upper() == "INTERIOR " or line[1:10].upper() == "EXTERIOR " or \
                 line[1:10].upper() == "BACKDROP ":
                if ignoreBack != line[10:-1]:
                    backGround(line[10:-1])
                    ignoreBack = 0
            elif line[1:12].upper() == "BACKGROUND ":
                if ignoreBack != line[12:-1]:
                    backGround(line[12:-1])
                    ignoreBack = 0

            elif line[1:6].upper() == "PLAY ":
                inject.append("startplaying_")
                music(line[6:-1])
            elif line[1:7].upper() == "MUSIC ":
                inject.append("startplaying_")
                music(line[7:-1])

            elif line[1:-1].upper() == "SHOCK":
                inject.append("broadcast_")
                inject.append("shock")

            elif line[1:-1].upper() == "BLACKOUT":
                inject.append("broadcast_")
                inject.append("blackout")
                inject.append("wait_")
                inject.append(".205")

            elif line[1:5].upper() == "JUMP " or line[1:7].upper() == "GO TO " or \
                 line[1:6].upper() == "GOTO ":
                inject.append("broadcast_")
                inject.append("blackout")
                inject.append("leave_")
                inject.append("all")
                inject.append("n")
                inject.append("")
                onStageCount = 0
                if line[1:7].upper() == "GO TO ":
                    jumpToScene = line.split()[2]
                else:
                    jumpToScene = line.split()[1]

            else:
                output_div = document.querySelector("#output")
                output_div.innerText = f"FATAL: {line.strip()}: command invalid!"
                terminated = True
                #sys.tracebacklimit = 0
                #raise TypeError(f"{line}: command invalid!")

        elif (line[0:5].upper() == "MECH " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:4].upper() == "MECH" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:4].upper() == "MECH" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            charEmotion("Mech", line)
            lastTalked = "Mech"
        elif (line[0:5].upper() == "MOSS " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:4].upper() == "MOSS" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:4].upper() == "MOSS" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            charEmotion("Moss", line)
            lastTalked = "Moss"
        elif (line[0:7].upper() == "MITSUU " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:6].upper() == "MITSUU" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:6].upper() == "MITSUU" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            charEmotion("Mitsuu", line)
            lastTalked = "Mitsuu"
        elif (line[0:6].upper() == "ERWIN " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:5].upper() == "ERWIN" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:5].upper() == "ERWIN" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            charEmotion("Erwin", line)
            lastTalked = "Erwin"
        elif (line[0:8].upper() == "TEACHER " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:7].upper() == "TEACHER" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:7].upper() == "TEACHER" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if "Teacher" in toBeAdded:
                onStageCount = charJoin("Teacher", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                jakstein("Teacher", line[line.find((line[(line.find(":") + 1):]).split()[0]):-1])
            else:
                jakstein("Teacher", line[(line.find(":") + 1):-1])
            lastTalked = "Teacher"
        elif (line[0:6].upper() == "BREAD " and ("):" in line.split()[1] or \
             (")" in line.split()[1] and ":" in line.split()[2]))) or \
             (line[0:5].upper() == "BREAD" and ("):" in line.split()[0] and \
                                              "(" in line.split()[0])) or \
             (line[0:5].upper() == "BREAD" and ("(" in line.split()[0] and \
                                               ")" in line.split()[0] and \
                                               ":" in line.split()[1])):
            if "Bread" in toBeAdded:
                onStageCount = charJoin("Bread", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                jakstein("Bread", line[line.find((line[(line.find(":") + 1):]).split()[0]):-1])
            else:
                jakstein("Bread", line[(line.find(":") + 1):-1])
            lastTalked = "Bread"
            
        elif line.split()[0][0] == "[" or line.split()[0][0] == "*":
            #jakstein("Grill", f"[{line[line.find(line.split()[0][1]):-2]}]")
            jakstein("Grill", line[0:-1])
        elif (line[0:5].upper() == "MECH:") or \
           (line.split()[0].upper() == "MECH" and ":" in line.split()[1].upper()):
            if "Mech" in toBeAdded:
                onStageCount = charJoin("Mech", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "MECH" and ":" in line.split()[1].upper():
                    jakstein("Mech", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Mech", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Mech", line[(line.find(":") + 1):-1])
            lastTalked = "Mech"
        elif (line[0:5].upper() == "MOSS:") or \
           (line.split()[0].upper() == "MOSS" and ":" in line.split()[1].upper()):
            if "Moss" in toBeAdded:
                onStageCount = charJoin("Moss", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "MOSS" and ":" in line.split()[1].upper():
                    jakstein("Moss", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Moss", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Moss", line[(line.find(":") + 1):-1])
            lastTalked = "Moss"
        elif (line[0:7].upper() == "MITSUU:") or \
           (line.split()[0].upper() == "MITSUU" and ":" in line.split()[1].upper()):
            if "Mitsuu" in toBeAdded:
                onStageCount = charJoin("Mitsuu", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "MITSUU" and ":" in line.split()[1].upper():
                    jakstein("Mitsuu", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Mitsuu", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Mitsuu", line[(line.find(":") + 1):-1])
            lastTalked = "Mitsuu"
        elif (line[0:6].upper() == "ERWIN:") or \
           (line.split()[0].upper() == "ERWIN" and ":" in line.split()[1].upper()):
            if "Erwin" in toBeAdded:
                onStageCount = charJoin("Erwin", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "ERWIN" and ":" in line.split()[1].upper():
                    jakstein("Erwin", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Erwin", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Erwin", line[(line.find(":") + 1):-1])
            lastTalked = "Erwin"
        elif (line[0:8].upper() == "TEACHER:") or \
           (line.split()[0].upper() == "TEACHER" and ":" in line.split()[1].upper()):
            if "Teacher" in toBeAdded:
                onStageCount = charJoin("Teacher", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "TEACHER" and ":" in line.split()[1].upper():
                    jakstein("Teacher", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Teacher", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Teacher", line[(line.find(":") + 1):-1])
            lastTalked = "Teacher"
        elif (line[0:6].upper() == "BREAD:") or \
           (line.split()[0].upper() == "BREAD" and ":" in line.split()[1].upper() and \
            (not "*" in line.split()[1].upper())):
            if "Bread" in toBeAdded:
                onStageCount = charJoin("Bread", "auto", onStageCount, "y")
            if line[(line.find(":") + 1)] == " ":
                if line.split()[0].upper() == "BREAD" and ":" in line.split()[1].upper():
                    jakstein("Bread", line[line.find(line.split()[2]):-1])
                else:
                    jakstein("Bread", line[1 + line.find((" " + line.split()[1])):-1])
            else:
                jakstein("Bread", line[(line.find(":") + 1):-1])
            lastTalked = "Bread"
        elif line[0:6].upper() == "BREAD " and 3 <= len(line.split()):
            if ((line.split()[0].upper() + line.split()[1].upper()) == "BREADEATER:") or \
               ((line.split()[0].upper() + line.split()[1].upper()) == "BREADEATER" and \
               ":" in line.split()[2].upper()):
                if "Bread" in toBeAdded:
                    onStageCount = charJoin("Bread", "auto", onStageCount, "y")
                if line[(line.find(":") + 1)] == " ":
                    jakstein("Bread", line[line.find(line.split()[3]):-1])
                else:
                    jakstein("Bread", line[(line.find(":") + 1):-1])
                lastTalked = "Bread"

        elif line[0:6].upper() == "BREAD " and 4 <= len(line.split()):
            if (line[0:12].upper() == "BREAD EATER " and ("):" in line.split()[2] or \
                 (")" in line.split()[2] and ":" in line.split()[3]))) or \
                 (line[0:11].upper() == "BREAD EATER" and ("):" in line.split()[1] and \
                                                  "(" in line.split()[1])) or \
                 (line[0:11].upper() == "BREAD EATER" and ("(" in line.split()[1] and \
                                                   ")" in line.split()[1] and \
                                                   ":" in line.split()[2])):
                if "Bread" in toBeAdded:
                    onStageCount = charJoin("Bread", "auto", onStageCount, "y")
                if line[(line.find(":") + 1)] == " ":
                    jakstein("Bread", line[line.find((line[(line.find(":") + 1):]).split()[0]):-1])
                else:
                    jakstein("Bread", line[(line.find(":") + 1):-1])
                lastTalked = "Bread"

        elif line != "" and line != "\n" and "lastTalked" in globals():
            jakstein(lastTalked, line[:-1])
        #if
    if jumpToScene != -1:
        output_div = document.querySelector("#output")
        output_div.innerText = f"FATAL: {jumpToScene}: Scene is incorrectly ordered or does not exist!"
        terminated = True
        #sys.tracebacklimit = 0
        #raise ValueError(f"{jumpToScene}: Scene is incorrectly ordered or does not exist!")
    inject.append("broadcast_")
    inject.append("blackout")
    inject.append("leave_")
    inject.append("all")
    inject.append("n")
    inject.append("")
    inject.append("loadscene_")
    inject.append("mainmenu")
    inject.append("BRAVO_")

    if terminated != True:
        gameframe = document.querySelector("#output")
        gameframe.style = "background-color: #777349"
        
        print("Compilation success... Ready for Turbowarp!")

        injectJSON = '{"☁ compiled":"'

        for i in range(len(inject) - 1):
            injectJSON += f"{inject[i]}🤡"
        injectJSON += f"{inject[-1]}"

        injectJSON += '"}'
        
        window.localStorage.setItem("cloudvariables:polhi.lol-online", injectJSON)
        
        gameframe = document.querySelector("#gameframe")
        gameframe.src = "./play"
    
