#d.Fill NaN with the mean value of the column in the columns: height, weight.

def data_fill_nans(file_name):
    train,test=data_remove_nans(file_name)
    train['height'] = train['height'].fillna(train['height'].mean())
    train['weight'] = train['weight'].fillna(train['weight'].mean())
    test['height'] = test['height'].fillna(test['height'].mean())
    test['weight'] = test['weight'].fillna(test['weight'].mean())
    return train,test