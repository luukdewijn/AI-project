from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def train_and_evaluate(X, y):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a RandomForestClassifier
    forest = RandomForestClassifier(random_state=1)

    # Create the MultiOutputClassifier
    multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)

    # Train the model
    multi_target_forest.fit(X_train, y_train)

    # Now you can use this model to predict
    predictions = multi_target_forest.predict(X_test)

    # Evaluate the model
    for i in range(y_test.shape[1]):
        print(f"Classification report for output {i+1}:")
        print(classification_report(y_test[:, i], predictions[:, i]))

    return multi_target_forest