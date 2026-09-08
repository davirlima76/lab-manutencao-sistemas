# Lab 2: Documentação, Procedimentos e Plano de Manutenção com IA 📝🤖

Neste laboratório, você aprenderá a planejar intervenções de manutenção de software, registrar procedimentos formais e utilizar **Inteligência Artificial Generativa** como ferramenta de apoio para a escrita assistida de documentação técnica.

---

## 📚 Resumo do Conteúdo da Aula

Para garantir a qualidade e a rastreabilidade do software ao longo do tempo, qualquer intervenção precisa seguir um fluxo estruturado.

### 1. Documentação de Manutenção
É o registro de tudo o que foi alterado, o porquê da mudança, os testes realizados e os impactos esperados. Sem documentação, o sistema torna-se um "código legado sem dono".

### 2. Procedimentos de Manutenção (Passo a Passo)
Fluxo recomendado para realizar uma manutenção segura:
1. **Identificar & Diagnosticar:** Mapear a origem da falha ou necessidade de mudança.
2. **Avaliar Impacto:** Verificar quais módulos do sistema podem ser afetados.
3. **Planejar:** Definir tempo, responsáveis e estratégia de *rollback* (como voltar atrás se der errado).
4. **Implementar & Testar:** Aplicar o ajuste no código e validar os caminhos de execução.
5. **Documentar & Registrar:** Atualizar o histórico de alterações (*Changelog* / Relatório).

### 3. Plano de Manutenção
Documento estruturado que mapeia a saúde do software, prevê manutenções periódicas (preventivas) e estabelece prioridades de execução (crítico, alto, médio, baixo).

---

## 🤖 Competência de IA: Redação Assistida de Documentação

No dia a dia do desenvolvedor, a documentação pode ser agilizada com o uso de **Prompts estruturados**. 

### Estrutura de um Bom Prompt para Documentação Técnica:
* **Contexto:** Papel da IA (ex: *"Atue como um Engenheiro de Software"*).
* **Entrada:** O código ou descrição da tarefa.
* **Instrução Clara:** O que deve ser gerado (ex: *"Gere um relatório de manutenção..."*).
* **Formato desejado:** Estrutura específica (ex: *"Use marcadores com Impacto, Ação e Testes"*).

---

## 💻 Atividade Prática: Estudo de Caso

Imagine que você é responsável pelo sistema de retaguarda de um e-commerce. O sistema apresentou uma falha crítica de segurança no módulo de autenticação e necessita de atualização imediata.

### Código que apresentou problema (`autenticacao.py`):

```python
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
```

---

## 🎯 Desafio Prático: Elaboração do Plano de Manutenção Assistido por IA

Sua missão é utilizar uma ferramenta de IA (ChatGPT, Claude, Gemini, etc.) para auxiliar na criação do **Documento de Plano de Manutenção**.

### Passo 1: Elaborar o Prompt para a IA
Copie o código acima e utilize o modelo de prompt abaixo (ou aprimore-o) na ferramenta de IA de sua preferência:

> **Prompt Sugerido:**
> *"Atue como um Engenheiro de Software responsável pela manutenção de sistemas. Analise o código Python fornecido acima e gere um **Plano de Manutenção de Emergência** contendo:*
> 1. *Tipo de manutenção necessária (Corretiva, Preventiva, etc.) e Justificativa.*
> 2. *Diagnóstico dos problemas e vulnerabilidades encontradas.*
> 3. *Procedimento passo a passo para correção.*
> 4. *Plano de testes recomendados para validar a correção.*
> 5. *Sugestão de refatoração simples do código Python utilizando boas práticas (como hash de senha com biblioteca padrão)."*

### Passo 2: Implementar a Solução
Com base nas orientações geradas pela IA, modifique o arquivo `autenticacao.py` criando a versão corrigida (`autenticacao_corrigido.py`).

---

## 📬 Instruções para Entrega

Envie um e-mail com as seguintes informações:

1. **Prompt Utilizado:** O comando exato que você enviou para a IA.
2. **Plano de Manutenção Gerado:** A documentação técnica gerada com a ajuda da IA.
3. **Código Corrigido:** O arquivo `autenticacao_corrigido.py` funcionando.
4. **Endereço de envio:** `eduardo.hernandes@docente.senai.br`
5. **Assunto do e-mail:** `[Manutenção de Sistemas] Entrega Lab 2 - <Seu Nome Completo>`