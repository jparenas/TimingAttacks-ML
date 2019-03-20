import pandas as pd
from sklearn.model_selection import train_test_split


train_test_ratio = (4, 1)


if __name__ == '__main__':
    df = pd.read_csv('../data/stats_train_v2.csv')
    #print(df.head())
    #print(df.shape)  # 60,000

    X_train, X_test, y_train, y_test = train_test_split(
        df[['length', 'time', 'time_mean', 'time_stdev']], df['algo'],
        test_size=train_test_ratio[1]/sum(train_test_ratio),
        random_state=42
    )

    train = pd.concat([X_train, y_train], axis=1)
    test = pd.concat([X_test, y_test], axis=1)

    train.to_csv('../data/final_train.csv', index=False)
    test.to_csv('../data/final_test.csv', index=False)
