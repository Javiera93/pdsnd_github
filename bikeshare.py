import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citys = ('chicago', 'new york', 'washington')
    while True:
        city = input('What city will you choose: Chicago, New York City or Washington? \n>').lower()

        if city in citys:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Enter month {} \n>'.format(months)).lower()
        
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
         day = input('Enter day {} \n>'.format(days)).lower()

         if day in days:
            break
            
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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])  
    
    df["month"] = df['Start Time'].dt.month                 
    df["day_of_week"] = df['Start Time'].dt.weekday_name       
    df["hour"] = df['Start Time'].dt.hour             
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_1 = months.index(month) + 1        
        df = df[df["month"] == month_1 ]                

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df
  
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_mode = df["month"].mode()[0] -1
    common_month = months[month_mode].title()
    print("Most common month: ", common_month)
    
    # TO DO: display the most common day of week
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    common_day = df["day_of_week"].mode()[0]
    print("Most common day: ", common_day)
    
    # TO DO: display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("Most common hour: ", common_hour)  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_used = df['Start Station'].mode()[0]
    print("The most used start station is: ", most_start_used)

    # TO DO: display most commonly used end station
    most_end_used = df['End Station'].mode()[0]
    print("The most used end station: ", most_end_used)

    # TO DO: display most frequent combination of start station and end station trip
    df["Start_End"] = df['Start Station'].astype(str) + ' & ' + df['End Station']
    most_common_combination = df["Start_End"].mode()[0]
    print("The most frequent combination of Start and End Stationn: ", most_common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    time_total_travel = df['Trip Duration'].sum()
    print("Total travel time is:", time_total_travel)

    # TO DO: display mean travel time
    time_mean = df['Trip Duration'].mean()
    time_mean_travel = int(time_mean)
    print("Average travel time is:", time_mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_types_user = df["User Type"].value_counts()
    print("The count of user types is:", count_types_user) 

    # TO DO: Display counts of gender
    if "Gender" in df:
        count_gender = df['Gender'].value_counts()
        print("The count of gender:", count_gender) 
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("Earliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].mode()[0]) 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
     
def display_data(df):
    while True:
         resp = input('Do you want to see raw data? Enter yes or no \n>').lower()
            
         if resp == 'yes':
             print(df.iloc[:5])
         if resp != 'yes':
             break
                         
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