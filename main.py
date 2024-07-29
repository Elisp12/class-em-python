from palura.test import Restaurante


restaurante1 = Restaurante('praça', 'Goumert')

restaurante1.recebe_avaliacao('elispo', 6)
restaurante1.recebe_avaliacao('elis', 1)
restaurante1.recebe_avaliacao('elispo', 8)
restaurante1.recebe_avaliacao('elispo', 7)

restaurante1.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()