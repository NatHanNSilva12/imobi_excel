import pandas as pd

def generate_excel(data):
    df = pd.DataFrame([data])
    filename = f"contrato_{data['codigoImovel']}.xlsx"
    df.to_excel(filename, index=False)
    return filename
