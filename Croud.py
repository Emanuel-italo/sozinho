def aluno_fiap (lista):
    
    try:
        
        semestre = int(input("Semestre do aluno eh: "))
        
        nome = input("Nome do aluno é: ")
        
        id = int(input("ID do aluno é: "))

        graduacao = input("Nome da graduacao é: ")


        checkpoint = []

        for i in range (3):
            nota = float(input(f"Nota do aluno é { i + 1 }: "))
            checkpoint.append(nota)

        aluno = {

            "semestre": semestre,
            "nome": nome,
            "id": id,
            "graduacao": graduacao
        }

    except ValueError:
        print("Precisa ser submetido o valor correto. ")
    else:
        lista.append(aluno)
        print("aluno inserido com sucesso!")

    finally:
        ("Inserção Finalizada.\n")


