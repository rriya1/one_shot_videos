#used to analyze tabular data
import pandas as pd

#reading the csv file into a pandas data structure
covid_df=pd.read_csv('italy.csv')
#this will return a dataframe of pandas
print(type(covid_df))
#Nan means that no value was provided for that column
print(covid_df)
print("")

#getting metadata of a CSV
#---------------------------------------------------
#viewing basic information about the dataframe
print("about data")
print(covid_df.info())
#object is a generic datatype when it cannot figure out what data type a column is
print("")

print("a quick overview of the numeric data")
print(covid_df.describe())
print("")

#list the column properties
print(covid_df.columns)
print("")
#------------------------------------------------------

#internally we can think of this dataframe as a dictionary of lists
#the keys are the column header and the column under each key are the values for the corresponding keys in the dictionary
#its not actually like this but its the conceptual picture.


#retreiving the data
print("retrieving a column and then a vlaue")
print(covid_df['new_cases'])
print(covid_df.new_deaths)
#each column is not a list but a series, a differnt kind of np array with other functionalitites
#we can retrive a specific location from the series using the indexing notation
print(covid_df['new_cases'][230])
print("")

#the same retrival can also be done using the "at" method.
print(covid_df.at[230,'new_deaths'])
#specifying the row first and then the column in this case

#accesing multiplecolumns together
print("taking multiple columns, or the only ones which are needed")
new_covid_df=covid_df[['new_deaths','new_tests']]
#passing a list of columns
print(new_covid_df)
print("")
#this data that got created is justa different view of the same data, this also points to the same data
#if we modify anything here then the original datframe will also get modified.

#to make a coopy of the data frame we can call a copy method
covid_df_copy=covid_df.copy()
#this is a differnt data frome now

#getting the whole row
print("getting row with the key")
print(covid_df.loc[100])
print("")
#getting multiple rows from the table
print("first 5 and last 5 rows")
print(covid_df.head(5)) #printing the first 5 rows
print(covid_df.tail(5))#printing the last 5 rows
print("")

#to get the first column that isnt Nan
print(covid_df.new_tests.first_valid_index())
#random sample from the database
print(covid_df.sample(10))
print("")

print("sum of deaths")
print(covid_df.new_deaths.sum())
#when we are taking a sum, if there are any Nan values, they get ignored


#soritng data accroding to some conditions
print("show days when cases were more than 1K")
days1k=covid_df.new_cases>1000 #returns a column of boolean, true and false
print(covid_df[days1k])#will print where rows are true
print("only show deaths where cases > 1K")
print(covid_df[days1k].new_deaths)
print("")

#in python, the entire dataframe is not shown, we only see the first 5 and last 5 roows for convinience
#to change this we can use a function
# from IPython.display import display
# with pd.option_context('display.max_rows',100): #now this will display about 100 rows at once
#     display(covid_df)


#to remove a column we use this:
#covid_df.drop(columns=['new_cases'], inplace=True)

#sortng data accroding to a specific column
print('sorting data according to some values')
print(covid_df.sort_values('new_cases', ascending=False))
#sorting in descending order


#pandas has many utilities provided to work with dates
print("this date column has the data type of object")
print(covid_df.date)
print("converting it to date datatype and appending it to the dataframe")
covid_df['date_obj']=pd.to_datetime(covid_df.date)
print(covid_df)
print("")

#dropping the date column
print("removing date column")
covid_df.drop(columns=['date'],inplace=True)
print(covid_df)
print("")

print("extracting parts of date into seperate column usinf pandas")
covid_df['year']=pd.DatetimeIndex(covid_df.date_obj).year
print(covid_df)
#similarly month, weekday, month,da can also be returned
print("") 

print("grouping the data by its year")
#combining data for a year into a sile row of data
covid_df_yearly=covid_df.groupby('year')[['new_cases','new_deaths','new_tests']]
#so data of all year is grouped and displayed together
print(covid_df_yearly)

#writing the result back to a file
covid_df.to_csv('covid_yearly.csv',index=None)
#pandas also treats the index as data but we dnt want that in out csv file

print("plotting can also be done by pandas")
covid_df.new_cases.plot()