#g.& h. Predict the targets for both the train and test sets and add the prediction as a new column 

def data_train_models(file_name): 
    train,test=data_binary(file_name)
    from sklearn.linear_model import LogisticRegression
    features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
            'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    X_train = train[features]
    y_train = train['diabetes_mellitus']
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_proba = model.predict_proba(X_test_std)[:, 1]
    

    return model

    
