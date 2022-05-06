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
import csv

def main():
    """
    This runs the code, must include a BLS_private.csv, and a presidents.txt for the program to draw from.
    conclusions.md will be generated.
    """

    create_year_dict("BLS_private.csv", "presidents.txt")
    write_conclusions()

def create_year_dict(file_name, file_name_two):
    """
    Should be called with BLS_private as the first parameter, it will use the data and provide differences between one year to the
    next, this helps give the reader information with which to determine the validity of President Clintons
    comment. The second parameter should be the "presidents.txt" file containing a list of presidents and their particular party.
    Each file should be comma separated, on the left is the year.
    """
    try:
        with open(file_name, "r") as in_file:
            reader = csv.reader(in_file, delimiter = ",")
            lines = list(reader)
        with open(file_name_two, "r") as in_file_two:
            reader_two = csv.reader(in_file_two, delimiter = ",")
            lines_presidents = list(reader_two)
            lines.pop(0)

    except FileNotFoundError:
        print("You need to include a proper file for this to run.")

    for line in lines:
        for _i in range(len(line)):
            line[_i] = int(line[_i])


    last_diff = int(lines[-1][-1]) - int(lines[-1][1])

    job_diff = []

    for _i in range(len(lines)-1):
        job_diff.append(lines[_i+1][1] - lines[_i][1])

    job_diff.append(last_diff)

    summ_dem = []
    summ_rep = []
    for _i in range(len(lines)):
        if lines_presidents[_i][1] == " Democrat":
            summ_dem.append(job_diff[_i])

        elif lines_presidents[_i][1] == " Republican":
            summ_rep.append(job_diff[_i])

    comp_summ_dem = int(math.fsum(summ_dem))
    final_summ_dem = (comp_summ_dem * 1000)
    comp_summ_rep = int(math.fsum(summ_rep))
    final_summ_rep = (comp_summ_rep * 1000)
    for _i in range(len(lines)):
        print(f"Party: {lines_presidents[_i][1]} Year: {lines[_i][0]} Jobs Created: {job_diff[_i]}")
    print()

    print(f"Democrat total increase in jobs: {final_summ_dem}")
    print(f"Republican total increase in jobs: {final_summ_rep}")



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
            4. I have chosen presidents to represent the years based on greatest amount of months in office.
            The assumption here is that the few months where there is a different president in office were inconsequential.

                As per the assignment we know Bill Clinton made the claim: "So what's the score? Republicans 24 million, 
            Democrats 42 million. In this I say Bill Clinton was close enough, the Democrats did have a greater overall average
            employment increase over the time period suggested. I verify his claim. The data backs him up.
            He really is correct about the numbers being much higher during years where a Democrat was in office. 
            As you can see from the programs results, there were 40 million jobs created during years where a democrat
            was the president and only 24 million while a republican president was in office.
            I may be a republican but it is hard to argue with those figures regarding his statement.

                So what about job satisfaction, overall satisfaction of society? Well, Clinton never said
            anything about those factors. He is a politician and he wanted to focus on the positive. There
            isn't really anything unsurprising about that. Employment opportunities are important, and it
            is a good thing that they were made.

                You think I'm not very persuasive, well that is probably because I don't particularly side with
            democrats, I just can't argue the numbers. Four years in office on average means that if there was
            a problem with something the previous president had done, they would have plenty of time to undo
            whatever there predecessor may have messed up, and plenty of time to make jobs.

                In conclusion, Clinton was right about what he said. Holding the White House may or may not
            include having a majority in congress, but he didn't address that and he is a politician so using the
            statistics that make him and his party look the best quite frankly, makes a lot of sense.

                )""", file = out_file)

            print("""
                Bonus question answer: The comment made by Bill Clinton uses the straw man fallacy,
            or in other words, it is addressing the numbers but he purposefully omits the other factors.
            For example, are the jobs that exist during democratic presidential years represent a quality employment
            experience for the employees involved? Do the jobs created represent a loss of government jobs so more
            alternative work is created out of necessity? Do the jobs actually have a purpose that influences
            the benefit of society. The numbers could be adjusted to better represent what Bill Clinton should
            have suggested by including an average wage of employment, valuation of the dollar, surveys
            of employment satisfaction tallied and given a metric based on an average.

                Another method that would help increase the value of the statement would be to have percentages of 
            congressmen who were republican, and who were democratic. The senate also can impact this. For example:
            Someone wants to pass a law that requires licenses for braiding hair. The law gets passed and now new jobs are created, but, maybe 
            not in the economies best interest. If every effort to start a business is thwarted by litigation, is it really
            in our best interest to have jobs created that are only collecting money for licenses? Yes it is a job, but it hinders
            jobs that are created that provide a service.

                In conclusion numbers representing jobs that provide a service versus jobs that only collect money for licensure should
            be a factor included. Numbers representing congress personelle, senate personelle, and any other influential party's should be taken 
            into consideration. Not just who the president is, but all of these.""", file = out_file)

    except FileExistsError:
        print("File cannot be created")

if __name__ == "__main__":
    main()




