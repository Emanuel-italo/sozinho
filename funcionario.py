def base_func(lista):
    try:
        nome = input("Nome do funcionário: ")
        idade = int(input("A idade do funcionário é: "))
        cargo = input("Cargo do funcionário: ")
        codigo = int(input("Código do funcionário: "))
        salario = float(input("Salário do funcionário é: "))

        funcionario = {
            "nome": nome,
            "idade": idade,
            "cargo": cargo,
            "codigo": codigo,
            "salario": salario
        }
    except ValueError:
        print("Erro: digite valores numéricos válidos para idade, código e salário.")
    else:
        lista.append(funcionario)
        print("Funcionário executado com sucesso.")
    finally:
        print("Inserção finalizada.\n")

def consultar_func(lista):
    codigo = input("Digite o codigo do funcionario: ")
    for funcionario in lista:
        if funcionario["codigo"] == codigo:
            print(f"codigo encontrado: {funcionario}")
            return
        else:
            print("codigo não encontrado. ")

def alterar_func(lista):
    try:
        codigo = input("Digite aqui a alteração que deseja fazer: ")
        for funcionario in lista:
            if funcionario ["codigo"] == codigo:
                print("Funcionario encontrado. Digite os novos dados que deseja:")
                funcionario["nome"] = input("Novo nome:  ")
                funcionario["codigo"] = input("Novo codigo: ")
                funcionario["idade"] = input ("Nova idade:")
                funcionario["cargo"] = input("Novo cargo: ")
                funcionario["salario"] = input("Novo salario: ")
                print("Dados alterados com sucesso. ")
                return
        print("Funcionario não encontrado. ")
    except ValueError:
        print("Erro: digite valores numéricos válidos para idade, código e salário.")
    finally:
        print("Operação de alteração finalizada.\n")



