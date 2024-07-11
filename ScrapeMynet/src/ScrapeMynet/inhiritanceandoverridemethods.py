class araba:
    def __init__(self, motor_hacmi, model_yılı, çekiş_tipi):   
        
        self.motor_hacmi = motor_hacmi
        self.model_yılı = model_yılı
        self.çekiş_tipi = çekiş_tipi
        
    def __str__(self):
        return f"Araba(Yıl: {self.model_yılı}, Motor Hacmi: {self.motor_hacmi}, Çekiş Tipi: {self.çekiş_tipi})"
        
class marka(araba):
    def __init__(self, isim, motor_hacmi, model_yılı, çekiş_tipi): 
        
        super().__init__(motor_hacmi, model_yılı, çekiş_tipi)
        self.isim = isim    
                
    def __str__(self):
        return f"Marka(İsim: {self.isim}, {super().__str__()})"
                
araba1 = araba("1600cc", 2020, "önden_çekiş")
marka1 = marka("mercedes", "1600cc", 2020, "önden_çekiş")
                
print(marka1)

