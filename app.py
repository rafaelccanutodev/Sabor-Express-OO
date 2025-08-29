from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')
bebida_suco = Bebida('Suco de melancia',5.0,'Grande')
prato_pao = Prato('Pão',2,'O melhor pão da cidade')


def main():
    
    print(bebida_suco)
    print(prato_pao)


if __name__=="__main__":
    main()