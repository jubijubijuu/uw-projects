"""
Nalu Zou, Yuming Tsang, Jerome Orille
CSE 163
This file will identify the top five movies with the highest average
rating per country.
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def average_ratings_per_country(df, countries):
    """
    This function analyzes the data based on the average movie ratings per
    country.
    Returns top 5 average movie ratings
    """
    # find mean ratings per country
    df = df.groupby('country')['score'].mean()
    top_5 = df.nlargest(5)

    # plot average ratings by country
    fig, ax = plt.subplots(1)
    countries.plot(ax=ax, color='#EEEEEE')
    scores = countries.merge(df, left_on='NAME', right_on='country',
                             how='outer')
    scores = scores.dropna()
    scores.plot(ax=ax, column='score', legend=True, vmin=0, vmax=10)
    plt.title('Average IMDb Movie Ratings Per Country')
    plt.savefig('top-ratings.png', bbox_inches='tight')

    return top_5


def top_five_per_country(df, countries):
    """
    This function analyzes the data based on the top movie per country.
    Gives good overview of how top hits from each country compare.
    Returns top 5 highest ratings
    """
    # find top rating per country
    df = df.groupby('country')['score'].max()
    top_5 = df.nlargest(5)

    # plot top ratings by country
    fig, ax = plt.subplots(1)
    countries.plot(ax=ax, color='#EEEEEE')
    scores = countries.merge(df, left_on='NAME', right_on='country',
                             how='outer')
    scores = scores.dropna()
    scores.plot(ax=ax, column='score', legend=True, vmin=0, vmax=10)
    plt.title('Top IMDb Movie Rating Per Country')
    plt.savefig('top-movie.png', bbox_inches='tight')

    return top_5


def sort_movies(df):
    """
    Returns dataframe sorted by country and score
    """
    df = df.sort_values(['country'], ascending=True) \
        .groupby(['country'], sort=False) \
        .apply(lambda x: x.sort_values(['score'], ascending=False)) \
        .reset_index(drop=True)
    return df


def main():
    """
    Main method reads in and filters movie data, turns it into a
    geopandas dataframe, and produces plots based on ratings
    in different countries.
    """
    # read in csv file
    df = pd.read_csv('movies.csv', encoding="ISO-8859-1")

    # filter data
    columns = ['country', 'name', 'score']
    df = df.loc[:, columns]

    # sort movies by country
    df = sort_movies(df)

    # filter geopandas dataframe to be merged with cvs data
    countries = gpd.read_file('ne_50m_admin_0_countries.shp')
    countries = countries[['NAME', 'geometry']]
    countries.loc[countries['NAME'] == 'United Kingdom', 'NAME'] = 'UK'
    countries.loc[countries['NAME'] == 'United States of America',
                  'NAME'] = 'USA'

    # produce plots and print top 5 average and highest ratings
    print("Top 5 Average Movie Ratings:")
    print(average_ratings_per_country(df, countries))
    print("Top 5 Highest Ratings")
    print(top_five_per_country(df, countries))


if __name__ == '__main__':
    main()