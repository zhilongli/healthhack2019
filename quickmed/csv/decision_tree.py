def next_qn(curr_node, response):

    #nodeDict={1: cough_duration, 2: cough_type, 3: wheezing, 4: rash, 5: sore_throat, 6: aches, 7: chills, 8: appetite, 9: sore_throat, 10: chest_pain, 11: swelling}

    if curr_node==1:
        if response>3:
            return "TB"
        else:
            return 2
    elif curr_node==2:
        if response==True: #wet cough with phlegm
            return 4
        else:
            return 3
    elif curr_node==3:
        if response==True: #wheezing!
            return "Asthma"
        else:
            return 5
    elif curr_node==5:
        if response==False: #No sore throat!!
            return "sinusitis"
        else:
            return "Pharyngitis"
    elif curr_node==8:
        if response==True: #Loss of appetite!
            return "influenza"
        else:
            return "Pharyngitis"
    elif curr_node==10:
        if response==True: #experiencing chest pain!
            return "bronchitis"
        else:
            return "strep"
    elif (curr_node == 4):
        if (response == True):
                return 'mono'
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
            return 'cold'
    elif (curr_node == 9):
        if (response == True):
            return 10
        else:
            return 11

    elif (curr_node == 11):
        if (response == True):
            return 'COPD'
        else:
            return 'Asthma'
    else:
        return "invalid response"
