class Livro: # Define uma **classe** chamada 'Livro'.
    def __init__ (self, titulo): # O **construtor** da classe, chamado ao criar um novo livro.
        self.__titulo = titulo # Armazena o título como um atributo **privado**.

    def set_titulo(self, t): # Método para **alterar** o título do livro.
        if t: # Verifica se o novo título não está vazio.
            self.__titulo = t # Atualiza o título.
        else:
            return print("Erro, título não pode ser vazio.") # Mensagem de erro se o título for vazio.

    def mostrar_titulo(self): # Método para **obter** (ler) o título do livro.
        return self.__titulo # Retorna o título armazenado.


livro1 = Livro("Rafael do Capa") # Cria um **objeto** 'livro1' com o título inicial.
print(f"titulo antigo: {livro1.mostrar_titulo()}") # Exibe o título **antes** da mudança.
livro1.set_titulo("titulo atualizado") # **Chama** o método para mudar o título.
print(f"titulo novo: {livro1.mostrar_titulo()}") # Exibe o título **depois** da mudança.

livro2 = Livro("vitor do papiro") # Cria um **objeto** 'livro2' com o título inicial.
print(f"titulo antigo: {livro2.mostrar_titulo()}") # Exibe o título **antes** da mudança.
livro2.set_titulo("titulo vitor atualizado") # **Chama** o método para mudar o título.
print(f"titulo novo: {livro2.mostrar_titulo()}") # Exibe o título **depois** da mudança.
