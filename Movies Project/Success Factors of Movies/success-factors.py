"""
Nalu Zou, Yuming Tsang, Jerome Orille
CSE 163
This file will identify what factors contribute to the success of a movie,
which will be defined by high revenue, profit and ratings. Linear regressions
will be analyzed for multiple different features to see if there is a
relationship with success.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statistics import mean


def budget_vs_revenue(df):
    """
    Plots relationship between budget and revenue based on test data
    from linear regressor
    """
    X = [[x] for x in df['budget'].values]
    y = [[x] for x in df['revenue'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Budget vs Revenue')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Budget vs Revenue')
    plt.xlabel('Budget')
    plt.ylabel('Revenue')
    plt.savefig('Budget vs Revenue.png')


def budget_vs_rating(df):
    """
    Plots relationship between budget and ratings based on test data
    from linear regressor
    """
    X = [[x] for x in df['budget'].values]
    y = [[x] for x in df['rating'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Budget vs Rating')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Budget vs Rating')
    plt.xlabel('Budget')
    plt.ylabel('Rating')
    plt.savefig('Budget vs Rating.png')


def year_vs_revenue(df):
    """
    Plots relationship between year and revenue based on test data
    from linear regressor
    """
    X = [[x] for x in df['year'].values]
    y = [[x] for x in df['revenue'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Year vs Revenue')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Year Made vs Revenue')
    plt.xlabel('Year')
    plt.ylabel('Revenue')
    plt.savefig('Year vs Revenue.png')


def runtime_vs_revenue(df):
    """
    Plots relationship between runtime and revenue based on test data
    from linear regressor
    """
    X = [[x] for x in df['runtime'].values]
    y = [[x] for x in df['revenue'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Runtime vs Revenue')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Runtime vs Revenue')
    plt.xlabel('Runtime')
    plt.ylabel('Revenue')
    plt.savefig('Runtime vs Revenue.png')


def year_vs_rating(df):
    """
    Plots relationship between year and rating based on test data
    from linear regressor
    """
    X = [[x] for x in df['year'].values]
    y = [[x] for x in df['rating'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Year vs Rating')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Year Made vs Rating')
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.savefig('Year vs Rating.png')


def runtime_vs_rating(df):
    """
    Plots relationship between runtime and rating based on test data
    from linear regressor
    """
    X = [[x] for x in df['runtime'].values]
    y = [[x] for x in df['rating'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Runtime vs Rating')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Runtime vs Rating')
    plt.xlabel('Runtime')
    plt.ylabel('Rating')
    plt.savefig('Runtime vs Rating.png')


def budget_vs_profit(df):
    """
    Plots relationship between budget and profit based on test data
    from linear regressor
    """
    X = [[x] for x in df['budget'].values]
    y = [[x] for x in df['profit'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Budget vs Profit')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Budget vs Profit')
    plt.xlabel('Budget')
    plt.ylabel('Profit')
    plt.savefig('Budget vs Profit.png')


def year_vs_profit(df):
    """
    Plots relationship between year and profit based on test data
    from linear regressor
    """
    X = [[x] for x in df['year'].values]
    y = [[x] for x in df['profit'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Year vs Profit')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Year Made vs Profit')
    plt.xlabel('Year')
    plt.ylabel('Profit')
    plt.savefig('Year vs Profit.png')


def runtime_vs_profit(df):
    """
    Plots relationship between runtime and profit based on test data
    from linear regressor
    """
    X = [[x] for x in df['runtime'].values]
    y = [[x] for x in df['profit'].values]
    X_test, y_test, y_test_pred = linear_regressor(X, y, 'Runtime vs Profit')

    plt.figure()
    plt.scatter(X_test, y_test, color='green', s=2)
    plt.plot(X_test, y_test_pred, color='black', linewidth=0.5)
    plt.title('Runtime vs Profit')
    plt.xlabel('Runtime')
    plt.ylabel('Profit')
    plt.savefig('Runtime vs Profit.png')


def linear_regressor(X, y, string):
    """
    Trains a model to for linear regression based on one feature
    and one label that is passed in. Returns test data and test
    predictions.
    The code is run many times to compute mean root error to ensure
    consistency in the model's performance and accuracy of results.
    """
    scores = []
    for i in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.2)
        # Create linear regression object
        model = linear_model.LinearRegression()

        # Train the model using the training sets
        model.fit(X_train, y_train)

        y_test_pred = model.predict(X_test)

        score = np.sqrt(mean_squared_error(y_test, y_test_pred))
        scores.append(score)
    print(string + ' root mean squared error:')
    print(mean(scores))

    return (X_test, y_test, y_test_pred)


def main():
    """
    Main method reads in and filters our data, calls the functions
    that will analyze relationships between different features and
    labels, and creates a correlation matrix for all features.
    """
    # read in csv file
    df = pd.read_csv('movies.csv', encoding="ISO-8859-1")

    # filter data
    columns = ['budget', 'gross', 'runtime', 'score', 'year']
    df = df.loc[:, columns]
    df = df.dropna()
    df.rename(columns={'gross': 'revenue'}, inplace=True)
    df.rename(columns={'score': 'rating'}, inplace=True)
    df['profit'] = df['revenue'] - df['budget']

    # create linear regressors for different features
    budget_vs_revenue(df)
    budget_vs_rating(df)
    year_vs_revenue(df)
    runtime_vs_revenue(df)
    year_vs_rating(df)
    runtime_vs_rating(df)
    budget_vs_profit(df)
    year_vs_profit(df)
    runtime_vs_profit(df)

    # create a correlation matrix for all features
    corr = df.corr()
    ax = sns.heatmap(corr, vmin=-0.5, vmax=1, center=0,
                     cmap=sns.diverging_palette(20, 220, n=200), square=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                       horizontalalignment='right')
    plt.title('Correlation Matrix')
    plt.savefig('Correlation Matrix.png')


if __name__ == '__main__':
    main()