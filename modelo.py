from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
       
   
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
  
        
    
    def get_valor_medio(self,lista):
       pass
    
    def get_valor_max(self,lista):
       pass
    
    def get_valor_min(self,lista):
       pass    
                                            
        


                
        
        