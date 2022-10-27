# Desafio salario
salario = int(input("coloque o valor: ")) 

if salario <= 600:
    Novo_salario = f"{(salario*(17/100)) + salario:.2f}"
    Reajuste_ganho = f"{(salario*(17/100)):.2f}"
    Em_percentual = "17 %"
    print("Novo salario:",str(Novo_salario).replace(".",","),"Reajuste ganho:",str(Reajuste_ganho).replace(".",","),"Em percentual:",Em_percentual)
elif salario > 600 and salario <= 900:
    Novo_salario = f"{(salario*(13/100)) + salario:.2f}"
    Reajuste_ganho = f"{(salario*(13/100)):.2f}"
    Em_percentual = "13 %"
    print("Novo salario:",str(Novo_salario).replace(".",","),"Reajuste ganho:",str(Reajuste_ganho).replace(".",","),"Em percentual:",Em_percentual)
elif salario > 900 and salario <= 1500:
    Novo_salario = f"{(salario*(12/100)) + salario:.2f}"
    Reajuste_ganho = f"{(salario*(12/100)):.2f}"
    Em_percentual = "12 %"
    print("Novo salario:",str(Novo_salario).replace(".",","),"Reajuste ganho:",str(Reajuste_ganho).replace(".",","),"Em percentual:",Em_percentual)
elif salario > 1500 and salario <= 2000:
    Novo_salario = f"{(salario*(10/100)) + salario:.2f}"
    Reajuste_ganho = f"{(salario*(10/100)):.2f}"
    Em_percentual = "10 %"
    print("Novo salario:",Novo_salario,"Reajuste ganho:",Reajuste_ganho,"Em percentual:",Em_percentual)
else:
    Novo_salario = f"{(salario*(5/100)) + salario:.2f}"
    Reajuste_ganho = f"{(salario*(5/100)):.2f}"
    Em_percentual = "5 %"
    print("Novo salario:",str(Novo_salario).replace(".",","),"Reajuste ganho:",str(Reajuste_ganho).replace(".",","),"Em percentual:",Em_percentual)


