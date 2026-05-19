import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
def load_sample_data():
    np.random.seed(42)
    data = {
        'idade': np.random.randint(18, 65, 500),
        'salario': np.random.normal(5000, 1500, 500).round(2),
        'experiencia': np.random.randint(0, 35, 500),
        'nivel_educacao': np.random.choice(['Fundamental', 'Médio', 'Superior', 'Pós'], 500),
        'departamento': np.random.choice(['TI', 'RH', 'Financeiro', 'Marketing', 'Operações'], 500),
        'satisfacao': np.random.randint(1, 11, 500)
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = load_sample_data()
    print(df.head())
    df.to_csv('data/sample_data.csv', index=False)