# In following snippet, I am over-writing the content of employees.txt with new text

employees_text = open("employees.txt", "w")
employees_text.write("\nPramod - Scrum Master")
employees_text.close()
