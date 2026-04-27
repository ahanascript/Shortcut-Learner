shortcut={}   #blank initial dict

with open("shortcut_db.txt", "r") as f:
    for line in f:
        content=line.strip()
        contentpart=content.split(",")
        
        if(len(contentpart)>=2):
            key=contentpart[0].strip()
            value=contentpart[1].strip()
            shortcut[key]=value
            
def find_closest_match(x,shortcut):
    best_match=None
    best_similarity=0
    
    for key in shortcut:
        similarity=0
        shorter_len=min(len(x),len(key))
        
        for pos in range(shorter_len):
            if x[pos]==key[pos]:
                similarity+=1
                
        if similarity>best_similarity:
            best_similarity=similarity
            best_match=key
            
    if best_similarity>=2:
        return best_match
    else:
        return None
    

while True:
    x=input("enter: ")   #user enters shortcut
    if (x=="exit"):
        print("goodbye")
        break
    if x in shortcut:      #check if shortcut exists or not
        print(shortcut[x])
    
    else:
        match=find_closest_match(x,shortcut)
        if match:
            print("did you mean",match,"?")
            y=input("enter yes or no: ")
            if (y=="yes"):
                print(shortcut[match])
                continue
        
        y=input("will you teach me? (yes/no): ")   #user enters meaning 
        if (y=="yes"):
            meaning=input("what's the meaning? ")
            shortcut[x]=meaning  #link meaning to shortcut
            with open("shortcut_db.txt", "a") as f1:
                f1.write(x+","+meaning+"\n")    #write into file and save
                
            print("learned")
        else:
            continue