inscricao = input()
nome, escolha = inscricao.split()

vencedor = {"nome": nome, "nome_tam": len(nome)}
inscritos_yes = set()
inscritos_no = set()

while inscricao != 'FIM':
    nome, escolha = inscricao.split()
    if escolha == 'YES':
        inscritos_yes.add(nome)
        if len(nome) > vencedor["nome_tam"]:
            vencedor["nome"] = nome
            vencedor["nome_tam"] = len(nome)
    else:
        inscritos_no.add(nome)
    inscricao = input()

inscritos_yes = sorted(inscritos_yes)
inscritos_no = sorted(inscritos_no)

print("\n".join(inscritos_yes))
print("\n".join(inscritos_no))
print(f"\nAmigo do Habay:\n{vencedor['nome']}")
