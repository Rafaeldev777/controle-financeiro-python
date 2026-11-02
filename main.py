# ==========================================
# Projeto: Controle Financeiro Pessoal
# Linguagem: Python
# ==========================================

saldo_atual = 0.0
transacoes = []

def exibir_menu():
    print("\n==============================")
    print("      CONTROLE FINANCEIRO     ")
    print("==============================")
    print("1. Adicionar Receita (Entrada)")
    print("2. Adicionar Despesa (Saída)")
    print("3. Ver Saldo e Extrato")
    print("4. Sair")
    print("==============================")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        valor = float(input("Digite o valor da receita (R$): "))
        descricao = input("Descrição da receita (ex: Salário, freela): ")
        saldo_atual += valor
        transacoes.append({"tipo": "Receita", "valor": valor, "desc": descricao})
        print(f"✅ Receita de R$ {valor:.2f} adicionada com sucesso!")

    elif opcao == "2":
        valor = float(input("Digite o valor da despesa (R$): "))
        descricao = input("Descrição da despesa (ex: Aluguel, mercado): ")
        saldo_atual -= valor
        transacoes.append({"tipo": "Despesa", "valor": valor, "desc": descricao})
        print(f"❌ Despesa de R$ {valor:.2f} registada.")

    elif opcao == "3":
        print("\n--- EXTRATO FINANCEIRO ---")
        print(f"Saldo Atual: R$ {saldo_atual:.2f}")
        print("Histórico de Movimentações:")
        if not transacoes:
            print("Nenhuma transação registada ainda.")
        else:
            for t in transacoes:
                sinal = "+" if t["tipo"] == "Receita" else "-"
                print(f"[{t['tipo']}] {t['desc']}: {sinal}R$ {t['valor']:.2f}")
        print("--------------------------")

    elif opcao == "4":
        print("\nA sair do programa. Até logo!")
        break
    else:
        print("⚠️ Opção inválida! Escolha um número de 1 a 4.")
