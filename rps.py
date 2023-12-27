import random as random

liste=["Taş","Kağit","Makas"]
liste2=["Rock","Paper","Scissors"]
x=(random.choice(liste2))
y=(random.choice(liste))
dil=input("Language = ")

if dil=="en":
    choice=input("Please make your choice (Rock,Paper,Scissors) = ").upper()
    print(choice.title())
    print(x)

    if choice=="ROCK":
        if x=="Paper":
            print("You lost")
        elif x=="Scissors":
            print("You won")
        elif x=="Rock":
            print("You tied")

    elif choice=="PAPER":
        if x=="Scissors":
            print("You lost")
        elif x=="Rock":
            print("You won")
        elif x=="Paper":
            print("You tied")

    elif choice=="SCISSORS":
        if x=="Rock":
            print("You lost")
        elif x=="Paper":
            print("You win")
        elif x=="Scissors":
            print("You tied")         
elif dil=="tr":
    choice=input("Lütfen seçiminizi yapınız (Taş,Kağıt,Makas) = ").upper()
    print(choice.title())
    print(y)

    if choice=="TAŞ":
        if y=="Makas":
            print("Kazandın")
        elif y=="Kağit":
            print("Kaybettin")
        elif y=="Taş":
            print("Berabere kaldın")
        else:
            print("Geçersiz komut")

    elif choice=="KAĞIT":
        if y=="Taş":
            print("Kazandın")
        elif y=="Makas":
            print("Kaybettin")
        elif y=="Kağit":
            print("Berabere kaldın")
        else:
            print("Geçersiz komut")
            
    elif choice=="MAKAS":
        if y=="Taş":
            print("Kaybettin")
        elif y=="Kağit":
            print("Kazandın")
        elif y=="Makas":
            print("Berabere kaldın")
        else:
            print("Geçersiz komut")
else: 
    print("Geçersiz komut")
