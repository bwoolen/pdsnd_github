import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! I am Brandon.  Let\'s explore some US bikeshare data!')
    print('Motivate, a bike share company, provided this data.')
    print('The data is provided for the months of January through June of 2017.')
    print('\nThe cities for which data is provided are Chicago, New York City, and Washington.')
    print(' ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Valid inputs for the cities are below:\n For Chicago you may enter Chicago or CHI\n For New York City you many enter New York or NYC\n For Washington you may enter Washington or WAS\n ")
    city= input('Enter a city from the list above that you would like to see data for: ')
    city=city.lower()
    while True:

       if city == 'chi' or city == 'chicago':
            print('\nChicago! Nice!\n')
            city = 'chicago'
            break
            

        elif city == 'nyc' or city=='new york':
            print('\nNew York City! Nice!\n')
            city='new york city'    
            break
            
        
        elif city == 'washington':
            print('\nWashington! Nice!\n')
            break
            
                
        else:
            print('\nPlease enter Chicago, New York City, or Washington.\n')
            city=input('Enter a city from the list above that you would like to see data for: ')
            city=city.lower()
    
        # TO DO: get user input for month (all, january, february, ... , june)
    allmonths=input('Would you like to filter the data by Month (Y/N)?: ')
    allmonths=allmonths.lower()
    month=''
    while True:
        if (allmonths=='y' and month==''):
            month=input('\nWhat month between January and June would you like to filter by?: ')
            month=month.lower()
            while True:
                if month in ['january','february','march','april','may','june']:
                    print('\nGot it.  We will filter by that.\n')
                    break
                    
                else:
                    print('\nThat is not a valid month.\n')
                    print('\nThe valid months are between January and June\n')
                    month=input('Please enter a valid month: ')
                    month=month.lower()
        elif (allmonths=='y' and month!=''):
            break
        elif allmonths=='n':
            print('\nOk. We will show you statistics for all months!\n')
            month='all'
            break
        else:
            print('\nThat is not a valid input.  Please enter Y or N.\n')
            allmonths=input('Would you like to filter by Month (Y/N)?: ')
            allmonths=allmonths.lower()
               
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    alldays=input('Would you like to filter the data by Day of the Week (Y/N)?: ')
    alldays=alldays.lower()
    day=''
    while True:
        if (alldays == 'y' and day==''):
            print('\nValid inputs are Monday, Tuesday, Wednesday, Thursday')
            print(',Friday,Saturday, and Sunday.\n')
            day=input('What day of the week would you like to filter by?: ')
            day=day.lower()
            while True:
                if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
                             print('\nGot it.  We will filter by that.\n')
                             break

                else:
                    print('\nThat is not a valid day of the week.')
                    print('Valid inputs are Monday, Tuesday, Wednesday, Thursday')
                    print(',Friday,Saturday, and Sunday.\n')
                    day=input('Please enter a valid day of the week: ')
                    day=day.lower()
        elif alldays == 'y' and day != '':
            break
        elif alldays == 'n':
            print('\nOk. We will show you statistics for all days!\n')
            day='all'
            break
        else:
            print('\nThat is not a valid input.  Please enter Y or N.\n')
            alldays=input('Would you like to filter by Day of the Week (Y/N)?: ')
            alldays=alldays.lower()
    print('The filters are {},{},and {}.'.format(city, month, day))
    print('\nLet\'s have some fun looking at this data!\n')
    print('-'*40)
    return city, month, day
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    #Gets the unique months.
    unique_month = df['month'].unique()
    #Gets the count of the unique months.
    set_month = set(unique_month)
    month_count=len(set_month)
    # find the most popular month if it is not filtered.
    popular_month =df['month'].mode()[0]
    if month_count>1:
        print('Most Popular Month:',popular_month)
    
    # TO DO: display the most common day of week
    #Gets the unique days of the week.
    unique_days = df['day_of_week'].unique()
    #Gets the count of the unique days of the week.
    set_days = set(unique_days)
    days_count = len(set_days)
    # find the most popular day of the week if it is not filtered.
    popular_day = df['day_of_week'].mode()[0]
    if days_count > 1:
        print('Most Popular Day of the Week:', popular_day)


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour.
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour:', popular_hour)
    #Prints how long the time stats took to run.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_startstation)
    
    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    #Create combined location
    df['Combined Location']=' Start: '+df['Start Station']+' / End: '+df['End Station']
    popular_combined_loc=df['Combined Location'].mode()[0]
    print('The Most Frequent Combination:',popular_combined_loc)


    #Prints how long the station stats took to run.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time']=pd.to_datetime(df['End Time'])
    df['Travel Time']=df['End Time']-df['Start Time']
    total_travel_time=np.sum(df['Travel Time'])
    total_travel_days=str(total_travel_time).split()[0]

    print('The total ride time adds up to {} days.'.format(total_travel_days))
      

    # TO DO: display mean travel time

    mean_travel_time=np.mean(df['Travel Time'])
    mean_travel_minutes=str(mean_travel_time).split(':')[1]
    print('The average ride time for each trip was {} minutes.'.format(mean_travel_minutes))

    #Prints how long the trip duration stats took to run.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count=df['User Type'].value_counts()
    print('The breakdown by type of user was as follows:\n')
    print(user_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nThe breakdown by gender is below:\n (Records without a reported gender are excluded.)\n')
        print(gender_count)
    except:
        print('\nThere is no gender data for this city.\n')
     
    # TO DO: Display earliest, most recent, and most common year of birth
   
    try:
        max_dob=df['Birth Year'].max()
        min_dob=df['Birth Year'].min()
        mode_dob=df['Birth Year'].mode()[0]
        print('\nThe oldest user was born in {}.\n\nThe youngest user was born in {}.\n\nThe most common year that users were born was {}.'.format(min_dob,max_dob,mode_dob))
    except:
        print('\nThere is no birth year data for this city.\n')
    #Prints how long the user stats took to run.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    '''
    Displays 5 rows of raw data at a time at the users request.
    Input: The DataFrame(df) used to compute the statistics.
    '''
    
    raw_data_index=0
    raw_data=input('Would you like to see the first five rows of data? (Y/N): ').lower()
    while True:
        if raw_data=='n':
            return
        elif raw_data=='y':
            print(df[raw_data_index:raw_data_index+5])
            raw_data_index=raw_data_index+5
            raw_data=input('Would you like to see five more rows of data? (Y/N: ').lower()
        else:
            print('That is not a valid input.  Please enter \'Y\' or \'N\'.')
            raw_data=input('Would you like to see five rows of data? (Y/N): ')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__": 
	main()





                     

