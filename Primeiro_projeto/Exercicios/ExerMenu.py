import importlib.util


def executar_funcao(arquivo, nome_funcao):
    try:
        # Importar o módulo dinamicamente
        spec = importlib.util.spec_from_file_location("modulo_temporario", arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        # Obter a função do módulo
        funcao = getattr(modulo, nome_funcao)

        # Executar a função
        resultado = funcao()
        print(resultado)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
    except ImportError as e:
        print(f"Erro ao importar o módulo: {e}")
    except AttributeError:
        print(f"Erro: A função '{nome_funcao}' não encontrada no módulo.")
    except Exception as e:
        print(f"Erro durante a execução: {e}")


def main():
    # Solicitar ao usuário o caminho do arquivo Python
    nome_arquivo = input("Digite o caminho do arquivo Python (.py): ")
    nome_arquivo = "exer"+nome_arquivo+".py"
    # Solicitar ao usuário o nome da função a ser executada
    nome_funcao = input("Digite o nome da função a ser executada: ")
    nome_funcao = "f"+nome_funcao
    # Executar a função com o arquivo e o nome da função fornecidos
    executar_funcao(nome_arquivo, nome_funcao)


if __name__ == "__main__":
    main()
