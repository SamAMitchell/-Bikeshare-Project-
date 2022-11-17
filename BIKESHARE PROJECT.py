import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}




def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data.\n')
    
    city = ('chicago', 'new york city', 'washington')
    month = ('janurary', 'feburary', 'march', 'april', 'june', 'all')
    day = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all')

#user to choose a city.
    while True:
        city = input('What city would you like to learn about today Chicago, New York City, or Washington? ').lower()
        if city not in('chicago', 'new york city', 'washington'):
            print('\nOops you did not choose a city that is listed, please try again. Please and Thank You!\n')
            continue
        else:
            break
#asking for the user to pick a month, day or both
    while True:
       month = input('\nGreat!, now would you like to filter your data by a month, day, all or none? \n').lower()
       if month not in( 'month', 'day', 'all'):
           print('\nOops you did not choose one of the options, please try again. Please and Thank You!\n')
           continue
       else:
           break
#get user to pick which month
    while True:
       month = input('\nGreat!. Please choose a month, day, or all \n').lower()
       if month not in ('januray', 'feburary', 'march', 'april', 'may', 'june', 'all'):
           print('\nOops you did not choose one of the options, please try again. Please and Thank You!\n')
           continue
       else:
           break
#choosing what day to pick
    while True:
        day = input('\nPlease choose a day of the week.\n').lower()
        if day not in('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print('\nOops you did not choose one of the options, please try again. Please and Thank you!\n')
        else:
            break
       
    print('-'*40)
    return city, month, day




#loading data into data frame
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    start_time = pd.to_datetime(df['Start Time'])
#convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#extract month and dayof the week from start time to create new column
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = (df['Start Time'].dt.day_of_week)

#displaying the month df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february','march', 'april', 'may', 'june']
        month = months.index(month) + 1

#filter by month to create new df
    df = df[df['month'] == month]

#filter day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

#displaying statistics on the most frequent times of travel
    return df



def time_stats(df):
    print('\nNow calculating the most frequent times of travel...\n')
    start_time = time.time()   

#displaying the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most common month: \n', popular_month)
          
#displaying the most common day
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most common day is: \n', popular_day)

#displaying the common hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most common hour is: \n', popular_hour)
    print('\nThis took %s seconds: \n' %(time.time() - start_time))
    print('_'*40)
    

    
def station_stats(df):

#displaying statistics on the most popular stations and trip
    print('\nCalculating the most popular start stations for trips...\n')
    start_time = time.time() 
#displaying the most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most popular start station is: \n',  start_station)

#display the most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station is: \n', end_station)

#display most frequent combination of start station and end station
    combination_station = (df['Start Station'] + df['End Station']).value_counts().idxmax
    print('\nThe most popular ride start and end stations are: \n', combination_station)
    print('\nThis took %s seconds. \n' % (time.time() - start_time))
    print('_'*40)

    

    
def trip_duration_stats(df):
#displaying the statistics on the total and average trip duration  
    print('\nCalculating trip duration... \n')
    start_time = time.time()  

#display tital time travel
    total_travel_time = sum(df['Trip Duration'])
    print('\nThe total travel time: \n', total_travel_time/86400, 'days')

#diaply mean travel time
    mean_travel_time = sum(df['Trip Duration'])                                     
    print('\nMean travel time is: \n', mean_travel_time/60, 'minutes')                               
                           
    print('\nThis took %s seconds: \n' % (time.time() - start_time))
    print('_'*40)


    
    
#displaying statistics on bikeshare users
def user_stats(df):
#displaying statistics on bikeshare userserally we are almost done!')
    print('\nCalculating user stats...\n')
    start_time = time.time()

#display counts of user types
    if 'user type' in(df.columns):
        user_types = (df['user type']).value_counts()
        print('user type: \n', user_types)

#displaying counts of gender
    if "gender" in(df.columns):
        gender_types = df['gender'].value_counts()
        print(df['gender'].value_counts())
        print('\ngender: \n', gender_type)
    else:
        print('nan')
#displaying earliest, most recent, and most common year of birth
    if 'birth year' in(df.columns):
        birth_year = df['birth_year'].fillna(0).astype('int64')
        print('\nThe easrlist birth year is: {year.min()}\most recent is: {year.max()}\ and most common is: {year.mode()}\n')
        print('\nThis too %s seconds: \n' % (time.time() - start_time))
        print('_'*40)

        

#asking the user if they would like to see some raw data and displaying 5 rows
def diaplay_raw_data(df):
    view_data = input('\nIf you would like to view 5 rows of individual trip data, enter yes or no\n').lower()
    if view_data == 'yes':
        count = 0
    while True:
        print(df.iloc[ :5])
        count += 5
        ask = input('\nShould we keep going?\n')
    if ask() != 'yes':
        print('\nGoodbye!\n')

        
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':      
            break
     
    
    
    
if __name__=='__main__':
    main()
        
#credits
# overstackflow.com
# mike coding turtorials on you tube
# git hub
# kaggle


# In[ ]:




