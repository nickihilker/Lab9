############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
userInput = raw_input()
temperature = raw_input()
keepGoing = True
print "hello"
while(keepGoing):
    print "What is your Temperature?"
    temperature = raw_input()
    print temperature
    print "Have you been sick in the last 24 hours. Say yes or no."
    health = raw_input()
    print health
    print "Have you recently traveled to West Africa?"
    travel = raw_input()
    print travel
    if temperature > 105:
        print "go to the hospital"
    if health == "yes" and temperature > 102:
        print "go to the hosptial"
    if travel == "yes" and temperature > 100 and health == "yes":
        print "go to the hosptial"
    if health == "no" and travel == "no" and temperature < 100:
        keepGoing = False
print "everyone is safe from ebola ayyy"
            
            
