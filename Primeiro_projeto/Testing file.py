def calcular_tempo_populacao_ultrapassar(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0
    while populacao_a <= populacao_b:
        populacao_a *= (1 + taxa_a / 100)
        populacao_b *= (1 + taxa_b / 100)
        anos += 1
    return anos


def main():
    while True:
        try:
            populacao_a = float(input("Informe a população do país A: "))
            taxa_a = float(input("Informe a taxa de crescimento da população do país A (%): "))
            populacao_b = float(input("Informe a população do país B: "))
            taxa_b = float(input("Informe a taxa de crescimento da população do país B (%): "))

            if populacao_a <= 0 or taxa_a < 0 or populacao_b <= 0 or taxa_b < 0:
                raise ValueError("Por favor, insira valores válidos.")

            anos_necessarios = calcular_tempo_populacao_ultrapassar(populacao_a, taxa_a, populacao_b, taxa_b)

            print(
                f"\nSerão necessários {anos_necessarios} anos para que a população de um país ultrapasse a população do outro.\n")

        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de inserir valores válidos.\n")

        continuar = input("Deseja fazer outra simulação? (s/n): ").lower()
        if continuar != 's':
            break


if __name__ == "__main__":
    main()
