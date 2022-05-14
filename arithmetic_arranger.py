import re

def arithmetic_arranger(problems, ans = False):

    main_list = []

    #  This is for the problems sorting and making them in correct format.
    while len(problems) < 6:
        if '/' in problems or '*' not in problems:
            print("Only Addition and subtraction are allowed")
        for i in problems:

            if '+' in i:
                list = i.split(' + ')
                for j in range(1):
                    list[0] = "  " + list[0]
                    list[1] = '  ' + list[1]
                if len(list[1]) > len(list[0]):
                    space = len(list[1]) - len(list[0])
                    list[0] = (" " * space) + ' ' +  list[0] 
                    list[1] = '+' + list[1]
                else :
                    space = len(list[0]) - len(list[1])
                    list[1] = ('+' + " " * space) + list[1]
                    list[0] = " " + list[0] 
                main_list.append(list)
            elif '-' in i:
                list = i.split(' - ')
                for j in range(1):
                    list[0] = "  " + list[0] 
                    list[1] = '  ' + list[1]        
                if len(list[1]) > len(list[0]):
                    space = len(list[1]) - len(list[0])
                    list[0] = (" " * space) + ' ' + list[0] 
                    list[1] = '+' + list[1]
                else :
                    space = len(list[0]) - len(list[1])
                    list[1] = ('-' + " " * space) + list[1]
                    list[0] = " " + list[0]
                main_list.append(list)

        # The main list contains the problems in sorted order.
        # Use another method and split each nested list first elemnt and store it somewhere else same with the second one.


        top_row = []
        bottom_row = []
        x = len(main_list)
        for i in range(x):
            top_row.append(main_list[i][0])
            bottom_row.append(main_list[i][1])

        # and then u need to calc the highest number of space req and make ------ accordingly.

        dash_row = []
        for i in range(len(bottom_row)):
            dash = len(bottom_row[i])
            dash_row.append('-' * dash)

        # then join them all and make it into one thing and the return this whole thing.

        main_dec = []
        for i in range(len(top_row)):
            main_dec.append(top_row[i])
            main_dec.append('    ')
        main_dec.append('\n')
        for i in range(len(bottom_row)):
            main_dec.append(bottom_row[i])
            main_dec.append('    ')
        main_dec.append('\n')
        for i in range(len(dash_row)):
            main_dec.append(dash_row[i])
            main_dec.append('    ')
        main_dec.append('\n')

        x = "".join(main_dec) 


        # Get answers for all problems

        answer = []
        for i in range(len(top_row)):
            a = int(top_row[i].replace(' ', '')) + int(bottom_row[i].replace(' ', ''))
            if len(bottom_row[i]) > len(str(a)):
                space = len(bottom_row[i]) - len(str(a))
                answer.append( (' ' * space) + str(a) + "    ")

        if ans == True:
            x = "".join(main_dec) + ''.join(answer)

        return x
