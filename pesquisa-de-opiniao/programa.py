excelente = 0
bom= 0
ruim = 0
for i in range (0,50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = input("Qual a sua opinião sobre o sistema entrevistado? EXCELENTE, BOM OU RUIM? ")
    if opiniao == "EXCELENTE":
        excelente += 1
    else:
        if opiniao == "BOM":
            bom += 1
        else:
            if opiniao == "RUIM":
                ruim += 1
print("A quantidade de pessoas que responderam excelente foi: ", excelente)
print("A quantidade de pessoas que responderar ruim foi: ", ruim)



    

    

            
