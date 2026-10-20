# 📊 Boletim Escolar — Sistema de Gestão Escolar em Python

## 📌 Visão Geral

O **Boletim Escolar** é um sistema simples de gestão escolar desenvolvido em Python. O programa permite cadastrar alunos, lançar notas dos quatro bimestres, calcular a média final, registrar a frequência e informar a situação do aluno (aprovado ou reprovado). O objetivo é resolver o problema de organização manual de notas e frequência em pequenas instituições de ensino, praticando lógica de programação, funções e estruturas de repetição.

## 🎯 Contexto e Motivação

Este projeto foi desenvolvido como trabalho prático da disciplina de progamação de computadores do curso de tecnologo ads, no semestre 2026.1. A proposta era criar uma solução que aplicasse os conceitos aprendidos em sala — como funções, listas, condicionais e entrada/saída de dados — em um cenário real de gestão escolar.

## 👥 Integrantes da Equipe

- Davi Cauê Almeida da Silva — [@davicauezz](https://github.com/davicauezz)
- Gabriel Hansel Pimenta da Silva — [@gabrielhansel15-hue](https://github.com/gabrielhansel15-hue)
- Igor de Souza Leão Vieira — [@IgorLeaoVieira](https://github.com/IgorLeaoVieira)
- Pedro Gabriel França Carneiro — [@PedroGFCarneiro](https://github.com/PedroGFCarneiro)
- Roniel Ferreira Ribas — [@ferreiraroniel220-eng](https://github.com/ferreiraroniel220-eng)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** — linguagem principal
- **Terminal/CLI** — interface de uso (entrada e saída via `input()` e `print()`)

## ⚙️ Funcionalidades

- Cadastro de alunos e disciplinas
- Lançamento das notas dos 4 bimestres
- Cálculo da média final
- Registro de faltas e cálculo de frequência
- Verificação da situação do aluno (aprovado/reprovado por nota ou por falta)
- Geração de relatório final no terminal

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/IgorLeaoVieira/boletim-escolar-python.git

# 2. Entre na pasta do projeto
cd boletim-escolar-python

# 3. Execute o programa
python main.py

Digite o nome do aluno: Igor Leão Vieira
Disciplina: Matemática
1º bimestre: 7
2º bimestre: 8
3º bimestre: 6
4º bimestre: 9
Quantidade de faltas: 10

RELATÓRIO FINAL
Aluno: Igor Leão Vieira
Disciplina: Matemática
Média: 7.5
Frequência: 95.0
Situação: APROVADO

boletim-escolar-python/
├── main.py             # Código principal do sistema
├── README.md           # Este arquivo
├── LICENSE             # Licença MIT
└── .gitignore          # Arquivos ignorados pelo Git
