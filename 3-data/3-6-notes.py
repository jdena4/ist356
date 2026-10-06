import datetime

# A String
mike_dob = "Dec 6, 1990"
mikes_dob_date =datetime.datetime.strptime(mike_dob, "%b %d, %Y").date()
four_weeks = datetime.timedelta(weeks=4)
four_weeks_from_dob = mikes_dob_date + four_weeks

# a python datetime object
today = datetime.date.today()

print(f"Today is {today}")
print(f"Mike's date of birth is {mikes_dob_date}")
print(f"Four weeks from Mike's date of birth is {four_weeks_from_dob}")