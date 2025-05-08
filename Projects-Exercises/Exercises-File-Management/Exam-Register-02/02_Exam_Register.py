
archive_inventory = 'inventory.txt'
class Inventory:
# Se crea la clase Inventory para tener conglomerado los metodos y por ende poder heredar todos estos metodos a algun objeto, en este caso book_inventory


    def load_inventory(self):
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            books = file.readlines()
            for book in books:
                content_book = book.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                print(
                    f'\nID: {content_book[0]} Titulo: {content_book[1]} Autor: {content_book[2]} Año: {content_book[3]} Categoria: {content_book[4]} '
                    f'Editorial: {content_book[5]} Precio: {content_book[6]} Cantidad: {content_book[7]}')
                # Se imprime el contenido que se desea ver del libro segun el orden con el cual se ha hecho la insercion en el archivo .txt

    def add_book(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        title = str(input('Ingrese el titulo: ').title())
        author = str(input('Ingrese el autor: ').title())
        year = int(input('Ingrese el año de publicacion: '))
        category = str(input('Ingrese la categoria: ').title())
        editorial = str(input('Ingrese la editorial: ').title())
        price = float(input('Ingrese el precio: '))
        amount = int(input('Ingrese las unidades disponibles: '))
        with open(archive_inventory, mode='a', encoding='utf-8') as file:
            file.write(f"{id(self)},{title},{author},{year},{category},{editorial},{price},{amount}\n")
            # Se agrega el contenido del libro con un orden especifico y se separan por comas para su posterior lectura/busqueda


    def search_by_title(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        title = str(input('Ingrese el titulo del libro: ').title())
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if title in line:
                    content_book = line.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                    print(
                        f'\nID: {content_book[0]} Titulo: {content_book[1]} Autor: {content_book[2]} Año: {content_book[3]} Categoria: {content_book[4]} '
                        f'Editorial: {content_book[5]} Precio: {content_book[6]} Cantidad: {content_book[7]}')
                    # Se imprime el contenido que se desea ver del libro segun el orden con el cual se ha hecho la insercion en el archivo .txt


    def search_by_category(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        category = str(input('Ingrese el titulo del libro que desea buscar: ').title())
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if category in line:
                    content_book = line.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                    print(
                        f'\nID: {content_book[0]} Titulo: {content_book[1]} Autor: {content_book[2]} Año: {content_book[3]} Categoria: {content_book[4]} '
                        f'Editorial: {content_book[5]} Precio: {content_book[6]} Cantidad: {content_book[7]}')
                    # Se imprime el contenido que se desea ver del libro segun el orden con el cual se ha hecho la insercion en el archivo .txt

                else:
                    print('No se encontro el libro')


    def books_by_author(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        author = str(input('Ingrese el autor del libro que desea buscar: ').title())
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if author in line:
                    content_book = line.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                    print(
                        f'\nID: {content_book[0]} Titulo: {content_book[1]} Autor: {content_book[2]} Año: {content_book[3]} Categoria: {content_book[4]} '
                        f'Editorial: {content_book[5]} Precio: {content_book[6]} Cantidad: {content_book[7]}')
                    # Se imprime el contenido que se desea ver del libro segun el orden con el cual se ha hecho la insercion en el archivo .txt


    def search_price_book(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        book = str(input('Ingrese el nombre del libro: ').title())
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if book in line:
                    content_book = line.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                    print(f'\nPrecio: ${content_book[6]}')
                    # Se imprime el contenido que se desea ver del libro, en este caso el precio


    def search_amount_book(self):
        # title() se usa para que la primera letra de cada palabra sea mayuscula
        book = str(input('Ingrese nombre del libro: ').title())
        with open(archive_inventory, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if book in line:
                    content_book = line.split(',') # Separa el contenido del libro por comas, dando como resultado una cadena de texto con sus con sus campos
                    print(f'\nUnidades disponibles: {content_book[7]}')
    # Se imprime el contenido que se desea ver del libro, en este caso el las unidades disponibles


# Se crea el objeto book_inventory para poder usar los metodos de la clase Inventory
book_inventory = Inventory()

continuar = True

while continuar:
    print(
        'Tiene las siguientes opciones: \n1. Agregar libro\n2. Leer libros\n3. Buscar por titulo\n4. Buscar por autor'
        '\n5. Buscar por categoria\n6. Buscar precio de algun libro\n7. Buscar unidades disponibles de un libro\n8. Salir\n ')
    option = int(input('Ingrese su opcion aqui: '))
    match option:
        case 1:
            book_inventory.add_book()
        case 2:
            book_inventory.load_inventory()
        case 3:
            book_inventory.search_by_title()
        case 4:
            book_inventory.books_by_author()
        case 5:
            book_inventory.search_by_category()
        case 6:
            book_inventory.search_price_book()
        case 7:
            book_inventory.search_amount_book()
        case 8:
            continuar = False
        case _:
            print('Opcion no valida')
