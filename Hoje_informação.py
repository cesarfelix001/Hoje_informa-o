import datetime

data = datetime.datetime.now()

hoje = input("Digite 'hoje' para saber informações sobre: ")

if hoje == "hoje" or hoje == "Hoje":
    print("Informações sobre hoje ༼ つ ◕_◕ ༽つ")
    print(f"Semana: {data.strftime("%A")}")
    print(f"Mês: {data.strftime("%B")}")
    print(f"Ano: {data.year}")


