"""
Nalu Zou, Yuming Tsang, Jerome Orille
CSE 163
Trains a model to predict movie success (revenue) based on various factors.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


def main():
    sns.set()
    df = pd.read_csv('movies.csv', encoding="ISO-8859-1")
    columns = ['budget', 'company', 'country', 'director', 'genre', 'gross',
               'rating', 'runtime', 'score', 'star', 'writer', 'year']
    scores = []
    test_sizes = []
    for i in range(300):
        sample = df.sample(n=1000)
        filtered = sample.loc[:, columns]
        filtered.dropna()
        X = filtered.loc[:, (filtered.columns != 'gross')]
        X = pd.get_dummies(X)
        y = filtered['gross']
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.2)
        model = DecisionTreeRegressor()

        # train on the training features and labels
        model.fit(X_train, y_train)

        # test on the test set
        y_pred = model.predict(X_test)

        score = mean_squared_error(y_test, y_pred)
        print("Accuracy Score", model.get_depth(), score)
        test_sizes.append(model.get_depth())
        scores.append(score)
    score_df = pd.DataFrame({'scores': scores, 'test_sizes': test_sizes})
    sns.relplot(x='test_sizes', y='scores', data=score_df, kind='line')
    plt.title('Mean Squared Error vs Decision Tree Depth')
    plt.xlabel('Decision Tree Depth')
    plt.ylabel('Mean Squared Error')
    plt.savefig('movie_success_prediction.png', bbox_inches='tight')


if __name__ == '__main__':
    main()