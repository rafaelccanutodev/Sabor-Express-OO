from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')




def main():
    Restaurante.listar_restaurantes()



if __name__=="__main__":
    main()