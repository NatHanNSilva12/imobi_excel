from supabase import create_client
from config import config

supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)

def save_to_supabase(data):
    response = supabase.table('imoveis').insert({
        'nome_cliente': data['nomeCliente'],
        'codigo_imovel': data['codigoImovel'],
        'data_inicio': data['dataInicio'],
        'data_fim': data['dataFim'],
        'endereco': data['endereco'],
        'telefone_proprietario': data['telefoneProprietario'],
        'status': data['status']
    }).execute()
    return response