
# PyCity Schools Analysis

* For a "hopefully not interpreted as causal by a politician" observation, schools that had smaller budgets per student tended to have higher passing rates. Schools with budgets less than `$`615 per student had overall passing rates nearly 20% higher than schools with budgets greater than `$`615. Maybe teachers at the schools with small budgets altered their students tests, but overcorrected by a suspiciously large amount. Maybe all the smart kids go to those schools. Maybe whoever generated this data is a libertarian who hates government spending. I'm not sure.

* While there was quite a bit of variation in passing rates for reading and math between schools, there was very little variation in passing rates between grades within each school. This could be due to some combination of schools generally drawing students with similar educational backgrounds and socioeconomic status for each grade and/or have a more or less uniform quality to the teaching at each grade level. Or maybe the data was generated using the same distribution for each school.

* Charter schools tended to have higher overall passing rates than district schools by a wide margin of 95% to only 74%. The only logical explanation for this is that Betsy Devos is the random number generator for this assignment's data.

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd
import numpy as np

# Set file paths for school and student data
school_data_to_load = "C:\\Users\\andre\\OneDrive\\Wash_U_Repos\\DataAnalytics\\Week 4 - Pandas\\Homework\\Instructions\\PyCitySchools\\Resources\\schools_complete.csv"
student_data_to_load = "C:\\Users\\andre\\OneDrive\\Wash_U_Repos\\DataAnalytics\\Week 4 - Pandas\\Homework\\Instructions\\PyCitySchools\Resources\\students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()

## District Summary

* Calculate the total number of schools

* Calculate the total number of students

* Calculate the total budget

* Calculate the average math score 

* Calculate the average reading score

* Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2

* Calculate the percentage of students with a passing math score (70 or greater)

* Calculate the percentage of students with a passing reading score (70 or greater)

* Create a dataframe to hold the above results

* Optional: give the displayed data cleaner formatting

# Calculate the total number of schools
number_of_schools = school_data_complete["school_name"].nunique()
# Calculate the total number of students
number_of_students = school_data_complete["Student ID"].nunique()
# Calculate the total budget for all schools
total_budget = school_data_complete.groupby("school_name")["budget"].mean().sum()
# Calculate the average math score
avg_math_score = school_data_complete["math_score"].mean()
# Calculate the average reading score
avg_reading_score = school_data_complete["reading_score"].mean()
# Calculate the overall average score
avg_overall_score = (avg_math_score + avg_reading_score)/2
# Calculate the percentage of students that had passing math scores (>70%)
math_pass_pct = school_data_complete[school_data_complete["math_score"] > 70].count()["math_score"]/school_data_complete["math_score"].count()

# Calculate the percentage of students that had passing reading scores (>70%)
reading_pass_pct = school_data_complete[school_data_complete["reading_score"] > 70].count()["reading_score"]/school_data_complete["reading_score"].count()
# Create a pandas dataframe to summarize school and student data
summary_dataframe = pd.DataFrame({'School Count':number_of_schools, 'Student Count':number_of_students, 'Total Budget':total_budget, 'Avg Math Score':avg_math_score,
                         'Avg Reading Score':avg_reading_score, 'Overall Avg Score':avg_overall_score, 'Math Pass Rate':math_pass_pct, 'Reading Pass Rate':reading_pass_pct},
                                index = [0])

summary_dataframe


## School Summary

* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)
  
* Create a dataframe to hold the above results

print(school_data_complete.dtypes)

# Group data by school and type
grouped_df = school_data_complete.groupby(['school_name', 'type'])

# Calculate number of students per school
school_students = grouped_df["size"].mean()

# Calc budget per school
school_budget = grouped_df["budget"].mean()

# Calc each school's average math score
school_avg_math = grouped_df["math_score"].mean()

# Calc each school's average reading score
school_avg_reading = grouped_df["reading_score"].mean()

# Calc the number of students at each school with a passing math score
school_math_pass = school_data_complete.loc[school_data_complete["math_score"] >= 70].groupby(["school_name", "type"])["Student ID"].count()

# Calc the number of students at each school with a passing math score
school_reading_pass = school_data_complete.loc[school_data_complete["reading_score"] >= 70].groupby(["school_name", "type"])["Student ID"].count()

# Create summary table of summary statistics for each school
school_summary = pd.DataFrame({'Total Students' : school_students,
                               'Total School Budget' : school_budget,
                               'Per Student Budget' : school_budget/school_students,
                               'Average Math Score' : school_avg_math,
                               'Average Reading Score' : school_avg_reading,
                               '% Passing Math' : school_math_pass/school_students * 100,
                               '% Passing Reading' : school_reading_pass/school_students * 100,
                               '% Overall Passing Rate' : (school_math_pass + school_reading_pass)/(2 * school_students) * 100
                              })

# Reset index of summary table
school_summary = school_summary.reset_index(drop = False)

# Rename school name and type
school_summary = school_summary.rename(index=str, columns={"school_name": "School Name", "type": "School Type"})

# Set school name as the lone index
school_summary = school_summary.set_index('School Name')

# Reorder the columns to something that makes sense
school_summary = school_summary[['School Type', 'Total Students', 'Total School Budget', 'Per Student Budget',
                                'Average Math Score', 'Average Reading Score',
                                '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]

# Display top 5 rows of summary table without the school name index showing
del school_summary.index.name
school_summary.head()


## Top Performing Schools (By Passing Rate)

* Sort and display the top five schools in overall passing rate

# Sort the table by % Overall Passing Rate and return table of top 5 schools
school_summary.sort_values(by = "% Overall Passing Rate", ascending = False).head()

## Bottom Performing Schools (By Passing Rate)

* Sort and display the five worst-performing schools

# Sort the table by % Overall Passing Rate and return table of bottom 5 schools
school_summary.sort_values(by = "% Overall Passing Rate", ascending = True).head()

## Math Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

  * Create a pandas series for each grade. Hint: use a conditional statement.
  
  * Group each series by school
  
  * Combine the series into a dataframe
  
  * Optional: give the displayed data cleaner formatting

# Separate data into grades then group by school and find avg math score
grade_9 = school_data_complete.loc[school_data_complete["grade"] == "9th"].groupby("school_name")["math_score"].mean()
grade_10 = school_data_complete.loc[school_data_complete["grade"] == "10th"].groupby("school_name")["math_score"].mean()
grade_11 = school_data_complete.loc[school_data_complete["grade"] == "11th"].groupby("school_name")["math_score"].mean()
grade_12 = school_data_complete.loc[school_data_complete["grade"] == "12th"].groupby("school_name")["math_score"].mean()

# Merge each grade into one table
grade_math_summary = pd.DataFrame({"9th" : grade_9,
                                  "10th" : grade_10,
                                  "11th" : grade_11,
                                  "12th" : grade_12})
grade_math_summary = grade_math_summary[["9th", "10th", "11th", "12th"]]

del grade_math_summary.index.name
grade_math_summary

## Reading Score by Grade 

* Perform the same operations as above for reading scores

# Separate data into grades then group by school and find avg math score
grade_9 = school_data_complete.loc[school_data_complete["grade"] == "9th"].groupby("school_name")["reading_score"].mean()
grade_10 = school_data_complete.loc[school_data_complete["grade"] == "10th"].groupby("school_name")["reading_score"].mean()
grade_11 = school_data_complete.loc[school_data_complete["grade"] == "11th"].groupby("school_name")["reading_score"].mean()
grade_12 = school_data_complete.loc[school_data_complete["grade"] == "12th"].groupby("school_name")["reading_score"].mean()

# Merge each grade into one table
grade_math_summary = pd.DataFrame({"9th" : grade_9,
                                  "10th" : grade_10,
                                  "11th" : grade_11,
                                  "12th" : grade_12})
grade_math_summary = grade_math_summary[["9th", "10th", "11th", "12th"]]

del grade_math_summary.index.name
grade_math_summary

## Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

school_data_complete["Per Student Budget"] = school_data_complete["budget"]/school_data_complete["size"]

school_data_complete["Spending Ranges (Per Student)"] = pd.cut(school_data_complete["Per Student Budget"], 
                            bins = spending_bins, 
                            labels = group_names)

spending_grouped = school_data_complete.groupby("Spending Ranges (Per Student)")
students_in_bin = spending_grouped["Student ID"].count()
spending_avg_math = spending_grouped["math_score"].mean()
spending_avg_reading = spending_grouped["reading_score"].mean()
spending_pass_math = school_data_complete.loc[school_data_complete["math_score"] >= 70].groupby("Spending Ranges (Per Student)")["Student ID"].count()

spending_pass_reading = school_data_complete.loc[school_data_complete["reading_score"] >= 70].groupby("Spending Ranges (Per Student)")["Student ID"].count()

spending_summary = pd.DataFrame({'Average Math Score' : spending_avg_math,
                                'Average Reading Score' : spending_avg_reading,
                                '% Passing Math': spending_pass_math/students_in_bin * 100,
                                '% Passing Reading' : spending_pass_reading/students_in_bin * 100,
                                '% Overall Passing Rate' : (spending_pass_math + spending_pass_reading) / (2 * students_in_bin) * 100
                                })
spending_summary = spending_summary[['Average Math Score', 'Average Reading Score', '% Passing Math',
                                    '% Passing Reading', '% Overall Passing Rate']]


spending_summary



## Scores by School Size

* Perform the same operations as above, based on school size.

# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

school_data_complete["School Size"] = pd.cut(school_data_complete["size"], 
                            bins = size_bins, 
                            labels = group_names)

size_grouped = school_data_complete.groupby("School Size")
students_in_bin = size_grouped["Student ID"].count()
size_avg_math = size_grouped["math_score"].mean()
size_avg_reading = size_grouped["reading_score"].mean()
size_pass_math = school_data_complete.loc[school_data_complete["math_score"] >= 70].groupby("School Size")["Student ID"].count()

size_pass_reading = school_data_complete.loc[school_data_complete["reading_score"] >= 70].groupby("School Size")["Student ID"].count()

size_summary = pd.DataFrame({'Average Math Score' : size_avg_math,
                                'Average Reading Score' : size_avg_reading,
                                '% Passing Math': size_pass_math/students_in_bin * 100,
                                '% Passing Reading' : size_pass_reading/students_in_bin * 100,
                                '% Overall Passing Rate' : (size_pass_math + size_pass_reading) / (2 * students_in_bin) * 100
                                })
size_summary = size_summary[['Average Math Score', 'Average Reading Score', '% Passing Math',
                                    '% Passing Reading', '% Overall Passing Rate']]


size_summary

## Scores by School Type

* Perform the same operations as above, based on school type.

type_grouped = school_data_complete.groupby("type")
students_in_bin = type_grouped["Student ID"].count()
type_avg_math = type_grouped["math_score"].mean()
type_avg_reading = type_grouped["reading_score"].mean()
type_pass_math = school_data_complete.loc[school_data_complete["math_score"] >= 70].groupby("type")["Student ID"].count()

type_pass_reading = school_data_complete.loc[school_data_complete["reading_score"] >= 70].groupby("type")["Student ID"].count()

type_summary = pd.DataFrame({'Average Math Score' : type_avg_math,
                                'Average Reading Score' : type_avg_reading,
                                '% Passing Math': type_pass_math/students_in_bin * 100,
                                '% Passing Reading' : type_pass_reading/students_in_bin * 100,
                                '% Overall Passing Rate' : (type_pass_math + type_pass_reading) / (2 * students_in_bin) * 100
                                })
type_summary = type_summary[['Average Math Score', 'Average Reading Score', '% Passing Math',
                                    '% Passing Reading', '% Overall Passing Rate']]


type_summary