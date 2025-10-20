#g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) 

def data_predict(file_name): 
     train,test=data_binary(file_name)
     from sklearn.linear_model import LogisticRegression
     features = [
         'age', 'height', 'weight', 'aids', 'cirrhosis',
          'hepatic_failure','immunosuppression', 'leukemia', 
          'lymphoma', 'solid_tumor_with_metastasis']
     # Get features and target variables
     X_train = train[features]
     y_train = train['diabetes_mellitus']
     X_test = test[features]
     y_test = test['diabetes_mellitus']
     # Fit the model with training data
     model = LogisticRegression(max_iter=1000)
     model.fit(X_train, y_train)
     # Predict class labels and probabilities on test data
     y_pred = model.predict(X_test)
     y_proba = model.predict_proba(X_test)[:, 1]

    


    
    
    
    
    
    
