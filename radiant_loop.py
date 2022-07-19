user_firstName ="Alen"
where_are_you_now = input(f"Where are you now {user_firstName}?")
where_are_you_now = where_are_you_now.strip().upper()

still_at_radiant = True

while (still_at_radiant == True):
 where_are_you_now = input(f"Where are you now {user_firstName}?")
 if (where_are_you_now == "RADIANT"):
    print(f" NOOO Keep trying {user_firstName} "
        f"you gotta get the FCK out of it 🖖")
else:
 still_at_radiant = False
print(f"You're FREE {user_firstName} 🖖")