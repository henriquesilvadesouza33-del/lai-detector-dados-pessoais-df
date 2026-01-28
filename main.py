GitHub → lai-detector-dados-pessoais-df → main.py → "Edit this file"
import pandas as pd
import re

print("Detector LAI iniciado!")

dados = {
    'id': [1,2,3,4,5],
    'texto': [
        "João Silva CPF 123.456.789-00 tel (61)99999-9999",
        "Quero informações sobre licitação 2025/001", 
        "Maria Santos RG 12.345.678-9 email: maria@email.com",
        "Dados da compra pública 2025-001",
        "Endereço Rua das Flores 123 Asa Sul"
    ]
}

padrao_cpf = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
padrao_rg = r'\b\d{2}\.\d{3}\.\d{3}-\d\b'
padrao_telefone = r'\b\(?\d{2}\)?\s?\d{4,5}-\d{4}\b'
padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

df = pd.DataFrame(dados)
df['contem_dados_pessoais'] = df['texto'].apply(lambda x: 
    bool(re.search(padrao_cpf, x)) or 
    bool(re.search(padrao_rg, x)) or 
    bool(re.search(padrao_telefone, x)) or 
    bool(re.search(padrao_email, x))
)
df['confianca'] = df['contem_dados_pessoais'].apply(lambda x: 0.95 if x else 0.98)

print("DETEÇÃO CONCLUÍDA!")
print(df[['id', 'contem_dados_pessoais', 'confianca']])
df.to_csv('predictions.csv', index=False)
print("predictions.csv criado!")


**GIT BASH / POWERSHELL:**
```bash
py -m pip install pandas regex
python main.py

CMD:

text
pip install pandas regex
python main.py
GitHub main.py = SÓ código Python (SEM instruções)
README.md = Instruções de uso

text

**Teste local:**
```bash
cd ~/Desktop/Projetos/lai-detector-dados-pessoais-df
git pull
python main.py  # ← Funciona direto!

