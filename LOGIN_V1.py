import hashlib 

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

#https://www.youtube.com/watch?v=9OjD_HjV03E
def verifyLogin(username:str,password:str,iconLogginIn:bool): 
    if iconLogginIn: 
        filepath='iData.txt'
    else:
        filepath='aData.txt' 

    try: 
        hpass = hash(password) + "\n" # adds a newline character to the inputted password so it matches the format of the password stored in the text file.
        with open(filepath,'r') as file: # Opens and closes the file located in read-only mode ('r')
            for line in file: # reads the opened text file in a loop for each line
                fields=line.split(",") # splits the line of text into fields when there is a comma
                if len(fields)==2: # check if there are two items (username and password)
                    if fields[0]==username and fields[1]==hpass: 
                        return True             
        return False 
    except Exception as e:
        print(f"An error occurred: {e}")
        return False 
