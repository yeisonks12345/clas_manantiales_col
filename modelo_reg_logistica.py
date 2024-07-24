import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
label_encoder = LabelEncoder()


datos = pd.read_csv('datos_manantiales.csv',sep=';')

features = datos.iloc[:,:5]
scaler = MinMaxScaler()
features=  scaler.fit_transform(features)

target = datos[['CLASIFICACION']]
#target = label_encoder.fit_transform(target)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
# Crear una instancia del modelo de regresión logística
log_reg = LogisticRegression()

# Entrenar el modelo
log_reg.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred = log_reg.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)

# Guardar el modelo
#with open('reg_log_manantiales.pkl', 'wb') as file:
#    pickle.dump(log_reg, file)

#print(f'Accuracy: {accuracy}')
#accuracy del modelo 0.615

#print(features)




