### Características da Linguagem Python

    Ao criar um atributo precedido de __ o python cria um atributo randômico para ele agir como um atributo 'private':

        class Name:
            def __init__(self,attr):
                self.__attr = attr
    

    Ao criar um método com o decorator @property fica possível acessar esse método como uma propriedade

        class Name:
            def __init__(self,attr):
                self.__attr = attr
            
            @property
            def attr(self):
                return self.__attr
        
        a = Name(attr)
        a.attr # works

    