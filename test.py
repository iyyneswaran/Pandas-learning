import pandas as pd

patients = {
    'patient_id': [1],
    'patient_name ': ['Daniel'],
    'conditions ': ['SADIAB100']
}

df = pd.DataFrame(patients)
print(df)

df['check'] = patients[patients['conditions '].str.find('D')]