class automovel:
    """Classe que representa um automóvel com controlo de combustível e autonomia."""
    
    def __init__(self, cap_dep, quant_comb, consumo):
        """
        Inicializa o automóvel.
        cap_dep: capacidade do depósito em litros
        quant_comb: quantidade inicial de combustível em litros
        consumo: consumo em litros aos 100 km
        """
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo
    
    def combustivel(self):
        """Devolve a quantidade de combustível no depósito."""
        return self.quant_comb
    
    def autonomia(self):
        """Devolve o número de Km que é possível percorrer com o combustível no depósito."""
        if self.consumo == 0:
            return 0
        return int((self.quant_comb / self.consumo) * 100)
    
    def abastece(self, n_litros):
        """
        Aumenta em n_litros o combustível no depósito e retorna a autonomia.
        Se exceder a capacidade, gera erro e não aumenta o combustível.
        """
        if self.quant_comb + n_litros > self.cap_dep:
            raise ValueError("Abastecimento excede a capacidade do depósito!")
        
        self.quant_comb += n_litros
        return self.autonomia()
    
    def percorre(self, n_km):
        """
        Percorre n_km, desde que o combustível permita.
        Se não permitir, gera erro e o trajeto não é efetuado.
        Retorna a autonomia ou -1 em caso de erro.
        """
        combustivel_necessario = (n_km / 100) * self.consumo
        
        if combustivel_necessario > self.quant_comb:
            return -1
        
        self.quant_comb -= combustivel_necessario
        return self.autonomia()

def exibe_estado(carro):
    """Exibe o estado atual do automóvel."""
    print(f"\n--- Estado do Automóvel ---")
    print(f"Combustível no depósito: {carro.combustivel():.1f} litros")
    print(f"Capacidade do depósito: {carro.cap_dep} litros")
    print(f"Consumo: {carro.consumo} L/100km")
    print(f"Autonomia atual: {carro.autonomia()} km")
    print("-" * 30)

def main():
    """Função principal com menu interativo."""
    print("=== Gestão de Automóvel ===")
    print("Vamos criar o seu automóvel!")
    
    # Criação do automóvel
    try:
        cap_dep = float(input("Capacidade do depósito (litros): "))
        quant_comb = float(input("Quantidade inicial de combustível (litros): "))
        consumo = float(input("Consumo (litros aos 100 km): "))
        
        carro = automovel(cap_dep, quant_comb, consumo)
        print("\nAutomóvel criado com sucesso!")
        
    except ValueError:
        print("Erro: Valores inválidos inseridos!")
        return
    
    # Menu principal
    while True:
        exibe_estado(carro)
        print("\nEscolha uma opção:")
        print("1. Ver combustível")
        print("2. Ver autonomia")
        print("3. Abastecer")
        print("4. Percorrer distância")
        print("5. Sair")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "1":
            print(f"\nCombustível no depósito: {carro.combustivel():.1f} litros")
            
        elif opcao == "2":
            print(f"\nAutonomia atual: {carro.autonomia()} km")
            
        elif opcao == "3":
            try:
                litros = float(input("\nQuantos litros deseja abastecer? "))
                nova_autonomia = carro.abastece(litros)
                print(f"✅ Abastecimento realizado!")
                print(f"Nova autonomia: {nova_autonomia} km")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("❌ Erro: Insira um número válido!")
                else:
                    print(f"❌ Erro: {e}")
            
        elif opcao == "4":
            try:
                km = float(input("\nQuantos km deseja percorrer? "))
                resultado = carro.percorre(km)
                if resultado == -1:
                    print("❌ Erro: Combustível insuficiente para percorrer essa distância!")
                else:
                    print(f"✅ Viagem realizada!")
                    print(f"Autonomia restante: {resultado} km")
            except ValueError:
                print("❌ Erro: Insira um número válido!")
                
        elif opcao == "5":
            print("\nObrigado por usar o sistema de gestão do automóvel!")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
