
from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} - {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(25)} | {"Média Avaliações".ljust(25)}')
        print('-' * 75)
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} - {restaurante.categoria.ljust(25)} -{restaurante.ativo.ljust(25)} - {str(restaurante.media_avaliacoes).ljust(25)}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota < 0 or nota > 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print('A avaliação deve ser entre 0 e 5.')
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        total = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = total / len(self._avaliacoes)
        return round(media, 1)

    