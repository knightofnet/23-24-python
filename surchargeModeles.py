class MaClasse :
    
    # Retourne une chaine de carctère, permettant de représenter l'instance de façon complete.
    # Utile pour débugger, dans l'interpréteur python, etc.
    # Utilitée différente de __str__().
    #
    # Ici, l'implémentation est générique pour n'importe quelle classe.
    # Retourne une chaine au format 'NomDeLaClasse (attribut1=valAttribut1, attribut2=valAttribut2, ...)'
    # A copier/coller
    def __repr__(self) :
        attributs = []
        for key,value in self.__dict__.items() :
            attributs.append("{}={}".format(key, value))         
        return "{} ({})".format(__class__.__name__, ", ".join(attributs))
    
    
    # Surcharge de la méthode __eq__() pour tester l'égalité de 2 instances.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False).
    def __eq__(self, autre) :
        return 
 
    # Surcharge de la méthode __ne__() pour tester l'inégalité de 2 instances.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False).      
    #
    # Implémentation simple, effectuant l'inverse de l'égalité
    def __ne__(self, autre) :
        return not self.__eq__(autre)   
        
    # Surcharge de la méthode __gt__() pour tester si une instance est supérieure (stricte) à une autre.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False).
    def __gt__(self, autre) :
        return 
 
    # Surcharge de la méthode __ge__() pour tester si une instance est supérieure ou égale à une autre.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False). 
    def __ge__(self, autre) :
        return 

    # Surcharge de la méthode __lt__() pour tester si une instance est inférieure (stricte) à une autre.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False).        
    def __lt__(self, autre) :
        return 

    # Surcharge de la méthode __le__() pour tester si une instance est inférieure ou égale à une autre.
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer un booléen (True ou False).
    def __le__(self, autre) :
        return       
     
    # Surcharge de la méthode __add__() pour retourner l'ajout d'une instance à une autre (avec "+").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "+"     
    def __add__(self, autre) :
        retour = MaClasse()     
        ...
        return retour
    
     
    # Surcharge de la méthode __sub__() pour retourner la différence d'une instance à une autre (avec "-").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "-"     
    def __sub__(self, autre) :
        retour = MaClasse()     
        ...
        return retour    
    
    # Surcharge de la méthode __mul__() pour retourner la multiplication d'une instance à une autre (avec "*").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "*"       
    def __mul__(self, autre) :
        retour = MaClasse()     
        ...
        return retour            
    
    
    # Surcharge de la méthode __floordiv__() pour retourner la division entière d'une instance à une autre (avec "//").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "//"       
    def __floordiv__(self, autre) :
        retour = MaClasse()     
        ...
        return retour       
    
    # Surcharge de la méthode __truediv__() pour retourner la division d'une instance à une autre (avec "/").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "/"       
    def __truediv__(self, autre) :
        retour = MaClasse()     
        ...
        return retour        
    
    # Surcharge de la méthode __pow__() pour retourner la puissance d'une instance par une autre (avec "**").
    # Prends toujours 2 arguments : self [l'instance courante] et un autre objet
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "**"       
    def __pow__(self, autre) :
        retour = MaClasse()     
        ...
        return retour        
    
    # Surcharge de la méthode __neg__() pour retourner le resultat de "-instance".
    # Ne prend qu'un 1 argument : self [l'instance courange]
    # Doit renvoyer une nouvelle instance : le résultat de l'opération "-instance"    
    def __neg__(self) :
        retour = MaClasse()     
        ...
        return retour     
    
    
    
    
    
    
    