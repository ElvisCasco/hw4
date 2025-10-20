#f.Create a binary variable for gender M/F.
def data_binary(file_name):
    train,test= data_encoding(file_name)
    train['gender_M'] = (train['gender'] == 'M').astype(int)
    train['gender_F'] = (train['gender'] == 'F').astype(int)
    test['gender_M'] = (test['gender'] == 'M').astype(int)
    test['gender_F'] = (test['gender'] == 'F').astype(int)
    return train, test
