from datetime import date
from datetime import date


class CriadorNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razao social deve ser preenchida')

        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')

        if self.__itens is None:
            raise Exception('Os itens devem ser preenchidos')

        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()

        if self.__detalhes is None:
            self.__detalhes = ''

        return NotaFiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes,
        )


from datetime import date


class Item:
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal:
    def __init__(
        self,
        razao_social,
        cnpj,
        itens,
        data_de_emissao=date.today(),
        detalhes='',
    ):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                'Detalhes da nota fiscal nao pode ter mais que 20 chars'
            )
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens


if __name__ == '__main__':



    itens = [Item('ITEM A', 100), Item('ITEM B', 200)]

    nota_fiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='01928391827321',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes='',
    )

    nota_fiscal_criada_com_builder = (
        CriadorNotaFiscal()
        .com_razao_social('FHSA Limitada')
        .com_cnpj('01928391827321')
        .com_itens(itens)
        .constroi()
    )