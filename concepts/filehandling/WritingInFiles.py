# In following snippet, I am creating/over-writing the content of employees.txt with new text
# If the file is already there, it will over-write
# If the file not there already, it will create a new file and write text into it

employees_text = open("employees.txt", "w")
employees_text.write("\nPramod - Scrum Master")
employees_text.close()
