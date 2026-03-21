nome = input("Qual é o nome do aparelho? ")
potencia = float(input("Qual a potência do aparelho (W)? "))
tempo_medio = float(input("Qual o tempo médio de uso diário em horas? "))
consumoMensal = (potencia * tempo_medio * 30) / 1000
print("Aparelho:", nome)
print("Consume estimado: ",consumoMensal,"kWh/mês")
