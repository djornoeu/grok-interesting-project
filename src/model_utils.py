# Utilitários para modelos

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    y_pred = model.predict(X_test)
    print(f'Acurácia: {accuracy_score(y_test, y_pred):.2f}')
    return y_pred
