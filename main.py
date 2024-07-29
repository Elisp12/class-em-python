from palura.test import Restaurante


restaurante1 = Restaurante('praça', 'Goumert')

restaurante1.recebe_avaliacao('elispo', 5)
restaurante1.recebe_avaliacao('elis', 5)
restaurante1.recebe_avaliacao('elispo', 2)
restaurante1.recebe_avaliacao('elispo', 3)

restaurante1.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()