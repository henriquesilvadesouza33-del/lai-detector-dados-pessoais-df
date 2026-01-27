```python
#!/usr/bin/env python3
"""
Detector Automático de Dados Pessoais em Pedidos LAI - Desafio Participa DF
Categoria: Acesso à Informação
"""
import re
import pandas as pd
import argparse

class DetectorLAI:
    def __init__(self):
        self.padrao_cpf = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
        self.padrao_rg = r'\b\d{2}\.\d{3}\.\d{3}-\d\b'
        self.padrao_telefone = r'\b\(?\d{2}\)?\s?\d{4,5}-\d{4}\b'
        self.padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    def detectar(self, texto):
        patterns = [self.padrao_cpf, self.padrao_rg, self.padrao_telefone, self.padrao_email]
        for padrao in patterns:
            if re.search(padrao, texto, re.IGNORECASE):
                return True, 0.95
        return False, 0.98
    
    def predict(self, textos):
        return [self.detectar(texto) for texto in textos]

def main():
    parser = argparse.ArgumentParser(description="Detector LAI - CGDF")
    parser.add_argument('--input', default='data/sample.csv')
    parser.add_argument('--output', default='predictions.csv')
    args = parser.parse_args()
    
    detector = DetectorLAI()
    df = pd.read_csv(args.input)
    resultados = detector.predict(df['texto'].tolist())
    
    df['contem_dados_pessoais'] = [r[0] for r in resultados]
    df['confianca'] = [r[1] for r in resultados]
    df.to_csv(args.output, index=False)
    
    print(" Detecção concluída!")
    print(df[['id', 'contem_dados_pessoais', 'confianca']])

if __name__ == "__main__":
    main()
