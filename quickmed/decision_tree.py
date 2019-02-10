def next_qn(curr_node, response):

    #nodeDict={1: cough_duration, 2: cough_type, 3: wheezing, 4: rash, 5: sore_throat, 6: aches, 7: chills, 8: appetite, 9: sore_throat, 10: chest_pain, 11: swelling}


    if type(response) is str:
        return "Invalid response received"
    elif curr_node==1:
        if int(response)>3:
            return "This is not a final diagnosis, but we suspect you may have TB! Please visit the nearest hospital or clinic as soon as possible!"
        else:
            return 2
    elif curr_node==2:
        if response==True: #wet cough with phlegm
            return 4
        else:
            return 3
    elif curr_node==3:
        if response==True: #wheezing!
            return "This is not a final diagnosis, but we suspect you may have Asthma!"
        else:
            return 5
    elif curr_node==5:
        if response==False: #No sore throat!!
            return "This is not a final diagnosis, but we suspect you may have Sinusitis!"
        else:
            return "This is not a final diagnosis, but we suspect you may have Pharyngitis!"
    elif curr_node==8:
        if response==True: #Loss of appetite!
            return "This is not a final diagnosis, but we suspect you may have Influenza!"
        else:
            return "This is not a final diagnosis, but we suspect you may have Pharyngitis!"
    elif curr_node==10:
        if response==True: #experiencing chest pain!
            return "This is not a final diagnosis, but we suspect you may have Bronchitis!"
        else:
            return "This is not a final diagnosis, but we suspect you may have Strep!"
    elif (curr_node == 4):
        if (response == True):
                return 'This is not a final diagnosis, but we suspect you may have Mono!'
        else:
            return 6

    elif (curr_node == 6):
        if (response == True):
            return 7
        else:
            return 9

    elif (curr_node == 7):
        if (response == True):
            return 8
        else:
            return 'This is not a final diagnosis, but we suspect you may have Cold!'
    elif (curr_node == 9):
        if (response == True):
            return 10
        else:
            return 11

    elif (curr_node == 11):
        if (response == True):
            return 'This is not a final diagnosis, but we suspect you may have COPD!'
        else:
            return 'This is not a final diagnosis, but we suspect you may have Asthma!'
    else:
        return "invalid response"
