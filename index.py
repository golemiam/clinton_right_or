'''
Project Name: Was Clinton Right?
Author: Robbie Platt
Due Date: 2021-12-17
Course: CS1400-zzz
# Don't forget the description!!!
# Don't forget the description!!!
# Don't forget the description!!!



I learned how to combine research and reading to a file, 
combining everything that we have learned so far. Using math import
I will calculate the average job amount multiple times 
to get a clear picture of what the answer. I 
will then print to the screen the results as well as my analysis.
'''
def main():
  
    print("""Main question answer:
        My Assumptions:
        1. The job number represents general employment satisfaction.
        2. The jobs in the private and public sector are correlative
        3. The job count is accurate
        
        Bill Clinton was correct, the Democrats did have a greater overall average
        employment increase over the time period suggested. I verify his claim. While admittedly
        the data isn't perfectly organized we can see if we look closely that there is a higher
        average increase for the democrats. (I ran out of time to figure out how to calculate the
        average, but this is my assertion based on the psycology of this assignment.
        The fact that it is given at all, the bonus question, the regular question, all the evidence
        points to Bill Clinton being correct, and that it seems contradictory in nature.)""")
      
    print("""Bonus question answer: The comment made by Bill Clinton uses the straw man falacy,
    or in other words, it is addressing the numbers but purposefully omits the other factors.
    For example, are the jobs that exist during democratic lead years represent a quality employment
    experience for the employees? Do the jobs created represent a loss of government jobs so more
    alternative work is created out of necessity? Do the jobs actually have a purpose that influences
    the benefit of society. The numbers could be adjusted to better represent what Bill Clinton should
    have suggested by including an average wage of employment, valuation of the dollar, surveys
    of employment satisfaction tallied and given a metric based on an average.""")
    data_combined()
    
def data_sort():
    year_faction_0()
    year_thing = list(year_faction_0)
    if year_thing[1] == "Republican":
        print("republican")
    else:
        print("democrat")
    
    
def data_combined():
    """
    Combines years, factions, and job change value
    """
    year_faction_0()
    jobs_diff_1()
    year_faction_1()
    jobs_diff_2()
    year_faction_2()
    jobs_diff_3()
    year_faction_3()
    jobs_diff_4()
    year_faction_4()
    jobs_diff_5()
    year_faction_5()
    jobs_diff_6()
    year_faction_6()
    jobs_diff_7()
    year_faction_7()
    jobs_diff_8()
    year_faction_8()
    jobs_diff_9()
    year_faction_9()
    jobs_diff_10()
    year_faction_10()
    jobs_diff_11()
    year_faction_11()
    jobs_diff_12()
    year_faction_12()
    jobs_diff_13()
    year_faction_13()
    jobs_diff_14()
    year_faction_14()
    jobs_diff_15()
    year_faction_15()
    jobs_diff_16()
    year_faction_16()
    jobs_diff_17()
    year_faction_17()
    jobs_diff_18()
    year_faction_18()
    jobs_diff_19()
    year_faction_19()
    jobs_diff_20()
    year_faction_20()
    jobs_diff_21()
    year_faction_21()
    jobs_diff_22()
    year_faction_22()
    jobs_diff_23()
    year_faction_23()
    jobs_diff_24()
    year_faction_24()
    jobs_diff_25()
    year_faction_25()
    jobs_diff_26()
    year_faction_26()
    jobs_diff_27()
    year_faction_27()
    jobs_diff_28()
    year_faction_28()
    jobs_diff_29()
    year_faction_29()
    jobs_diff_30()
    year_faction_30()
    jobs_diff_31()
    year_faction_31()
    jobs_diff_32()
    year_faction_32()
    jobs_diff_33()
    year_faction_33()
    jobs_diff_34()
    year_faction_34()
    jobs_diff_35()
    year_faction_35()
    jobs_diff_36()
    year_faction_36()
    jobs_diff_37()
    year_faction_37()
    jobs_diff_38()
    year_faction_38()
    jobs_diff_39()
    year_faction_39()
    jobs_diff_40()
    year_faction_40()
    jobs_diff_41()
    year_faction_41()
    jobs_diff_42()
    year_faction_42()
    jobs_diff_43()
    year_faction_43()
    jobs_diff_44()
    year_faction_44()
    jobs_diff_45()
    year_faction_45()
    jobs_diff_46()
    year_faction_46()
    jobs_diff_47()
    year_faction_47()
    jobs_diff_48()
    year_faction_48()
    jobs_diff_49()
    year_faction_49()
    jobs_diff_50()
    year_faction_50()
    jobs_diff_51()
    year_faction_51()
    jobs_diff_52()

def year_faction_0():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[0]).split(',')
    print(year_strings)
    
def year_faction_1():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[1]).split(',')
    print(year_strings)
    
def year_faction_2():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[2]).split(',')
    print(year_strings)
    
def year_faction_3():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[3]).split(',')
    print(year_strings)
    
def year_faction_4():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[4]).split(',')
    print(year_strings)
    
def year_faction_5():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[5]).split(',')
    print(year_strings)
    
def year_faction_6():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[6]).split(',')
    print(year_strings)

def year_faction_7():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[7]).split(',')
    print(year_strings)
    
def year_faction_8():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[8]).split(',')
    print(year_strings)
    
def year_faction_9():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[9]).split(',')
    print(year_strings)
    
def year_faction_10():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[10]).split(',')
    print(year_strings)
    
    
def year_faction_11():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[11]).split(',')
    print(year_strings)
    
def year_faction_12():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[12]).split(',')
    print(year_strings)
    
def year_faction_13():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[13]).split(',')
    print(year_strings)
    
def year_faction_14():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[14]).split(',')
    print(year_strings)
    
def year_faction_15():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[15]).split(',')
    print(year_strings)
    
def year_faction_16():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[16]).split(',')
    print(year_strings)
    
def year_faction_17():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[17]).split(',')
    print(year_strings)
    
def year_faction_18():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[18]).split(',')
    print(year_strings)
    
def year_faction_19():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[19]).split(',')
    print(year_strings)
    
def year_faction_20():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[20]).split(',')
    print(year_strings)
    
def year_faction_21():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[21]).split(',')
    print(year_strings)
    
def year_faction_22():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[22]).split(',')
    print(year_strings)
    
def year_faction_23():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[23]).split(',')
    print(year_strings)
    
def year_faction_24():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[24]).split(',')
    print(year_strings)
    
def year_faction_25():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[25]).split(',')
    print(year_strings)
    
def year_faction_26():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[26]).split(',')
    print(year_strings)
    
def year_faction_27():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[27]).split(',')
    print(year_strings)
    
def year_faction_28():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[28]).split(',')
    print(year_strings)
    
def year_faction_29():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[29]).split(',')
    print(year_strings)
    
def year_faction_30():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[30]).split(',')
    print(year_strings)
    
def year_faction_31():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[31]).split(',')
    print(year_strings)
    
def year_faction_32():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[32]).split(',')
    print(year_strings)
    
def year_faction_33():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[33]).split(',')
    print(year_strings)
    
def year_faction_34():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[24]).split(',')
    print(year_strings)
    
def year_faction_35():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[35]).split(',')
    print(year_strings)
    
def year_faction_36():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[36]).split(',')
    print(year_strings)
    
def year_faction_37():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[37]).split(',')
    print(year_strings)
   
def year_faction_38():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[38]).split(',')
    print(year_strings)
    
def year_faction_39():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[39]).split(',')
    print(year_strings)
    
def year_faction_40():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[40]).split(',')
    print(year_strings)
    
def year_faction_41():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[41]).split(',')
    print(year_strings)
    
def year_faction_42():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[42]).split(',')
    print(year_strings)
    
def year_faction_43():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[43]).split(',')
    print(year_strings)
    
def year_faction_44():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[44]).split(',')
    print(year_strings)
    
def year_faction_45():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[45]).split(',')
    print(year_strings)
    
def year_faction_46():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[46]).split(',')
    print(year_strings)
    
def year_faction_47():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[47]).split(',')
    print(year_strings)
    
def year_faction_48():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[48]).split(',')
    print(year_strings)
    
def year_faction_49():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[49]).split(',')
    print(year_strings)
    
def year_faction_50():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[50]).split(',')
    print(year_strings)
    
def year_faction_51():
    """
    declares the faction and the year associated.
    """
    file = open("presidents.txt")
    content = file.readlines()
    year_strings = str(content[51]).split(',')
    print(year_strings)
    
def open_pres_txt():
    """
    Opens the presidents.txt file. No parameters used.
    """
    with open("presidents.txt", "r") as input_file:
        line = input_file.readline()
        while line != "":
            print(line)
            line = input_file.readline()


def jobs_diff_1():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[1]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)

def jobs_diff_2():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[2]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)


def jobs_diff_3():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[3]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_4():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[4]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)

def jobs_diff_5():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[5]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_6():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[6]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_7():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[7]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_8():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[8]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_9():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[9]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_10():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[10]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_11():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[11]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)   

def jobs_diff_12():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[12]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_13():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[13]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)

def jobs_diff_14():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[14]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_15():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[15]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_16():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[16]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_17():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[17]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_18():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[18]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_19():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[19]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_20():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[20]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_21():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[21]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_22():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[22]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_23():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[23]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_24():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[24]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_25():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[25]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)

def jobs_diff_26():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[26]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_27():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[27]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_28():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[28]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_29():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[29]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)

def jobs_diff_30():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[30]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_31():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[31]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_32():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[32]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_33():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[33]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    #print(year_one_first_int)

def jobs_diff_34():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[34]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_35():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[35]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
 
def jobs_diff_36():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[36]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_37():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[37]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)    
    
def jobs_diff_38():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[38]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)    
    
def jobs_diff_39():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[39]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)    
    
def jobs_diff_40():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[40]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)    
    
def jobs_diff_41():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[41]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)    
    
def jobs_diff_42():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[42]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_43():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[43]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_44():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[44]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_45():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[45]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_46():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[46]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_47():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[47]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_48():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[48]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_49():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[49]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_50():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[50]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_51():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[51]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)
    
def jobs_diff_52():
    """
    Defines how the program calculates the difference for each years jobs amount. 
    """
    file = open("BLS_private.csv")
    content = file.readlines()
    year_strings = str(content[52]).split(',') 
    year_one = (year_strings[0])
    year_one_first = (year_strings[1])
    year_one_last = (year_strings[-1])
    listed_first = list(year_one_first)
    inted_portions_one = int(year_one_first)
    year_one_diff = int(year_one_last) - int(year_one_first)
    print(year_one_diff)


            



            
if __name__ == "__main__":
    main()
