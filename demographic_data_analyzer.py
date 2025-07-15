import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex == 'Male'].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df.education == 'Bachelors'].shape[0]/df.shape[0]*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    con1 = df.education.isin(advanced)
    con2 = df.salary == '>50K'
    higher_education = len(df[con1 & con2])
    lower_education = len(df[~con1 & con2])

    # percentage with salary >50K
    higher_education_rich = round(len(df[con1 & con2])/len(df[con1])*100,1)
    lower_education_rich = round(len(df[~con1 & con2])/len(df[~con1])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    con3 = df['hours-per-week'] == min_work_hours
    num_min_workers = len(df[con3])

    rich_percentage = round(len(df[con2 & con3])/len(df[con3])*100,1)

    # What country has the highest percentage of people that earn >50K?
    S1 = pd.DataFrame(df['native-country'].value_counts())
    S1.columns = ['total_pop']
    S1['rich_pop'] = df.loc[con2, 'native-country'].value_counts()
    S1['rich_pct'] = S1['rich_pop']/S1['total_pop']*100
    highest = S1.sort_values(by='rich_pct', ascending=False).head(1)
    # df[con2].loc['native-country'].value_counts()
    highest_earning_country = highest.index.item()
    highest_earning_country_percentage = round(highest.iloc[:,-1].item(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    con4 = df['native-country'] =='India'
    top_IN_occupation = df.loc[con2 & con4, 'occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
