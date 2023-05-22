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
                9: ("macarronada", 24.99),
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
                9: ("Cerveja", 14.90),
                # Adicione mais bebidas aqui
            }
        elif category == 3:
            items = {
                1: ("Feijão", 9.90),
                2: ("Farofa", 3.90),
                3: ("Batata Frita", 10.90),
                4: ("Pure", 7.90),
                5: ("Salada", 6.90),
                6: ("Vinagrete", 4.50),
                7: ("Mandioca Frita", 8.90),
                8: ("Couve Refogada", 6.50),
                9: ("Torresmo", 9.90),

                # Adicione mais acompanhamentos aqui
            }

        elif category == 4:
            items = {
                1: ("Pudim", 8.50),
                2: ("Sorvete", 6.90),
                3: ("Torta de Limão", 12.0),
                4: ("Brigadeiro", 4.50),
                5: ("Mousse de Chocolate", 9.90),
                6: ("Cheesecake de Morango", 16.90),
                7: ("Quindim", 7.90),
                8: ("Tiramisu", 18.90),
                9: ("Açai", 15.90),
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


def remove_item(item_list):
    clear_screen()
    print("============")
    print("REMOVER ITEM")
    print("============\n")

    if not item_list:
        print("A comanda está vazia. Não há itens para remover.")
        input("\nPressione Enter para continuar...")
        return

    print("COMANDA")
    print("-------")
    for i, item in enumerate(item_list):
        print(f"{i+1} - {item.nome} - R$ {item.valor} - Quantidade: {item.quantidade}")

    print()
    item_index = int(input("Digite o número do item que deseja remover: "))

    if item_index < 1 or item_index > len(item_list):
        print("Índice inválido. Tente novamente.")
        input("\nPressione Enter para continuar...")
    else:
        item_list.pop(item_index - 1)
        print("Item removido com sucesso.")
        input("\nPressione Enter para continuar...")


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
    print("3 - Remover item da comanda")

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
    elif option == 3:
        remove_item(item_list)
    else:
        print("\nOpção inválida.")


def main():
    item_list = []
    while True:
        add_item(item_list)
        make_payment(item_list)


if __name__ == '__main__':
    main()
