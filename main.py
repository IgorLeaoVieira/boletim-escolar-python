# SISTEMA DE GESTÃO ESCOLAR


# Entrada

nome = input("Digite seu nome: ")

disciplina = input("Disciplina: ")

# Notas dos bimestres

nota1 = float(input("1º bimestre: "))
nota2 = float(input("2º bimestre: "))
nota3 = float(input("3º bimestre: "))
nota4 = float(input("4º bimestre: "))

# Cálculo da média

media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída

print("Aluno:", nome)

print("Média:", media)

# Situação do aluno

if media >= 5:

    print("Situação: Aprovado")

else:

    print("Situação: Reprovado")



# Frequência

frequencia = float(input("Frequência (%): "))

# Cálculo

nota_final = nota1 + nota2 + nota3 + nota4

media_final = nota_final / 4

print("Nota final:", nota_final)

print("Média final:", media_final)

# Regras de aprovação

if frequencia < 75:

    print("Aluno reprovado por falta.")

elif media_final < 5:

    print("Aluno reprovado por nota.")

else:

    print("Aluno aprovado!")



# Cadastro de alunos

alunos = []

while True:

    nome = input("Nome do aluno: ")

    if nome == "fim":

        break

    alunos.append(nome)

print("Alunos cadastrados:")

for aluno in alunos:

    print(aluno)


# Cadastro de disciplinas

for i in range(8):

    materia = input("Disciplina: ")

    print(materia)



# Função para cadastrar dados do aluno

def cadastrar_dados():

    nome = input("Digite o nome do aluno: ")

    disciplina = input("Disciplina: ")

    nota1 = float(input("1º bimestre: "))
    nota2 = float(input("2º bimestre: "))
    nota3 = float(input("3º bimestre: "))
    nota4 = float(input("4º bimestre: "))

    faltas = int(input("Quantidade de faltas: "))

    aulas_totais = 200

    return nome, disciplina, nota1, nota2, nota3, nota4, aulas_totais, faltas


# Função para calcular média

def calcular_nota(nota1, nota2, nota3, nota4):

    media = (nota1 + nota2 + nota3 + nota4) / 4

    return media


# Função para calcular frequência

def calcular_frequencia(aulas_totais, faltas):

    frequencia = ((aulas_totais - faltas) / aulas_totais) * 100

    return frequencia


# Função para gerar relatório

def gerar_relatorio(nome, disciplina, media, frequencia):

    print("RELATÓRIO FINAL")

    print("Aluno:", nome)

    print("Disciplina:", disciplina)

    print("Média:", media)

    print("Frequência:", frequencia)

    if media >= 5 and frequencia >= 75:

        print("Situação: APROVADO")

    else:

        print("Situação: REPROVADO")
