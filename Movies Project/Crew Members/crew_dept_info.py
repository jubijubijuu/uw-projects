'''
Nalu Zou, Yuming Tsang, Jerome Orille
3/13/20
Project Part 2 - Crew Member Data Wrangling
This file produces two graphs that show information
about the top ten grossing movies. The information
includes the total number of crew members per movie,
and the total number of crew members throughout
various departments, such as visual effects, of the movies.
'''
import pandas as pd
from ast import literal_eval
import seaborn as sns
import matplotlib.pyplot as plt


def populate_department(row):
    '''
    Takes in a list of dictionaries containing information
    about crew members in movies and their departments, and
    returns a dictionary that contains each department
    and the amount of crew members in each department.
    '''
    result = dict()
    for x in row:
        dept = x['department']
        if dept not in result:
            result[dept] = 1
        else:
            result[dept] += 1
    return result


def total_department(col):
    '''
    Takes in a series of dictionaries and returns a
    new dataframe containing crew types and their total counts.
    '''
    result = col.apply(pd.Series).sum()
    result = pd.DataFrame({'Department': result.index, 'Count': result.values})
    return result


def plot_dept_info(data):
    '''
    Takes in a pandas dataframe and plots a bar graph showing
    the total amount of crew members per movie.
    '''
    # Plot a bar chart, comparing the count of each crew member in
    # each department
    fig, ax1 = plt.subplots(1)
    ax = sns.barplot(x='Count',
                     y='Department',
                     orient='h',
                     data=data,
                     ax=ax1)

    # Add labels to bar plot
    for col in ax.patches:
        width = col.get_width()
        ax.annotate('{:.0f}'.format(width),
                    (width + 10, col.get_y() + 0.6),
                    ha='center',
                    va='bottom',
                    color='black')
    plt.title('Department Information from Top Ten Grossing Movies')
    plt.xlabel('Count of Crew Members')
    plt.ylabel('Department')
    plt.savefig('department_graph.png', bbox_inches='tight')


def plot_crew_info(data):
    '''
    Takes in a pandas dataframe and plots a bar graph showing
    the total amount of crew members per movie.
    '''
    # Plot a bar chart, comparing the top ten grossing
    # movies with their total amount of crew members
    fig, ax2 = plt.subplots(1)
    ax = sns.barplot(x='Total Crew per Movie',
                     y='Movie',
                     orient='h',
                     data=data,
                     ax=ax2)

    # Add labels to bar plot
    for col in ax.patches:
        width = col.get_width()
        ax.annotate('{:.0f}'.format(width),
                    (width + 10, col.get_y() + 0.6),
                    ha='center',
                    va='bottom',
                    color='black')
    plt.title('Crew Member Information from Top Ten Grossing Movies')
    plt.xlabel('Crew Members')
    plt.ylabel('Movie')
    plt.savefig('crew_graph.png', bbox_inches='tight')


def main():
    # Files into variables
    crew = pd.read_csv('credits.csv')
    movies = pd.read_csv('movies.csv', encoding='ISO-8859-1')
    metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

    # Fix ID values of metadata
    # Some ID values were messed up and had dates on them...
    remove_data = metadata['id'].str.contains('-')
    metadata['id'] = metadata.loc[~remove_data, ['id']]
    metadata = metadata.dropna()
    metadata['id'] = metadata['id'].astype(int)

    # Join datasets
    # The movies are from movies.csv, the smaller dataset
    # The crew members are from the metadata csv, which contains
    # information about the crew members in the smaller dataset
    join_mov = movies.merge(metadata,
                            left_on='name',
                            right_on='original_title')
    crew_metadata = crew.merge(join_mov,
                               left_on=crew['id'],
                               right_on=join_mov['id'])

    # Filter data for top ten movies by gross income
    crew_metadata = crew_metadata[['crew', 'gross', 'title']]
    crew_metadata = crew_metadata.nlargest(10, 'gross')

    # Write dataframe to new .csv file
    crew_metadata.to_csv('crew_info.csv', index=False)

    # Change values of the crew column
    # Each row would change from a string to a list of dictionaries
    # Each list represents the cast of a movie
    # Each dictionary represents one cast member of a movie
    member = crew_metadata['crew']
    member = member.apply(literal_eval)

    # Count the number of crew members per department
    department = member.apply(populate_department)
    num_of_departments = total_department(department)

    # Count up total crew members per movie
    crew_metadata['crew_per_movie'] = member.apply(lambda x: len(x))
    crew_per_mov = crew_metadata[['title', 'crew_per_movie']]
    crew_per_mov = crew_per_mov.rename(
        columns={'title': 'Movie',
                 'crew_per_movie': 'Total Crew per Movie'})

    # Plot bar graphs
    plot_dept_info(num_of_departments)
    plot_crew_info(crew_per_mov)


if __name__ == '__main__':
    main()