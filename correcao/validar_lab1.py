# ==============================================================================
# SCRIPT DE VALIDAÇÃO AUTOMÁTICA — LAB 1 (PROFESSOR / CORREÇÃO)
# Disciplina: Manutenção de Sistemas
# Professor: Eduardo Hernandes
# ==============================================================================
#
# COMO USAR:
# 1. Coloque o arquivo 'sistema_loja_resolvido.py' do aluno na mesma pasta.
# 2. Execute via terminal: python validar_lab1.py
#
# ==============================================================================

import sys
import time
import importlib.util

def carregar_modulo_aluno(nome_arquivo="sistema_loja_resolvido.py"):
    try:
        spec = importlib.util.spec_from_file_location("aluno_script", nome_arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo
    except FileNotFoundError:
        print(f"❌ ERRO CRÍTICO: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"❌ ERRO DE EXECUÇÃO/SINTAXE no arquivo do aluno: {e}")
        return None

def validar_lab1():
    print("=" * 60)
    print(" 🛠️  INICIANDO BATERIA DE TESTES DE VALIDAÇÃO DA ENTREGA (LAB 1)")
    print("=" * 60)

    aluno = carregar_modulo_aluno()
    if not aluno:
        sys.exit(1)

    pontuacao = 0
    total_testes = 4

    # 1. Manutenção Perfectiva
    print("\n[1/4] Testando Manutenção Perfectiva (Remoção do laço de lentidão)...")
    if hasattr(aluno, 'processar_venda'):
        inicio = time.time()
        aluno.processar_venda("101", 1)
        tempo_decorrido = time.time() - inicio

        if tempo_decorrido < 0.5:
            print("  ✅ PASSOU: A função executou instantaneamente (< 0.5s).")
            pontuacao += 1
        else:
            print(f"  ❌ FALHOU: A função demorou {tempo_decorrido:.2f}s. Laço inútil mantido.")
    else:
        print("  ❌ FALHOU: Função 'processar_venda' não encontrada.")

    # 2. Manutenção Corretiva
    print("\n[2/4] Testando Manutenção Corretiva (Validação de quantidades e estoque)...")
    if hasattr(aluno, 'processar_venda') and hasattr(aluno, 'estoque'):
        qtd_inicial = aluno.estoque.get("102", {}).get("qtd", 0)
        aluno.processar_venda("102", -1)
        aluno.processar_venda("102", 0)
        aluno.processar_venda("102", qtd_inicial + 50)
        qtd_final = aluno.estoque.get("102", {}).get("qtd", 0)

        if qtd_inicial == qtd_final:
            print("  ✅ PASSOU: Estoque mantido intacto em vendas inválidas.")
            pontuacao += 1
        else:
            print("  ❌ FALHOU: Permitiu venda com estoque insuficiente/inválido!")
    else:
        print("  ❌ FALHOU: Estrutura ausente.")

    # 3. Manutenção Adaptativa
    print("\n[3/4] Testando Manutenção Adaptativa (Emissão de Nota / Imposto)...")
    if hasattr(aluno, 'emitir_nota'):
        try:
            import io
            from contextlib import redirect_stdout

            f = io.StringIO()
            with redirect_stdout(f):
                aluno.emitir_nota("101", 1)
            saida = f.getvalue().lower()

            if "imposto" in saida or "taxa" in saida or "10%" in saida or "110" in saida:
                print("  ✅ PASSOU: 'emitir_nota' incluiu cálculo de imposto/legislação fiscal.")
                pontuacao += 1
            else:
                print("  ❌ FALHOU: Menção a imposto/novo valor não encontrada.")
        except Exception as e:
            print(f"  ❌ FALHOU ao executar 'emitir_nota': {e}")
    else:
        print("  ❌ FALHOU: Função 'emitir_nota' não encontrada.")

    # 4. Manutenção Evolutiva
    print("\n[4/4] Testando Manutenção Evolutiva (Função repor_estoque)...")
    if hasattr(aluno, 'repor_estoque') and hasattr(aluno, 'estoque'):
        try:
            qtd_antes = aluno.estoque.get("103", {}).get("qtd", 0)
            aluno.repor_estoque("103", 5)
            qtd_depois = aluno.estoque.get("103", {}).get("qtd", 0)

            if qtd_depois == (qtd_antes + 5):
                print(f"  ✅ PASSOU: 'repor_estoque' incrementou de {qtd_antes} para {qtd_depois}.")
                pontuacao += 1
            else:
                print(f"  ❌ FALHOU: Incremento incorreto. Esperado: {qtd_antes + 5}, Obtido: {qtd_depois}.")
        except Exception as e:
            print(f"  ❌ FALHOU ao executar 'repor_estoque': {e}")
    else:
        print("  ❌ FALHOU: Função 'repor_estoque' não encontrada.")

    # RESULTADO
    print("\n" + "=" * 60)
    print(f" RESULTADO FINAL: {pontuacao}/{total_testes} TESTES APROVADOS")
    print("=" * 60)
    if pontuacao == total_testes:
        print(" 🎉 PARABÉNS! A entrega atendeu a 100% dos requisitos de manutenção.\n")
    else:
        print(" ⚠️ ATENÇÃO: Requisitos pendentes detectados.\n")

if __name__ == "__main__":
    validar_lab1()
