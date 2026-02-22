## 💰 Calculadora de Salário Líquido – C & Python

📌 Sobre o Projeto

Este projeto consiste na implementação de uma calculadora de salário líquido, desenvolvida inicialmente em C como parte de um projeto acadêmico (2025) e posteriormente reimplementada em Python como exercício de aperfeiçoamento e transposição de lógica entre linguagens.

O objetivo principal foi reaproveitar a mesma lógica de programação e regras de negócio, comparando diferenças de sintaxe, estrutura e sistema de tipos entre as linguagens.

🧠 Objetivos Técnicos

Aplicar lógica condicional baseada em faixas salariais

Trabalhar com operações matemáticas e cálculos percentuais

Comparar declaração explícita de tipos (C) com tipagem dinâmica (Python)

Exercitar transposição de algoritmo entre linguagens

Analisar legibilidade e redução de boilerplate

📊 Regras de Negócio

O programa realiza:

Cálculo do Salário Bruto

salario_bruto = valor_hora × horas_trabalhadas

Aplicação de Imposto de Renda (IR) conforme faixa:

Faixa Salarial	Percentual IR
Até R$ 900,00	0%
R$ 900,01 – 1500,00	5%
R$ 1500,01 – 2500,00	10%
Acima de R$ 2500,00	20%

Cálculo adicional:

INSS = 10%

FGTS = 11% (não descontado do salário líquido)

Cálculo final:

salario_liquido = salario_bruto - (ir + inss)
🛠 Tecnologias Utilizadas

Linguagem C

Python 3

🔍 Comparação Técnica
<img width="1060" height="349" alt="image" src="https://github.com/user-attachments/assets/2ab6a171-e4cf-4652-9f24-257be845eed2" />


🚀 Próximos Passos

Refatoração utilizando funções

Separação da lógica em módulos

Implementação de testes

Evolução para versão com interface gráfica ou web

📈 Aprendizado

Este projeto reforça que a lógica de programação é independente da linguagem.
A sintaxe muda, mas a modelagem do problema permanece.
