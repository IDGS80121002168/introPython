class OperasBas:
    #declaracion de propiedades
        num1=0
        num2=0
        res=0
        #declaracion del cosructor de la clase
        def __init__(self,a,b):
            self.num1=a
            self.num2-b
        #declaracion de los metodos de la clase
        def suma(self):
            self.res=self.num1 + self.num2
            print("la suma es: {}".format(self.res))
        
def main():
    obj=OperasBas(3,4)
    obj.suma()
    
if __name__=="__main__":
    main()