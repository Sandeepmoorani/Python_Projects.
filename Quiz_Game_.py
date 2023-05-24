print("************************** Welcome to quiz! *******************")

play= input("Do you want to play? ")

if play.lower() != "yes":
    quit()

score = 0

print("Okay! Let's play :)")

question= input("What does SM stand for? ")
if question.lower() == "sandeep moorani":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question= input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question= input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question= input("What does PSU stand for? ")
if question.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")