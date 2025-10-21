
def pred_auc_score(file_name):
     #from sklearn.metrics import roc_auc_score, accuracy_score
     train,test=data_predict(file_name)
     # Evaluate performance
     y_train = train['diabetes_mellitus']
     y_test = test['diabetes_mellitus']
     train_auc = roc_auc_score(y_train, train['predictions_prob'])
     #train_accuracy = accuracy_score(y_train, train['predictions'])
     test_auc = roc_auc_score(y_test, test['predictions_prob'])
     #test_accuracy = accuracy_score(y_test, train['predictions'])
     # Print results
     print(f"\nTrain AUC: {train_auc:.4f}\n")
     #print(f"Train Accuracy: {train_accuracy:.4f}")
     print(f"\nTest AUC: {test_auc:.4f}\n")
     #print(f"\nTest Accuracy: {test_accuracy:.4f}")

