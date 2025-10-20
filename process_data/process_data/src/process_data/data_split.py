#b. Split the data between train and test

def data_split(data):
    data=data_loader(file_name)
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    return train,test 




