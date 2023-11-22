import matplotlib.pyplot as plt

class PolinomioManipulador:
    def __init__(self):
        self.polinomios = []

    def criar_polinomio_interativamente(self):
        grau = int(input("Introduza o grau do polinómio: "))
        coeficientes = [float(input(f"Introduza o coeficiente para x^{i}: ")) for i in range(grau, -1, -1)]
        self.polinomios.append(tuple(coeficientes))
        print("Polinómio criado com sucesso!")

    def ler_polinomios_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    coeficientes = [float(coef) for coef in linha.strip().split()]
                    self.polinomios.append(tuple(coeficientes))
            print("Polinómios carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    def listar_polinomios(self):
        print("Listagem de Polinómios:")
        print("Número | Coeficientes")
        for i, polinomio in enumerate(self.polinomios):
            print(f"{i + 1}      | {polinomio}")

    def calcular_valor_em_ponto(self):
        self.listar_polinomios()
        num_ordem = int(input("Introduza o número de ordem do polinómio: ")) - 1
        ponto = float(input("Introduza o valor do ponto: "))
        
        polinomio = self.polinomios[num_ordem]
        # Calcular o valor do polinômio no ponto usando a abordagem manual
        resultado = 0
        for grau, coeficiente in enumerate(polinomio[::-1]):
            resultado += coeficiente * (ponto ** grau)
        
        print(f"O valor do polinómio {num_ordem + 1} em {ponto} é {resultado}")

    def listar_polinomios_com_grau(self):
        print("Listagem de Polinómios:")
        print("Número | Coeficientes | Grau")
        for i, polinomio in enumerate(self.polinomios):
            grau = len(polinomio) - 1
            print(f"{i + 1}      | {polinomio}      | {grau}")

    def mostrar_maior_grau(self):
        graus = [len(p) - 1 for p in self.polinomios]
        indice_maior_grau = np.argmax(graus)
        maior_grau = graus[indice_maior_grau]
        print(f"O polinómio de maior grau é o {indice_maior_grau + 1} com grau {maior_grau}")
    
    def calcula_derivada(self, polinomio):
        derivadas = []
        for i in range(len(polinomio) - 1, 0, -1):
            derivadas.append(i * polinomio[i])
        return tuple(derivadas[::-1])

    def mostrar_derivadas(self):
        print("Tabela de Derivadas:")
        print("Número | Polinómio Original | Derivada")
        for i, polinomio in enumerate(self.polinomios):
            derivada = self.calcula_derivada(polinomio)
            print(f"{i + 1}      | {polinomio}           | {derivada}")
    
    def adiciona_poli(self):
        self.listar_polinomios()
        num_ordem1 = int(input("Introduza o número de ordem do primeiro polinómio: ")) - 1
        num_ordem2 = int(input("Introduza o número de ordem do segundo polinómio: ")) - 1
        p1 = self.polinomios[num_ordem1]
        p2 = self.polinomios[num_ordem2]
        # resultado tuple vazio
        resultado = ()
        tamanho_poli1 = len(p1)
        tamanho_poli2 = len(p1)
        maior_grau = max(tamanho_poli1, tamanho_poli2)
        if tamanho_poli1 != tamanho_poli2:
            # padding dos polinomios
            p1_padding = (0,) * (maior_grau - tamanho_poli1) 
            p2_padding = (0,) * (maior_grau - tamanho_poli2)
            p1 = p1_padding + p1
            p2 = p2_padding + p2

        # agora que tem ambos o mesmo tamanho 
        for grau in range(maior_grau):
            resultado = resultado + (p1[grau] + p2[grau],)
            
        self.polinomios.append(resultado)
        print("Polinómios somados com sucesso!")

    def gerar_grafico_para_polinomio(self):
        self.listar_polinomios()
        num_ordem = int(input("Introduza o número de ordem do polinómio: ")) - 1
        polinomio = self.polinomios[num_ordem]

        # Gerar valores x e y para o gráfico
        x_valores = [i for i in range(-10, 11)]
        y_valores = [sum(coef * (x ** grau) for grau, coef in enumerate(polinomio[::-1])) for x in x_valores]

        # Plotar o gráfico
        plt.plot(x_valores, y_valores, label=f'Polinómio {num_ordem + 1}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico do Polinómio')
        plt.legend()
        plt.grid(True)
        plt.show()

    def gravar_polinomios_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for polinomio in self.polinomios:
                arquivo.write(" ".join(map(str, polinomio)) + "\n")
        print("Polinómios gravados com sucesso!")

if __name__ == "__main__":
    manipulador = PolinomioManipulador()

    while True:
        print("\nOperações disponíveis:")
        print("1. Criar um polinómio interativamente")
        print("2. Ler uma lista de polinómios de um ficheiro")
        print("3. Listar polinómios")
        print("4. Calcular o valor de um polinómio num ponto")
        print("5. Listar polinómios com grau")
        print("6. Maior grau")
        print("7. Derivada")
        print("8. Somar dois polinómios")
        print("9. Gerar um gráfico para o polinómio")
        print("10. Gravar num ficheiro os polinómios em memória")
        print("0. Sair da aplicação")

        escolha = input("Introduza o número da operação desejada: ")

        if escolha == '1':
            manipulador.criar_polinomio_interativamente()
        elif escolha == '2':
            nome_arquivo = input("Introduza o nome do ficheiro: ")
            manipulador.ler_polinomios_de_arquivo(nome_arquivo)
        elif escolha == '3':
            manipulador.listar_polinomios()
        elif escolha == '4':
            manipulador.calcular_valor_em_ponto()
        elif escolha == '5':
            manipulador.listar_polinomios_com_grau()
        elif escolha == '6':
            manipulador.mostrar_maior_grau()
        elif escolha == '7':
            manipulador.mostrar_derivadas()
        elif escolha == '8':
            manipulador.adiciona_poli()
        elif escolha == '9':
            manipulador.gerar_grafico_para_polinomio()
        elif escolha == '10':
            nome_arquivo = input("Introduza o nome do ficheiro: ")
            manipulador.gravar_polinomios_em_arquivo(nome_arquivo)
        elif escolha == '0':
            break
        else:
            print("Escolha inválida. Por favor, introduza um número válido.")
