# Módulo de Autenticação Legado
usuarios_db = {
    "admin": "admin123",
    "gerente": "senha456"
}

def login(usuario, senha):
    # FALHA CRÍTICA: Senhas armazenadas e comparadas em texto puro!
    # Falta de logs de tentativa de acesso.
    if usuario in usuarios_db:
        if usuarios_db[usuario] == senha:
            print(f"Acesso liberado para {usuario}")
            return True
    print("Falha na autenticação")
    return False
