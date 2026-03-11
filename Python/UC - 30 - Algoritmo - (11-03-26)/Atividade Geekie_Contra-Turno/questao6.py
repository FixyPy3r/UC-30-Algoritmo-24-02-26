idade = int(input("Qual sua idade? "))

if idade < 12:
    print("Infantil")
elif 12 <= idade < 18:
    print("Juvenil")
elif 18 <= idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Sênior")
else:
    print("Nenhuma opção")