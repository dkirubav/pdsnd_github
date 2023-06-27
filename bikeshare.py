import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

filename = 'chicago.csv'

## load data file into a dataframe
df = pd.read_csv(filename)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name(chicago,new york city,washington:")
    city = city.lower()
    while (city != "chicago") and (city != "new york city") and (city != "washington"): 
     city = input("Enter city name(chicago,new york city,washington): ")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("Enter month(january through june OR all: ")
    month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("Enter Day of Week: " ) 
    day = day.lower()
    print("-"*70)   
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
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
    common_month = df['month'].mode()[0]
    print ("Most Common Month: ", common_month)
    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print ("Most Common Day of Week: ", common_dayofweek)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print ("Most Common Hour: ", common_hour)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ("Most Commonly used Start Station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ("Most Commonly used End Station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + " - " +  df['End Station']
    common_combination = df['start_end_station'].mode()[0]
    print ("Most frequent combination of Start and End Station Trip: " , common_combination)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    #print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ("Total Travel Time: ", total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ("Mean Travel time: ", mean_travel_time)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    #print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ("Counts of User Types: \n", user_types)

    # TO DO: Display counts of gender   
    gender_types = df['Gender'].value_counts()
    print ("\nCounts of Gender: \n", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print ("\nEarliest Birth Year: ", earliest_birth_year)
    recent_birth_year = df['Birth Year'].max()
    print ("Most Recent Birth Year: ", recent_birth_year)
    common_birth_year = df['Birth Year'].mode()[0]
    print ("Most Common Year of Birth: ", common_birth_year)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        rawdata_input = input('\nWould you like to see some raw data? Enter yes or no.\n')
        while True:
            if rawdata_input.lower() != 'yes':
                break  
            print(df.head())
            break
        print("-"*70)        
        time_stats(df)
        print ("\nCalling the Station Status Function")
        station_stats(df)
        print ("\nCalling the Trip Duration Status Function")
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
