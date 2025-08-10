def base_func(lista):

    try:
        nome = input("Nome do funcionario é: ")
        idade = int(input("A idade do funcionario é: " ))
        cargo = input("Cargo do funcionario é: ")
        codigo = int(input("Codigo do funcionario é: "))
        salario = float(input("Salario do funicionario é: "))


        funcionario = {
            "nome": nome,
            "idade": idade,
            "cargo": cargo,
            "codigo": codigo,
            "salario": salario
            }
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos para idade, codigo e salario.")
        
    else: lista.append (funcionario)
    print("Funcionario executado com sucesso. ")


