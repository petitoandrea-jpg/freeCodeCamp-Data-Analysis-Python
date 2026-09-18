import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leggi i dati dal file CSV
    df = pd.read_csv('adult.data.csv')

    # 1. Quante persone di ogni razza sono rappresentate in questo dataset?
    race_count = df['race'].value_counts()

    # 2. Qual è l'età media degli uomini?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Qual è la percentuale di persone che hanno una laurea triennale (Bachelors)?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4 & 5. Percentuale di persone con/senza istruzione avanzata che guadagnano >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentuale con istruzione avanzata che guadagna >50K
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # Percentuale senza istruzione avanzata che guadagna >50K
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Qual è il numero minimo di ore che una persona lavora a settimana?
    min_work_hours = df['hours-per-week'].min()

    # 7. Qual è la percentuale di persone che lavorano il numero minimo di ore e guadagnano >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Quale paese ha la percentuale più alta di persone che guadagnano >50K e qual è questa percentuale?
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich_counts / country_counts) * 100

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Individua l'occupazione più popolare tra chi guadagna >50K in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
        .value_counts()
        .idxmax()
    )

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation,
    }