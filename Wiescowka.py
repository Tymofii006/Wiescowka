                              #1
def main():
    a = int(input("Podaj pierwszą liczbę całkowitą a: "))
    b = int(input("Podaj drugą liczbę całkowitą b: "))

    suma_liczb = 0

    for i in range(a, b + 1):
        suma_liczb += i

    print("Suma wszystkich liczb w przedziale [a, b]:", suma_liczb)

if __name__ == "__main__":
    main()


                                       #2
while True:
    liczba = float(input("Podaj liczbę całkowitą: "))

    if liczba < 0:
        print("Podano licbę ujemną. Koniec. ")
        break
    else:
        print(f"Podano liczbę dodatnią: {liczba}")

