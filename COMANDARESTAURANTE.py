import os
import time


class Produto:
    def __init__(self, valor, nome):
        self.valor = valor
        self.nome = nome
        self.quantidade = 0
        self.proximo = None


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_item(item_list):
    while True:
        clear_screen()
        print("===========")
        print("COMANDA | {}º Item".format(len(item_list) + 1))
        print("===========")
        print()
        print("CARDAPIO")
        print("========")
        print("1 - PRATOS")
        print("2 - BEBIDAS")
        print("3 - ACOMPANHAMENTOS")
        print("4 - SOBREMESAS")
        print("0 - Encerrar")
        print("--------------")
        category = int(input("Categoria: "))

        if category == 0:
            break

        if category < 1 or category > 4:
            clear_screen()
            print("\n===================================")
            print("CATEGORIA INVÁLIDA, TENTE NOVAMENTE!")
            print("===================================\n")
            input("Pressione Enter para continuar...")
            continue

        if category == 1:
            items = {
                1: ("Moqueca", 38.0),
                2: ("Feijoada", 39.90),
                3: ("Baião de Dois", 95.0),
                4: ("Arroz com Pequi", 25.90),
                5: ("Virado à Paulista", 38.50),
                6: ("Bobó de Camarão", 42.90),
                7: ("Lasanha à Bolonhesa", 34.90),
                8: ("Risoto de Funghi", 29.90),
                # Adicione mais pratos aqui
            }
        elif category == 2:
            items = {
                1: ("Coca Cola", 9.90),
                2: ("Fanta (Laranja ou Uva)", 7.90),
                3: ("Guarana", 6.90),
                4: ("Pepsi", 7.90),
                5: ("Itubaina", 5.90),
                6: ("Suco de Laranja", 8.50),
                7: ("Água Mineral", 3.50),
                8: ("Chá Gelado", 4.90),
                # Adicione mais bebidas aqui
            }
        elif category == 3:
            items = {
                1: ("Feijão", 9.90),
                2: ("Farofa", 3.90),
                3: ("Batata Frita", 10.90),
                4: ("Purê", 7.90),
                5: ("Salada", 6.90),
                6: ("Vinagrete", 4.50),
                7: ("Mandioca Frita", 8.90),
                8: ("Couve Refogada", 6.50),
                # Adicione mais acompanhamentos aqui
            }
        elif category == 4:
            items = {
                1: ("Pudim de Leite", 12.90),
                2: ("Mousse de Chocolate", 9.90),
                3: ("Torta de Limão", 14.90),
                4: ("Sorvete de Creme", 8.90),
                5: ("Brigadeiro", 3.50),
                6: ("Cheesecake de Morango", 16.90),
                7: ("Quindim", 7.90),
                8: ("Tiramisu", 18.90),
                # Adicione mais sobremesas aqui
            }
        else:
            clear_screen()
            print("\n===================================")
            print("CATEGORIA INVÁLIDA, TENTE NOVAMENTE!")
            print("===================================\n")
            input("Pressione Enter para continuar...")
            continue

        clear_screen()
        print("===========")
        print("COMANDA | {}º Item".format(len(item_list) + 1))
        print("===========")
        print()
        print("CARDAPIO")
        print("========")
        print()
        for index, item in items.items():
            print(f"{index} - {item[0]} - R$ {item[1]}")
        print()
        print("0 - Encerrar")
        print("--------------")
        num = int(input("Opção: "))

        if num == 0:
            break

        if num < 1 or num > len(items):
            clear_screen()
            print("\n===================================")
            print("VALOR INCORRETO, TENTE NOVAMENTE!")
            print("===================================\n")
            input("Pressione Enter para continuar...")
            continue

        name, preco = items[num]
        qntd = int(input("\nQuantidade: "))

        item = Produto(preco, name)
        item.quantidade = qntd
        item_list.append(item)


def show_order(item_list):
    total = 0

    clear_screen()
    print("\t\t\t============")
    print("\t\t\tDESCRITIVO")
    print("\t\t\t============\n")

    print("----------------------------------------------------------------")
    print("Nome\t\t|   Quantidade\t|  Valor Unit\t| Sub-Total")
    print("----------------------------------------------------------------")
    for item in item_list:
        sub_total = item.quantidade * item.valor
        print("{:<12}|{:>8d}\t\t| R$ {:>8.2f}\t| R$ {:>8.2f}".format(item.nome, item.quantidade, item.valor, sub_total))
        total += sub_total
    print("----------------------------------------------------------------")
    print("\nTotal de compras: R$ {:.2f}".format(total))

    now = time.localtime()
    date = "{}/{}/{}".format(now.tm_mday, now.tm_mon, now.tm_year)
    print("Data: {}".format(date))


def make_payment(item_list):
    show_order(item_list)
    print("\n1 - Efetuar pagamento")
    print("2 - Adicionar mais itens")

    option = int(input("\nOpção: "))
    if option == 1:
        payment_method = input("\nInforme o método de pagamento (dinheiro, cartão): ")
        if payment_method.lower() == "dinheiro":
            payment_amount = float(input("\nInforme o valor pago: "))
            total = sum(item.quantidade * item.valor for item in item_list)
            change = payment_amount - total
            print("\nTroco: R$ {:.2f}".format(change))
        elif payment_method.lower() == "cartão":
            print("\nSimulando pagamento com cartão...")
        else:
            print("\nMétodo de pagamento inválido.")
            return
        print("\nPagamento realizado com sucesso!")
        input("\nPressione Enter para reiniciar...")
        item_list.clear()
    elif option == 2:
        add_item(item_list)
    else:
        print("\nOpção inválida.")


def main():
    item_list = []
    while True:
        add_item(item_list)
        make_payment(item_list)


if __name__ == '__main__':
    main()
