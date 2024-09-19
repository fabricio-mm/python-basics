'''
Agregação = Representa uma relacionamento onde um objeto contém referencias
para um ou mais objetos independentes.
'''

#Vamos seguir o seguinte exemplo de uma livraria e livros, um livro pode existir fora de uma livraria, assim como um livraria existe sem livros.
#				essa é a diferença entre agregação e composição

class Library:
	def __init__ ( self, name ):
		self.name = name
		self.books = [ ]

	def add_book ( self, book ): #criando um metodo para que seja possivel adcionar livros na biblioteca
		self.books.append (book)

	def list_books( self ): #criando um metodo para printar os livros adcionados
		return [f"[{book.author}]: {book.title}"for book in self.books]


class Book:
    def __init__( self, title, author ):
       self.title = title
       self.author = author

library = Library("Biblioteca de Belo Horizonte")

#Reparem que tanto biblioteca e os livros existem sem o outro, são INDEPENDENTES

book1 = Book("Clube da Luta", "Chuck Palahniuk" )
book2 = Book("Harry potter e a Pedra Filosofal", "J.K. Rowling")
book3 = Book("Alan Turing, The enigma", "Andrew Hodges")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.list_books():
	print(book)

# Isso que fizemos chama-se agregação :)