### COVID-19 Risk Assessment ###

q1 = """Those diagnosed with COVID-19 have had a wide range of symptoms - 
ranging from mild symptoms to severe illness. Symptoms may appear 2-14 days 
after exposure to the virus. 
Do you have:
* A fever of 100.4 degrees Fahrenheit or higher
* A cough
* Shortness of breath or difficulty breathing
* Fatigue
* Muscle or body aches
* Headache
* New loss of taste or smell
* Sore throat
* Congestion or runny nose
* Nausea or vomiting
* Diarrhea\n
"""
q2 = """Have you traveled in the past 14 days to regions affected by COVID-19?\n"""
q3 = """Have have you been in close contact with anyone who a has a confirmed COVID-19 diagnosis?\n"""
q4 = """Do you have heart disease, lung disease, kidney disease or diabetes?\n"""
q5 = """Are you age 60 or older?\n"""
low_risk = """Based off your answers to the previous question(s), you are likely at low risk for COVID-19. 
Please contact your healthcare provider for further advice or questions."""
high_risk = """Based on the responses to the previous questions, please contact your medical provider or visit 
your nearest Urgent Care to see if a COVID-19 test may be needed."""


# print(f"{q1=}\n{q2=}\n{low_risk=}\n{high_risk=}")

a1 = input(q1)
if a1 == 'n':
    print(low_risk)
else:
    a2 = input(q2)
    if a2 =='y':
        print(high_risk)
    else:
        a3 = input(q3)
        if a3 == 'y':
            print(high_risk)
        else:
            a4 = input(q4)
            if a4 == 'y':
                print(high_risk)
            a5 = input(q5)
            if a5 == 'y':
                print(high_risk)
            else:
                print(low_risk)