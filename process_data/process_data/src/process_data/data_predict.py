#g.& h. Predict the targets for both the train and test sets and add the prediction as a new column 
def data_logistic_model(file_name):
     # Get the logistic regression model using training data 
     train,test=data_binary(file_name)
     #from sklearn.linear_model import LogisticRegression
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
     return X_train,y_train,X_test,y_test,model

def data_predict(file_name): 
     train,test=data_binary(file_name)
     X_train,y_train,X_test,y_test,model=data_logistic_model(file_name)
     # Predict class labels and probabilities 
     train['predictions'] = model.predict(X_train)
     train['predictions_prob'] = model.predict_proba(X_train)[:, 1]
     test['predictions'] = model.predict(X_test)
     test['predictions_prob'] = model.predict_proba(X_test)[:, 1]
     return train,test
