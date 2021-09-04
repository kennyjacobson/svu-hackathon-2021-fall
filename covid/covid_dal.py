# pylint: disable=import-error
import pandas as pd 

def get_covid_df():
    df = pd.read_csv('./data/owid-covid-data.csv')
    print("df", df.shape)
    return df

def get_covid_countries_only_df():
    all_df = get_covid_df()
    countries_df = all_df[all_df.continent.notnull()]
    print("countries_df",countries_df.shape)
    return countries_df

def get_covid_countries_total_deaths():
    countries_df = get_covid_countries_only_df()
    death_sum_df = countries_df.groupby("location")["new_deaths"].sum()
    print(death_sum_df)
    return death_sum_df


