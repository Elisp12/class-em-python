from palura.test import Restaurante
from palura.item_cardapio.prato import Prato
from palura.item_cardapio.bebida import Bebida
from palura.item_cardapio.sobremesa import Sobremesa

restaurante1 = Restaurante('praça', 'Goumert')
restaurante2 = Restaurante('centro', 'Goumert')

restaurante1.recebe_avaliacao('elispo', 5)
restaurante1.recebe_avaliacao('elis', 5) 
restaurante1.recebe_avaliacao('elispo', 2)
restaurante1.recebe_avaliacao('elispo', 3)

restaurante1.alternar_estado()

bebida_laranja = Bebida('Suco de laranja', 2.90, 'grande')
bebida_laranja.aplicar_desconto()

prato_frango = Prato('Frango assado', 15.50, 'frango assado na brasa, com pitadas de limão')
prato_frango.aplicar_desconto()

sobremesa_picole = Sobremesa('Picolé', 1.5, 'picolé sabor frango')
sobremesa_picole.aplicar_desconto()

restaurante1.adicionar_no_cardapio(prato_frango)
restaurante1.adicionar_no_cardapio(bebida_laranja)
restaurante1.adicionar_no_cardapio(sobremesa_picole)

def main():
   restaurante1.exibir_cardapio
if __name__ == '__main__':
    main()