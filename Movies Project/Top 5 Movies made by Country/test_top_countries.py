"""
Nalu Zou, Yuming Tsang, Jerome Orille
CSE 163
Tests code from top-countries.py with a smaller dataset.
"""
import pandas as pd
import geopandas as gpd
from top_countries import sort_movies
from top_countries import average_ratings_per_country
from top_countries import top_five_per_country


def main():
    test_data = {'country': ['USA', 'Canada', 'Japan', 'Brazil', 'Canada'],
                 'score': [1, 2, 3, 4, 5]}
    test_df = pd.DataFrame(test_data, columns=['country', 'score'])
    test_df = sort_movies(test_df)
    expected_avg = pd.Series([4.0, 3.5, 3.0, 1.0],
                             ['Brazil', 'Canada', 'Japan', 'USA'])
    expected_max = pd.Series([5, 4, 3, 1],
                             ['Canada', 'Brazil', 'Japan', 'USA'])
    expected_avg.name = 'score'
    expected_max.name = 'score'
    expected_avg = expected_avg.rename_axis('country')
    expected_max = expected_max.rename_axis('country')

    # filter geopandas dataframe to be merged with cvs data
    countries = gpd.read_file('ne_50m_admin_0_countries.shp')
    countries = countries[['NAME', 'geometry']]
    countries.loc[countries['NAME'] == 'United Kingdom', 'NAME'] = 'UK'
    countries.loc[countries['NAME'] == 'United States of America',
                  'NAME'] = 'USA'

    passes_tests = expected_avg.equals(
        average_ratings_per_country(test_df, countries)) and \
        expected_max.equals(top_five_per_country(test_df, countries))
    if passes_tests:
        print('Passes all tests')
    else:
        print('Tests fail')


if __name__ == '__main__':
    main()