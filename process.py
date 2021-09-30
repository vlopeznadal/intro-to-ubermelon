log_file = open("um-server-01.txt") # opening file's information to use in program


def sales_reports(log_file): # function to print specific lines in text file
    for line in log_file: # for each line in the text file, do something
        line = line.rstrip() # take the line of text and remove white space
        day = line[0:3] # looking at the first three characters of the string
        if day == "Tue": # if the first three characters of the string are "Tue"...
            print(line) #... print the line 


sales_reports(log_file) # call the function and pass a text file for it to use