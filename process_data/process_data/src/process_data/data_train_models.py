#g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) 

def data_train_models(file_name): 
    train,_=data_binary(file_name)
    from sklearn.linear_model import LogisticRegression
    features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
            'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    X_train = train[features]
    y_train = train['diabetes_mellitus']
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

    


    
    
    
    
    
    
