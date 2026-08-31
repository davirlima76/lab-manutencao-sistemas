# Lab 1: Tipos de Manutenção de Software 🔧

Este laboratório aborda os conceitos fundamentais sobre **Manutenção de Sistemas** e como aplicar na prática os diferentes tipos de manutenção usando a linguagem Python.

---

## 📚 Resumo do Conteúdo da Aula

A manutenção de software não é apenas corrigir problemas. Ela engloba todas as atividades realizadas após a entrega do sistema para manter seu funcionamento, evoluir suas funcionalidades e garantir sua qualidade.

### Os 5 Tipos de Manutenção de Software:

1. 🔴 **Manutenção Corretiva:** Realizada para corrigir bugs, falhas de execução e erros existentes no sistema.
2. 🟢 **Manutenção Preventiva:** Objetiva evitar problemas futuros por meio de limpezas de código, atualizações e testes preliminares.
3. 🔵 **Manutenção Adaptativa:** Adequação do sistema quando ocorrem mudanças no ambiente externo (novas leis, atualização de SO, mudança de banco de dados ou APIs).
4. 🟣 **Manutenção Evolutiva:** Adição de novas funcionalidades e recursos que não existiam no sistema.
5. ⚡ **Manutenção Perfectiva:** Melhorias na qualidade interna do software, como otimização de desempenho, refatoração de código e facilidade de uso, sem alterar a regra de negócio.

---

## 💻 Código Base para o Laboratório

Abaixo está o código de um sistema simplificado de gestão de loja em Python. Ele contém erros, trechos desnecessários e limitações que precisaremos tratar.

Crie um arquivo chamado `sistema_loja.py` e cole o código a seguir:

```python
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
```

---

## 🎯 Desafio Prático

Sua tarefa como desenvolvedor(a) responsável pela manutenção é realizar **4 intervenções** no código `sistema_loja.py`:

### Tarefas a Realizar:

1. 🔴 **Manutenção Corretiva:** 
   Corrija a função `processar_venda`. Atualmente é possível vender mais itens do que o disponível em estoque ou vender quantidades negativas/nulas (`<= 0`). Adicione uma validação que impeça a venda nestes casos e exiba uma mensagem de erro adequada.

2. ⚡ **Manutenção Perfectiva:** 
   Identifique o trecho de código inútil na função `processar_venda` (o laço `for` de simulação) que deixa a execução lenta e remova-o para otimizar o desempenho do programa.

3. 🔵 **Manutenção Adaptativa:** 
   A legislação fiscal mudou e agora toda nota fiscal emitida precisa incluir uma taxa de imposto obrigatória de **10%** sobre o valor total. Modifique a função `emitir_nota` para calcular e exibir o valor do imposto e o valor final com imposto.

4. 🟣 **Manutenção Evolutiva:** 
   O gerente solicitou uma nova funcionalidade no sistema. Crie uma nova função chamada `repor_estoque(cod_prod, qtd)` que permita adicionar novas unidades de um produto existente ao estoque.

---

## 📬 Instruções para Entrega

Após concluir todas as alterações no código:

1. Salve o código final no arquivo `sistema_loja_resolvido.py`.
2. Escreva um pequeno relatório (pode ser no próprio corpo do e-mail) identificando a linha/trecho alterado para cada um dos 4 tipos de manutenção realizados.
3. Envie para o e-mail: **`eduardo.hernandes@docente.senai.br`**
4. **Assunto do e-mail:** `[Manutenção de Sistemas] Entrega Lab 1 - <Seu Nome Completo>`