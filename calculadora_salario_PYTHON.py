ValorHora = float(input ("Digite o valor da sua hora:"))

HorasTrabalhadas = float(input ("Digite a quantidade de horas trabalhadas:"))

salarioBruto = (ValorHora * HorasTrabalhadas)

if (salarioBruto <= 900):
    ir = 0

elif (salarioBruto <= 1500): 
    ir = salarioBruto * 0.05

elif (salarioBruto <= 2500):
    ir = salarioBruto * 0.10

elif ( salarioBruto >= 2500 ):

    ir = salarioBruto * 0.10

else:
    ir = salarioBruto * 0.20

#calculos
inss = salarioBruto * 0.10
fgts = salarioBruto * 0.11

#calculo descontos
TotalDescontos = ir + inss
salarioLiquido = salarioBruto - TotalDescontos

print("Salario bruto: R$ %.2f\n" % salarioBruto)
print("Valor descontado de IR R$ %.2f \n" % ir)
print("Valor descontado de INSS R$ %.2f\n" % inss)
print("Valor do FGTS: R$ %.2f\n" % fgts)
print("Total de descontos: R$ %.2f\n " % TotalDescontos)
print("Salario liquido: R$ %.2f\n " % salarioLiquido)