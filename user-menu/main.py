tam = 30

opcoes = {
    "1": "Fazer Login",
    "2": "Fazer Publicação",
    "3": "Excluir Publicação",
    "4": "Editar Publicação",
    "0": "Sair",
}

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        print(f"|{f' {k} - {v}':{tam}}|")
    print(f"+{'-' * tam}+")

    op = input()
    
    if op not in opcoes:
        print("Opção Inválida")
        continue
    
    if op == "0":
        break
    
    print(f"{opcoes.get(op)}\n")
