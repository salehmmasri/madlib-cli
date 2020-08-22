x=""
with open('assets/madilp_cli.txt') as file:
    x=file.read()

print('file is closed?', file.closed)
def getKeys(formatString):
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates
    
    # print(keyList)
    return set(keyList) 

def addPick(cue, dictionary): 
    promptFormat = "Enter a specific example for {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response                                                             

def getUserPicks(cues):
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks   

def tellStory(storyFormat):
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():
    originalStoryFormat = x
    final_result = tellStory(originalStoryFormat)
    merge(final_result)  
    input("Press Enter to end the program.")
main()

# def merge(words):
#     with open("assets/madlip_cli_copy.txt",'w') as f2:
#         const2 = f2.write(constant.format(*words))
#     with open("assets/madlip_cli_copy.txt",'r') as f3:
#         const3 = f3.read()
#     return const3