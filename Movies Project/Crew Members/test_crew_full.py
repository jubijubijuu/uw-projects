'''
Nalu Zou, Yuming Tsang, Jerome Orille
3/13/20
Project Part 2 - Crew Member Data Wrangling
This is a test file used for testing similar code
in 'dept_info.py' and 'crew_info.py.'
'''

from test_util import assert_equals
from crew_dept_info import populate_department, total_department
import pandas as pd
from ast import literal_eval


def main():
    # Import data
    crew = pd.read_csv('crew_info.csv')

    # Randomly get one row
    sample = crew.sample()

    # Change data type of values in 'crew' column
    # from string to list of dictionaries
    member = sample['crew']
    member = member.apply(literal_eval)

    # Populate crew type information
    sample['department'] = member.apply(populate_department)
    count_departments = total_department(sample['department'])
    print(count_departments)
    tot_crew_types = count_departments['Count'].sum()

    # Populate information for total number of crew members
    sample['total_crew'] = member.apply(lambda x: len(x))
    count_total_crew = sample[['title', 'total_crew']]
    count_total_crew = count_total_crew.rename(
        columns={'title': 'Movie', 'total_crew': 'Total Crew per Movie'})
    print(count_total_crew)
    tot_crew = count_total_crew['Total Crew per Movie'].sum()

    # Check to see if number of crew types matches total crew
    print('Checking number of crew types to total crew...')
    assert_equals(tot_crew_types, tot_crew)
    print('Total count from count_departments: ' + str(tot_crew_types))
    print('Total count from count_total_crew: ' + str(tot_crew))


if __name__ == '__main__':
    main()