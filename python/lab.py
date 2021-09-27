from datetime import datetime, date

dob=input("Please enter your date of birth mm/dd/yyyy")
dob_object= datetime.strptime(dob,"%m/%d/%Y")     



today=datetime.today()

age=int((today-dob_object).total_seconds())

print(f"You are {age} seconds old!") 
