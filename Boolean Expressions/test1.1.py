###################################################################
# Name : Suphinya Wu
# ID : 6201012630100
###################################################################


class exptt() :               
    
    def __init__(self,func) :       
        self.func = func           
        self.tree = []
        for i in range(len(func)) :     
            if func[i] == '(' or func[i] == ')' :      
                pass
            else :
                self.tree.append(func[i])         
        
        self.mylist = ['None'] * 15          
        

    def trans(self) :                                          
        n = 0

        self.boo = []
        for i in range(len(self.func)):
            if self.func[i] == 'I' and self.func[i+1] == '0' :
                self.boo += ['I0']
                
            if self.func[i] == 'I' and self.func[i+1] == '1' :
                self.boo += ['I1']
                
            if self.func[i] == 'I' and self.func[i+1] == '2' :
                self.boo += ['I2']
                
            if self.func[i] == 'I' and self.func[i+1] == '3' :
                self.boo += ['I3']
                
            if self.func[i] in '01' and self.func[i-1] != 'I':
                self.boo += self.func[i]
                
            if self.func[i] in '+!&()' :
                self.boo += self.func[i]
        

        for i in self.boo :                           
            self.left = (n * 2) + 1                        
            self.right = (n * 2) + 2                      
            if i == '(' :                                
                if self.mylist[self.left] == 'None' :      
                    n = self.left
                else :                                              
                    n = self.right
            elif i == 'I1' or i == 'I0' or i == 'I2' or i == 'I3' or i == '1' or i == '0' :                         
                if self.mylist[self.left] == 'None' :      
                    self.mylist[self.left] = i
                else :
                    self.mylist[self.right] = i
            elif i in '+&!' :                                      
                self.mylist[n] = i 
                
            else :                              
                if n%2 == 1 :                   
                    n = int((n-1)/2)
                else :
                    n = int((n-2)/2)             
                    
        return self.mylist
                 
        
f = input("input function : ") 
n = f.replace(" ", "")
print(n)
test = exptt(n)
show = test.trans()
print(show)


import pygame,sys

width = 1200
height = 880

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Expresstion Tree")

w0,h0 = 600,80
w1,h1 = 300,220
w2,h2 = 900,220
w3,h3 = 150,440
w4,h4 = 450,440
w5,h5 = 750,440
w6,h6 = 1050,440
w7,h7 = 75,660
w8,h8 = 225,660
w9,h9 = 375,660
w10,h10 = 525,660
w11,h11 = 675,660
w12,h12 = 825,660
w13,h13 = 975,660
w14,h14 = 1125,660



while True:


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #screen.fill(0,0,0)
    font = pygame.font.SysFont("Adobe Devanagari", 80)


    if show[0] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w0,h0),40)
        text = font.render(show[0], True, (255,255,255))
        screen.blit(text,(w0-18,h0-30))

    if show[1] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w1,h1),40)
        text = font.render(show[1], True, (255,255,255))
        screen.blit(text,(w1-17,h1-30))
        pygame.draw.line(screen,(0,128,255),(w0-30,h0),(w1+30,h1),10)
    
    if show[2] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w2,h2),40)
        text = font.render(show[2], True, (255,255,255))
        screen.blit(text,(w2-17,h2-30))
        pygame.draw.line(screen,(0,128,255),(w0+30,h0),(w2-30,h2),10)

    if show[3] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w3,h3),40)
        text = font.render(show[3], True, (255,255,255))
        screen.blit(text,(w3-17,h3-30))
        pygame.draw.line(screen,(0,128,255),(w1-30,h1+20),(w3+30,h3),10)

    if show[4] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w4,h4),40)
        text = font.render(show[4], True, (255,255,255))
        screen.blit(text,(w4-17,h4-30))
        pygame.draw.line(screen,(0,128,255),(w1+30,h1+20),(w4-30,h4),10)

    if show[5] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w5,h5),40)
        text = font.render(show[5], True, (255,255,255))
        screen.blit(text,(w5-17,h5-30))
        pygame.draw.line(screen,(0,128,255),(w2-30,h2+20),(w5+30,h5),10)
    
    if show[6] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w6,h6),40)
        text = font.render(show[6], True, (255,255,255))
        screen.blit(text,(w6-17,h6-30))
        pygame.draw.line(screen,(0,128,255),(w2+30,h2+20),(w6-30,h6),10)

    if show[7] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w7,h7),40)
        text = font.render(show[7], True, (255,255,255))
        screen.blit(text,(w7-17,h7-30))
        pygame.draw.line(screen,(0,128,255),(w3-30,h3+20),(w7+30,h7),10)

    if show[8] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w8,h8),40)
        text = font.render(show[8], True, (255,255,255))
        screen.blit(text,(w8-17,h8-30))
        pygame.draw.line(screen,(0,128,255),(w3+30,h3+20),(w8-30,h8),10)

    if show[9] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w9,h9),40)
        text = font.render(show[9], True, (255,255,255))
        screen.blit(text,(w9-17,h9-30))
        pygame.draw.line(screen,(0,128,255),(w4-30,h4+20),(w9+30,h9),10)
    
    if show[10] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w10,h10),40)
        text = font.render(show[10], True, (255,255,255))
        screen.blit(text,(w10-17,h10-30))
        pygame.draw.line(screen,(0,128,255),(w4+30,h4+20),(w10-30,h10),10)

    if show[11] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w11,h11),40)
        text = font.render(show[11], True, (255,255,255))
        screen.blit(text,(w11-17,h11-30))
        pygame.draw.line(screen,(0,128,255),(w5-30,h5+20),(w11+30,h11),10)

    if show[12] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w12,h12),40)
        text = font.render(show[12], True, (255,255,255))
        screen.blit(text,(w12-17,h12-30))
        pygame.draw.line(screen,(0,128,255),(w5+30,h5+20),(w12-30,h12),10)

    if show[13] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w13,h13),40)
        text = font.render(show[13], True, (255,255,255))
        screen.blit(text,(w13-17,h13-30))
        pygame.draw.line(screen,(0,128,255),(w6-30,h6+20),(w13+30,h13),10)

    if show[14] != 'None':
        pygame.draw.circle(screen,(0,128,255),(w14,h14),40)
        text = font.render(show[14], True, (255,255,255))
        screen.blit(text,(w14-17,h14-30))
        pygame.draw.line(screen,(0,128,255),(w6+30,h6+20),(w14-30,h14),10)

    
    pygame.display.update()


print("Done...")
#####################################################




