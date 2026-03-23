import hashlib 

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verifyLogin(username: str, password: str, is_icon: bool):
    if is_icon:
        filepath = 'iData.txt'
    else:
        filepath = 'aData.txt'

    try:
        hpass = hash(password)  # no "\n" needed
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()  # removes \n and whitespace
                fields = line.split(",")
                if len(fields) == 2:
                    if fields[0] == username and fields[1] == hpass:
                        return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False