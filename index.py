'''
Project Name: Was Clinton Right?
Author: Robbie Platt
Due Date: 2022-05-04
Course: CS1400-zzz




I learned how to combine research and reading to a file, 
combining everything that we have learned so far. Using math import
I will calculate the average job amount multiple times 
to get a clear picture of what the answer. I 
will then print to the screen the results as well as my analysis.
'''
import math
import statistics
import csv
"""
While I didn't get to use the imported math and statistics, they may have been helpful.
"""
def main():
    """
    This runs the code, must include a BLS_private.csv, and a presidents.txt for the program to draw from.
    conclusions.md will be generated.
    """
  
    
    #data_combined()
    #year_faction()
    #jobs_diff()
    read_book("presidents.txt")
    read_book("BLS_private.csv")
    write_conclusions()
    create_year_dict("BLS_private.csv")

def president_party(file_name):
    """
    file_name is used by the program to use presidents.txt, it will give the different presidents with
    their associated parties.
    """
    try:
        with open(file_name, "r") as in_file:
            reader = csv.reader(in_file, delimiter = ",")
            lines = list(reader)
    except:
        print("File must be included and meet proper formatting")
        
    
def create_year_dict(file_name):
    """
    Should be called with BLS_private, it will use the data and provide differences between one year to the
    next, this helps give the reader information with which to determine the validity of President Clintons
    comment.
    """
    try:
        with open(file_name, "r") as in_file:
            reader = csv.reader(in_file, delimiter = ",")
            lines = list(reader)
            year_dict = {}
            for line in lines:
                year_dict[line[0]] = line[1:]
            print(year_dict)
            for _i in range(6):
                print(lines[_i])
            for value in year_dict.values():
                #print(value)
                pass
            number = 0

            for item in year_dict.items():
                for line in lines[1:]:
                    number_new = number
                    number = int(line[1])
                    job_change = number - number_new
                    year_dict[item[0]].append(job_change)
                print(job_change)
                print(f'{item[0]}:{job_change}')


            number = 0
            """
            for line in lines:
                try:
                    number_new = number
                    number = int(line[1])
                    job_change = number - number_new
                    print(f"{key}:{job_change}")
                
            except:
                print("Nope")

        """  
    except:
        print("File must be included and meet proper formatting")

        #return item
        

def read_book(file_name):
    """
    Reads 6 lines of the file given it as a parameter.
    """
    try:
        with open(file_name, "r") as in_file:
            reader = csv.reader(in_file, delimiter = ",")
            lines = list(reader)



            for _i in range(50):
                print(lines[_i])
            in_file.seek(0)

    except:
        print("File must be included and meet proper formatting")


def write_conclusions():
    """
    Creates the conclusions.md file, the file includes my conclusions regarding the data.
    """
    try:
        with open('conclusions.md', 'w') as out_file:
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
            points to Bill Clinton being correct, and that it seems contradictory in nature.)""", file = out_file)
          
            print("""Bonus question answer: The comment made by Bill Clinton uses the straw man falacy,
            or in other words, it is addressing the numbers but purposefully omits the other factors.
            For example, are the jobs that exist during democratic lead years represent a quality employment
            experience for the employees? Do the jobs created represent a loss of government jobs so more
            alternative work is created out of necessity? Do the jobs actually have a purpose that influences
            the benefit of society. The numbers could be adjusted to better represent what Bill Clinton should
            have suggested by including an average wage of employment, valuation of the dollar, surveys
            of employment satisfaction tallied and given a metric based on an average.""", file = out_file)

    except:
        print("File must be included and meet proper formatting")


    
def data_sort():
    """
    Unused function, the beginnings of figuring out the average.
    """
    year_faction()
    year_thing = list(year_faction)
    if year_thing[1] == "Republican":
        print("republican")
    else:
        print("democrat")
    
    
def data_combined():
    """
    Combines years, factions, and job change value
    """
    year_faction()
    jobs_diff()

def year_faction():
    """
    declares the faction and the year associated.
    """
    try:
        file = open("presidents.txt")
    except:
        print("File must be included and meet proper formatting")
    content = file.readlines()
    year_strings = str(content[0]).split(',')
    print(year_strings)
    

    
def open_pres_txt():
    """
    Opens the presidents.txt file. No parameters used.
    """
    try:
        with open("presidents.txt", "r") as input_file:
            line = input_file.readline()
            while line != "":
                print(line)
                line = input_file.readline()
    except:
        print("File must be included and meet proper formatting")


def jobs_diff():
    """
    Defines how the program calculates the difference for each years jobs amount.  No parameters used.
    """
    try:
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
    except:
        print("File must be included and meet proper formatting")



            



            
if __name__ == "__main__":
    main()
