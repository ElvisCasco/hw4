#e.Generate dummies for ethnicity column (One hot encoding).
def data_encoding(file_name):
    train,test=data_fill_nans(file_name)
    train = pd.get_dummies(train, columns=['ethnicity'], drop_first=True)
    test = pd.get_dummies(test, columns=['ethnicity'], drop_first=True)
    return train,test
