#c.Remove those rows that contain NaN values in the columns: age, gender, ethnicity.

def data_remove_nans(file_name):
    train,test=data_split(file_name)
    train = train.dropna(subset=['age', 'gender', 'ethnicity'])
    test = test.dropna(subset=['age', 'gender', 'ethnicity'])
    return train,test

