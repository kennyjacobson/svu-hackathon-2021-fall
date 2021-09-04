from covid import covid_dal

def summarize_data():
    df = covid_dal.get_covid_countries_total_deaths()
    print(df)