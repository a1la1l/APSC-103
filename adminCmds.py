import hashlib
import pandas as pd
import os

def addItem(item_name: str, stock: int) -> bool: # Define the function to take an item name, an integer stock, and return a boolean
    try: # Start a try block to catch and handle any potential errors during the file operations
        if os.path.exists(INVENTORY_FILE): # Check if the specified inventory file already exists in the current directory
            inventory_df = pd.read_excel(INVENTORY_FILE) # If the file exists, load its contents into a pandas DataFrame
        else:
            inventory_df = pd.DataFrame(columns=['Item Name', 'Stock']) # Create a completely new, empty DataFrame with the required column headers
            
        if item_name in inventory_df['Item Name'].values: # Check if the exact item name is already present anywhere in the 'Equipment' column
            print(f"Error: {item_name} already exists in the inventory.") # Print a specific error message to the console alerting the user of the duplicate
            return False # Return False to the user interface to indicate that the item addition was aborted
            
        new_item = pd.DataFrame({'Item Name': [item_name], 'Stock': [stock]}) # Create a new, single-row DataFrame containing the provided item name and its initial stock value
        inventory_df = pd.concat([inventory_df, new_item], ignore_index=True) # Append this new row to the bottom of the main DataFrame and reset the numerical index
        
        inventory_df.to_excel(INVENTORY_FILE, index=False) # Overwrite the physical Excel file with the updated DataFrame, explicitly excluding the pandas row numbers
        return True 
        
    except Exception as error:
        print(f"An error occurred adding the item: {error}") 
        return False
def deleteItem():

def addIconLoginInfo(username: str, password: str):
        try:
            hpassword = hashlib.sha256(password.encode()).hexdigest()
            with open('iData.txt', 'a') as file:# 'a' (append) mode adds new line to bottom without overwriting
                file.write(f"{username},{hpassword}\n")   
            return True
        except Exception as e:
            print(f"An error occurred adding new Icon: {e}")
            return False
def deleteIconLoginInfo(username: str):
    try:
        try: 
            with open('iData.txt', 'r') as file: 
                lines = file.readlines() 
        except FileNotFoundError as e: 
            print(f"File does not exist: {e}")
            return False 
            
        userfound = False 
        for i in range(len(lines)): # Iterate through the list of lines using a numerical index
            if lines[i].startswith(f"{username},"): # Check if the current line starts with the exact target username
                del lines[i] # Completely remove this specific line from the list rather than overwriting it with blanks
                userfound = True 
                break 
                
        if not userfound: 
            print(f"User not found") 
            return False
            
        with open('iData.txt', 'w') as file: 
            file.writelines(lines) 
            
        return True 
            
    except Exception as e: 
        print(f"An error occurred deleting the Icon account: {e}") 
        return False
    
def changePassword(username:str,new_password:str,isIcon:bool): 
    try: 
        hpassword = hashlib.sha256(new_password.encode()).hexdigest() 
        
        if isIcon: 
            datafile = 'iData.txt'
        else:
            datafile = 'aData.txt'

        try: 
            with open(datafile,'r') as file: 
                lines = file.readlines() # Read all lines from the file into a list
        except FileNotFoundError as e: 
            print(f"File does not exist: {e}")
            return False 
        
        userfound = False 
        for i in range(len(lines)): # Iterate through the list of lines using a numerical index so we can modify lines in place
            if lines[i].startswith(f"{username},"): # Check if the current line starts with the exact username followed by a comma
                lines[i] = f"{username},{hpassword}\n" # update the current line with username and new hashed password
                userfound = True 
                break 
        if not userfound: 
            print(f"User not found") 
            return False
            
        # Only open the file in write mode if we actually made a change in the steps above
        with open(datafile, 'w') as file: 
            file.writelines(lines) 
            
        return True 
        
    except Exception as e: 
        print(f"An error occurred changing the password: {e}") 
        return False