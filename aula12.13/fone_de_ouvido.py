class FoneDeOuvido:

    def get_volume(self):
        return self.volume
    
    def set_volume(self, novo_volume):
        self.volume = novo_volume
    
    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()
fone.volume = 200 #set

print(fone.volume) #get