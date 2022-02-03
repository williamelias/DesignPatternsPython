from operacoes import ICMS,ISS

class CalculadorImpostos(object):
    def realiza_calculo(self,orcamento,imposto):

        if imposto == 'ISS':
            imposto_calculado = ISS.calcula(orcamento)
        if imposto == 'ICMS':
            imposto_calculado = ICMS.calcula(orcamento)
            
        print(imposto_calculado)
    

if __name__ == '__main__': # valida se o arquivo está sendo chamado via bash/shell

    """
    Criação de Orçamento para teste do cálculo de imposto
    
    """
    from orcamento import Orcamento

    calculador = CalculadorImpostos()

    orcamento = Orcamento(600)

    calculador.realiza_calculo(orcamento,'ICMS')
    calculador.realiza_calculo(orcamento,'ISS')
