from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

modelo_supervisionado = KNeighborsClassifier(n_neighbors=3)
modelo_supervisionado.fit(X_train, y_train)

previsoes = modelo_supervisionado.predict(X_test)

acuracia = accuracy_score(y_test, previsoes)
print(f'Acurácia do modelo supervisionado: {acuracia:.2f}')
