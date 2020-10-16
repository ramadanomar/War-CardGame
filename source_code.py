class Carte:
    suits = ["Inima Neagra","Inima Rosie","Romb","Trefla"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8","9","10","J","Q","K","A"]
    
    def __init__(self, v, s):  # 7 de Inima Neagra 
        """suits+value are ints"""
        self.value = v # value = 7
        self.suit = s  # suit  = Inima Neagra
        
    def __lt__(self, c2):  #Functie Magica pentru lower than (schimba cum comparam clasa)
        if self.value < c2.value: # verificam numar
            return True # daca c2>self => Adv
        if self.value == c2.value: # daca numerele sunt egale (ex. K cu K)
            if self.suit <c2.suit: # comparam in functie de semn
                return True 
            else:
                return False
        return False # daca c2<self => Fals
    
    def __gt__(self, c2): #Functie Magica pentru greater than
        if self.value > c2.value: #Verifica valoarea
            return True 
        if self.value == c2.value: #Verifica semn
            if self.suit > c2.suit: 
                return True
            else:
                return False
        return False
    
    def __repr__(self): #Functie magica pentru printat
        v = self.values[self.value] + " de " + self.suits[self.suit] # Se printeaza K de Inima Neagra
        return v
        
from random import shuffle #Importare dependenta Random - Shuffle

class Deck:
    def __init__(self): # Initializare
        self.cards = [] # Lista cu toate cartile dintr un deck
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Carte(i, j))
        shuffle(self.cards) # Amestecare carti
        
    def rm_card(self): #Metoda de scoate a unui card
        if len(self.cards) == 0: #Daca nu mai are carti in deck intoarce fals
            return
        return self.cards.pop() #Altfel scoate cartea
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
    
class Game:
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        
        self.deck = Deck() #Creaza pachetul de carti
        
        self.p1 = Player(name1) #Adaugare primu jucator
        self.p2 = Player(name2) #Adaugare al doilea jucator
        
    def wins(self,winner): #Printare nume persoana care a castigat
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    
    def draw(self,p1n,p1c,p2n,p2c): # Metoda de a trage carti din pachet
        d = "{} drew {} | {} drew {}" 
        d = d.format(p1n, p1c, p2n, p2c)
        print(d) #Printeaza "Jucator 1 drew CarteJucator1 | Jucator2 drew CarteJucator2
        
    def winner(self, p1, p2): #Functie pentru a arata cine a castigat
            if p1.wins > p2.wins: #comparam castigurile lui p1 cu p2
                return p1.name
            if p2.wins > p1.wins: 
                return p2.name
            return "A fost egalitate!" #Daca amanadoua sunt egale se intoarce String
        
    def play_game(self):
        cards = self.deck.cards
        print("Jocul a inceput! Facut de Ramadan Omar")
        
        while len(cards) >= 2:
            m = "q to quit. Any" + "key to play"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card() # Player1 Trage o carte
            p2c = self.deck.rm_card() # Player2 Trage o carte
            
            p1n = self.p1.name
            p2n = self.p2.name
            
            self.draw(p1n,p1c,p2n,p2c) # Se trage o carte pentru fiecare
            
            if p1c > p2c: #Daca cartea lui Player1 este mai mare
                self.p1.wins += 1 #Incrementare castiguri
                self.wins(self.p1.name) #Printeaza Player 1 a castigat
            else: # Daca Cartea jucatorului 2 este mai mare
                self.p2.wins += 1 #Incrementare castiguri
                self.wins(self.p2.name) #Printeaza Player 2 a castigat
            
        win = self.winner(self.p1, self.p2)
        print("\n\nRazboiul a fost terminat. {} castiga".format(win) )
        print("Jocul a fost creat de Ramadan Omar, sper ca v-a placut :)")
            
    def winner(self, p1, p2): #Functie pentru a arata cine a castigat
        if p1.wins > p2.wins: #comparam castigurile lui p1 cu p2
            return p1.name
        if p2.wins > p1.wins: 
            return p2.name
        return "A fost egalitate!" #Daca amanadoua sunt egale se intoarce String
            

            
game = Game()
game.play_game()