
# A program to implememt the flowchart, asking a series of questions to determine if you should eat the food or not
# MNTALL0003
# 01 April 2021

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
r = input('Was it sticky? (yes/no)\n')
if r == 'no':
    r = input('Did anyone see you? (yes/no)\n')
    if r == 'no':    
        r = input('Is it an Emausaurus? (yes/no)\n')
    if r == 'no':
        r = input('Did the cat lick it? (yes/no)\n')
        if r == 'no':
            decision = 'Eat it.'
        else:
            r = input('Is your cat healthy? (yes/no)\n')
            if r == 'no':
                decision = 'Your call.'
            else:
                decision = 'Eat it.'
    else:  
        r = input('Are you a Megalosaurus? (yes/no)\n')
        if r == 'no': 
            decision = "Don't eat it."
        else:
            decision = 'Eat it.'
        
else:
    r = input('Is it a raw steak? (yes/no)\n')
    if r=='no':
        r = input('Did the cat lick it? (yes/no)\n')
        if r == 'no':
            decision = 'Eat it.'   
        else: 
            r = input('Is your cat healthy? (yes/no)\n') 
            if r == 'no':
                decision = 'Your call.'
            else:
                decision = 'Eat it.'                
    else:
        r = input('Are you a puma? (yes/no)\n')        
        if r == 'no':
            decision = "Don't eat it."
    else:     
        r = input('Was it a boss/lover/parent? (yes/no)\n')        
        if r == 'no':
            decision = 'Eat it.'
        else:    
            r = input('Was it expensive? (yes/no)\n')   
            if r == 'no':
                r = input('Is it chocolate? (yes/no)\n')
                if r == 'no':
                    decision="Don't eat it."
                else:        
                    decision = 'Eat it.' 
            else:
                r = input('Can you cut off the part that touched the floor? (yes/no)\n')
                if r=='no':
                    decision = 'Your call.'
                    
                else:
                    decision = 'Eat it.'
                
            else:
                decision = 'Eat it.'
                
                    
print('Decision:', decision)





























