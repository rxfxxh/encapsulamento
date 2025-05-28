class Livro:
    def __init__ (self, titulo):
        self.__titulo = titulo

    def set_titulo(self, t):
        if t:
            self.__titulo = t
        else:
            return print("Erro, título não pode ser vazio.")
        
    def mostrar_titulo(self):
        return self.__titulo
    


livro1 = Livro("Rafael do Capa")
print(f"titulo antigo: {livro1.mostrar_titulo()}")
livro1.set_titulo("titulo atualizado")
print(f"titulo novo: {livro1.mostrar_titulo()}")