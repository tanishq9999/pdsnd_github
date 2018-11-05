import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    check_city = True
    while check_city:
        city = input("Enter the name of the city you would like to query on: ").lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            check_city = False
        else:
            print('Error!! Please enter correct city name.')

    # get user input for month (all, january, february, ... , june)
    check_month = True
    while check_month:
        month = input("Enter the name of the month to filter by or all to apply no filter: ").lower()
        if month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'june' or month == 'july':
            check_month = False
        else:
            print('Error!! Please enter all or correct month name.')  

    # get user input for day of week (all, monday, tuesday, ... sunday)
    check_day = True
    while check_day:
        day = input("Enter the name of the day of week to filter by or all to apply no filter: ").lower()
        if day == 'all' or day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday':
            check_day = False
        else:
            print('Error!! Please enter the correct day of week.')

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
    # Load data for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Converting Start Time column into datetime datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month column from start time column and create new month column
    df['month'] = df['Start Time'].dt.month

    # Extract day of the week from start time column and create new day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['months'] = df['Start Time'].dt.month
    common_month = df['months'].mode()[0]
    print("The most common month is {}.".format(common_month))

    # display the most common day of week
    df['days'] = df['Start Time'].dt.weekday_name
    common_day = df['days'].mode()[0]
    print("The most common day of the week is {}.".format(common_day))

    # display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    common_hour = df['hours'].mode()[0]
    print("The most common start hour is {}.".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}.".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}.".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + ' ' + df['End Station']
    common_startandend = df['Start and End Station'].mode()[0]
    print("The most common combination of start and end station is {}.".format(common_startandend))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()

    print('The total time travelled is {} hours.'.format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()

    print('The mean of total travel time is {} hours.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('The number of counts of user type is \n{}.'.format(user_types))

    check = True
    while check:
        if df['Trip Duration'][0] == 489.066:
            break
        else:
            # Display counts of gender
            gender_count = df['Gender'].value_counts()

            print('The number of counts of each gender is \n{}.'.format(gender_count))

            # Display earliest, most recent, and most common year of birth
            # Drop any rows with Nan values.
            df.dropna(axis = 0, subset = ['Birth Year'])

            df = df.sort_values(by = ['Birth Year'])
            print('The earliest year of birth is {}'.format(df['Birth Year'].iloc[0]))

            df = df.sort_values(by = ['Birth Year'], ascending = False)
            print('The most recent year of birth is {}'.format(df['Birth Year'].iloc[0]))

            common_birthyear = df['Birth Year'].mode()[0]
            print('The most common year of birth is {}'.format(common_birthyear))

            check = False 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    count = 0
    check = True
    #creating while loop to keep track whether the user wants to see next five lines.
    while check:
        look_data = input('Do you wish to look at five lines of data yes/no: ')
        if look_data.lower() == 'yes':
            print(df.iloc[count:count+5,:9])
            count += 5
        elif look_data.lower() == 'no':
            break
            check = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

        

    

if __name__ == "__main__":
	main()
