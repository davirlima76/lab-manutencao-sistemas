import time

# Banco de dados simulado do estoque
estoque = {
    "101": {"nome": "Teclado USB", "preco": 100.0, "qtd": 10},
    "102": {"nome": "Mouse Óptico", "preco": 50.0, "qtd": 3},
    "103": {"nome": "Monitor 24'", "preco": 800.0, "qtd": 0}
}

def processar_venda(cod_prod, qtd_desejada):
    # SIMULAÇÃO DE LENTIDÃO / CÓDIGO MORTO
    for _ in range(10000000):
        pass
    
    prod = estoque.get(cod_prod)
    if prod:
        # BUG: Não verifica se a quantidade desejada está disponível no estoque!
        prod["qtd"] -= qtd_desejada
        total = prod["preco"] * qtd_desejada
        print(f"Venda concluída! Total: R$ {total:.2f}")
    else:
        print("Erro: Produto não encontrado!")

def emitir_nota(cod_prod, qtd):
    prod = estoque.get(cod_prod)
    if prod:
        total = prod["preco"] * qtd
        print(f"--- NOTA FISCAL ---")
        print(f"Produto: {prod['nome']} | Qtd: {qtd} | Total: R$ {total:.2f}")
        print(f"-------------------")

# Execução de teste inicial
processar_venda("101", 2)
emitir_nota("101", 2)
