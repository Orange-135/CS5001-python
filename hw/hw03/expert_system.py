#defining the main function to process the whole system
def main(my_question, true, false):
    enter = input(my_question)
    if (enter == 'yes' ):
        true()
    else:
        false()

#starting to ask a question about the fever situation
def cough():
    main("Are you coughing?(yes or no)\n", short_of_three_symptoms, headache_1)

def headache_1():
    main("Do you have a headache?(yes or no)\n", exprience_following, aching)

def exprience_following():
    main("""Are you experiencing any of the following: pain when ending your head forward, \
nausea or vomiting, bright light hurting your eyes, \
drowsiness or confusuion?(yes or no)\n""", menighities, vomiting)

#get the corresponding possibility
def menighities():
    print("Possibilities include menigities.")

def vomiting():
    main("Are you vomiting or had diarrhea?(yes or no)\n", \
        digestive_tract_infection, aching)

#get the corresponding possibility
def digestive_tract_infection():
    print("Possibilities include digestive tract infection.")

def short_of_three_symptoms():
    main("Are you short of breath or wheezing or coughing up phlegm?(yes or no)\n", \
        pneumonia, headache_2)

#get the corresponding possibility
def pneumonia():
    print("Possibilities include pneumonia or infection of airways.")

def headache_2():
    main("Do you have a headache?(yes or no)\n", viral, aching)

#get the corresponding possibility
def viral():
    print("Plssibilities include viral infection.")

def aching():
    main("Do you have aching bones or aching joints?(yes or no)\n", viral, rash)

def rash():
    main("Do you have a rash?(yes or no)\n", insufficient, throat)

#get the corresponding possibility
def insufficient():
    print("Insufficient information to list possibilities.")

def throat():
    main("Do you have a sore throat?(yes or no)\n", throat_infection, back_pain)

#get the corresponding possibility
def throat_infection():
    print("Possibilities include a throat infection.")

def back_pain():
    main("Do you have back pain just above the waist with chills and fever? \
(yes or no)\n", kidney_infection, pain_urinating)

#get the corresponding possibility
def kidney_infection():
    print("Possibilities include kidney infection.")

def pain_urinating():
    main("Do you have pain urinating or are urinating more often?(yes or no)\n", urinary_tract_infection, spent_time)

#get the corresponding possibility
def urinary_tract_infection():
    print("Possibilities include a urinary yract infection.")

def spent_time():
    main("Have you spent the day in the sun or in the hot conditions? \
(yes or no)\n", sunstroke_exhausion, insufficient)

#get the corresponding possibility
def sunstroke_exhausion():
    print("Possibilities sunstroke or heat exhausion.")

cough()
