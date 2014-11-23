################################################################################
# Name: Chaise Farrar       Date Assigned:10/29/2014                           #
# Course: CSE 1284 Sec 10   Date Due: 10/29/2014                               #
# Project Name: Art Gallery                                                    #
# Program Description: Program allows the creation and modification of an Art  #
#                      Gallery database.                                       #
################################################################################

def main():
    while True:
        while True:
            try:
                filename=input('Please enter the name of the file: ')
                infile = open(filename,'r')
                break
            except IOError:
                input('File not found.\nPlease reenter a filename.')
        biglist = []
        for line in infile:
            flag=0
            line = line.strip('\n')
            if line not in ['Quizzes and Assignments','Lab Assignments', \
                            'Tests','Final Exam','']:
                line=int(line)
                biglist.append(line)
        infile.close()
        quizzes = biglist[0:6]
        labs = biglist[6:16]
        tests = biglist[16:19]
        final = biglist[19]
        avg_quizzes = sum(quizzes) / len(quizzes)
        avg_labs = sum(labs)/len(labs)
        avg_tests = sum(tests)/len(tests)
        total = (avg_quizzes*.2)+(avg_labs*.15)+(avg_tests*.45)+(final*.2)
        print('Your Grade is ', round(total,2))
        repeat=input('Do you want to enter another file?: ')
        if repeat in ['No','no','NO','n']:
            break
main()
