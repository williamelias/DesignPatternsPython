from operacoes import ICMS,ISS
"""
    Padrão: Strategy aplicado em relação ao código condido no arquivo calculador_impostos
"""


class CalculadorImpostos(object):
    """
    Args: orcamento,imposto
    Return: orcamento calculado
    """
    def realiza_calculo(self,orcamento,imposto):

        imposto_calculado = imposto.calcula(orcamento)
            
        print(imposto_calculado)
    

if __name__ == '__main__': # valida se o arquivo está sendo chamado via bash/shell

    """
    Criação de Orçamento para teste do cálculo de imposto
    
    """
    from orcamento import Orcamento

    calculador = CalculadorImpostos()

    orcamento = Orcamento(600)

    # Nesse trecho temos a utilização do ducktype levando em consideração a presença do método calcula
    calculador.realiza_calculo(orcamento,ICMS())
    calculador.realiza_calculo(orcamento,ISS())
