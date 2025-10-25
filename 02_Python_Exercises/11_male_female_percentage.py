male_students = int(input("Please enter the amount of male students: "))
female_students = int(input("Please enter the amount of female students: "))

total_students = male_students + female_students

male_percentage = (male_students / total_students)*100
female_percentage = (female_students / total_students)*100

print(f"The percentage of male students is: {male_percentage}%")
print(f"The percentage of female students is: {female_percentage}%")
