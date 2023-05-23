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


def add_item(item_list, bebidas=None):
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
            pratosprotos = int(input("Pratos:\n1 - Frutos do mar\n2 - Massas\n3 - Carne\n4 - Peixes\nEscolha: "))

            if pratosprotos == 1:
                items = {
                    1: ("Espaguete ao frutos do mar", 38.0),
                    2: ("Camarão na champagne com arroz de maçã", 39.90),
                    3: ("Paella", 95.0),
                    4: ("Stroganov de frutos do mar", 25.90),
                    5: ("Lula grelhada com arroz negro", 38.50),
                    6: ("Lagosta ao thermidor", 42.90)
                }
            elif pratosprotos == 2:
                items = {
                    1: ("Capeletti de búfala e alcachofra", 38.0),
                    2: ("Agnolotti de búfala e manjericão", 39.90),
                    3: ("Nhoque de mandioquinha", 95.0),
                    4: ("Macarronada", 25.90)
                }
            elif pratosprotos == 3:
                items = {
                    1: ("Filé mignon ao molho de ervas", 38.0),
                    2: ("Picanha grelhada com batata recheada", 39.90),
                    3: ("Paleta de cordeiro", 95.0),
                    4: ("Picadinho à Marettimo", 25.90)
                }
            elif pratosprotos == 4:
                items = {
                    1: ("Filé de peixe fresco a belle Meuniere", 38.0),
                    2: ("Badejo grelhado ao molho de alcaparras", 39.90),
                    3: ("Badejo à brasileira", 95.0)
                }
            else:
                clear_screen()
                print("\n===================================")
                print("CATEGORIA INVÁLIDA, TENTE NOVAMENTE!")
                clear_screen()
                input("Pressione Enter para continuar...")
                continue

            clear_screen()
            print("PRATOS")
            print("======")
            for key, value in items.items():
                print("{}. {} - R$ {:.2f}".format(key, value[0], value[1]))
            print("0 - Voltar")
            print("--------------")
            prato = int(input("Escolha o prato: "))

            if prato == 0:
                continue

            if prato < 1 or prato > len(items):
                clear_screen()
                print("\n===================================")
                print("PRATO INVÁLIDO, TENTE NOVAMENTE!")
                print("===================================\n")
                input("Pressione Enter para continuar...")
                continue

            item = items[prato]
            item_list.append(Produto(item[1], item[0]))

            if category == 2:
                bebidas = int(input("Refrigerantes:\n1 - Sucos Naturais\n2 - Agua\n3 - Cervejas\n4 -\nEscolha: "))

                if bebidas == 1:
                    items = {
                        1: ("Coca Cola (2L)", 38.0),
                        2: ("Fanta Laranja (2L)", 39.90),
                        3: ("Fanta uva (2L)", 95.0),
                        4: ("Guarana Antartica (2L)", 25.90),
                        5: ("pepsi (2L)", 38.50),
                        6: ("Itubaina (2L)", 42.90)
                    }
                elif bebidas == 2:
                    items = {
                        1: ("Laranja (1L)", 8.0),
                        2: ("Abacaxi c/ Hortelã (1L)", 9.90),
                        3: ("Cupuacu (1L)", 5.0),
                        4: ("Lemonede (1L)", 5.90)
                    }
                elif bebidas == 3:
                    items = {
                        1: ("Agua Mineral (700ml)", 8.0),
                        2: ("Agua c/ Gas (700ml)", 9.90),
                        3: ("Agua Tonica (400ml)", 5.0),
                    }
                elif bebidas == 4:
                    items = {
                        1: ("Heineken", 38.0),
                        2: ("Corona", 39.90),
                        3: ("Cerveja Artesanal", 95.0)
                    }
                else:
                    clear_screen()
                    print("\n===================================")
                    print("CATEGORIA INVÁLIDA, TENTE NOVAMENTE!")
                    clear_screen()
                    input("Pressione Enter para continuar...")
                    continue

                clear_screen()
                print("BEBIDAS")
                print("======")
                for key, value in items.items():
                    print("{}. {} - R$ {:.2f}".format(key, value[0], value[1]))
                print("0 - Voltar")
                print("--------------")
                bebidas = int(input("Escolha a Bebida: "))

                if bebidas == 0:
                    continue

                if bebidas < 1 or bebidas > len(items):
                    clear_screen()
                    print("\n===================================")
                    print("BEBIDA INVÁLIDO, TENTE NOVAMENTE!")
                    print("===================================\n")
                    input("Pressione Enter para continuar...")
                    continue

                item = items[bebidas]
                item_list.append(Produto(item[1], item[0]))



        elif category == 3:
            items = {
                1: ("Batata frita", 12.0),
                2: ("Salada mista", 15.0),
                3: ("Arroz branco", 10.0),
                4: ("Legumes grelhados", 15.0)
            }

            clear_screen()
            print("ACOMPANHAMENTOS")
            print("===============")
            for key, value in items.items():
                print("{}. {} - R$ {:.2f}".format(key, value[0], value[1]))
            print("0 - Voltar")
            print("--------------")
            acompanhamento = int(input("Escolha o acompanhamento: "))

            if acompanhamento == 0:
                continue

            if acompanhamento < 1 or acompanhamento > len(items):
                clear_screen()
                print("\n===================================")
                print("ACOMPANHAMENTO INVÁLIDO, TENTE NOVAMENTE!")
                print("===================================\n")
                input("Pressione Enter para continuar...")
                continue

            item = items[acompanhamento]
            item_list.append(Produto(item[1], item[0]))

        elif category == 4:
            items = {
                1: ("Pudim de leite", 8.0),
                2: ("Mousse de chocolate", 10.0),
                3: ("Torta de limão", 12.0),
                4: ("Sorvete de creme", 6.0)
            }

            clear_screen()
            print("SOBREMESAS")
            print("==========")
            for key, value in items.items():
                print("{}. {} - R$ {:.2f}".format(key, value[0], value[1]))
            print("0 - Voltar")
            print("--------------")
            sobremesa = int(input("Escolha a sobremesa: "))

            if sobremesa == 0:
                continue

            if sobremesa < 1 or sobremesa > len(items):
                clear_screen()
                print("\n===================================")
                print("SOBREMESA INVÁLIDA, TENTE NOVAMENTE!")
                print("===================================\n")
                input("Pressione Enter para continuar...")
                continue

            item = items[sobremesa]
            item_list.append(Produto(item[1], item[0]))

        clear_screen()
        print("\n===================================")
        print("PRODUTO ADICIONADO À COMANDA")
        print("===================================\n")
        input("Pressione Enter para continuar...")
        clear_screen()


    while True:
        clear_screen()
        print("============")
        print("COMANDA")
        print("============")
        print()
        print("1 - Adicionar item")
        print("2 - Exibir comanda")
        print("0 - Encerrar")
        print("--------------")
        opcao = int(input("Opção: "))

        if opcao == 0:
            break

        if opcao < 1 or opcao > 2:
            clear_screen()
            print("\n===================================")
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
            print("===================================\n")
            input("Pressione Enter para continuar...")
            continue

        if opcao == 1:
            add_item(item_list, bebidas)

        elif opcao == 2:
            clear_screen()
            print("COMANDA")
            print("=======")
            total = 0.0

            for i, item in enumerate(item_list):
                print("{} - {} - R$ {:.2f}".format(i + 1, item.nome, item.valor))
                total += item.valor

            print("--------------")
            print("TOTAL: R$ {:.2f}".format(total))
            print("\n===================================\n")
            input("Pressione Enter para continuar...")
    now = time.localtime()
    date = "{}/{}/{}".format(now.tm_mday, now.tm_mon, now.tm_year)
    print("Data: {}".format(date))


def show_order(item_list):
    pass


def remove_item(item_list):
    pass


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

