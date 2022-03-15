def read_database():
    with open('database.txt', 'r') as file:
        f = file.readlines()
        user_list = []    # Defining a new list for contents of database.txt

        for item in f:
            user_list.append(item.strip())    # Takes out \n and any other spaces

        db_as_string = '\n'.join(user_list)    # Makes a str from the list of names
    
    return db_as_string    # returns string of names

def save_to_database(fname, lname):
    with open('database.txt', 'r+') as file:
        index = 1    #defining index that counts what will become the id of next entry
        item_list = []    #defining a new list for contents of database

        for item in file:
            item_list.append(item.strip())    # takes out \n and any other spaces
        
        for i in range(len(item_list)):    # raises the index as many times as is the length of the list
            index+=1
            i+=1
        
        file.write(f"\n{index},{fname},{lname}")    # writes a new line, the index we counted, first and lastname to the end of the line

save_to_database("James", "Bond")