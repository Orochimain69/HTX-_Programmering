import random
import pygame

def main():
    
    win_width = 1400
    win_height = 800
    
    pygame.init()
    win = pygame.display.set_mode((win_width,win_height))
    
    
    RED_VALUE = 255
    GREEN_VALUE = 255
    BLUE_VALUE = 255
    
    
    win.fill((RED_VALUE,GREEN_VALUE,BLUE_VALUE))
    width = 10
    height = 10
    
    x_pos = 0
    y_pos = 0
    
    run = True
    while run:
        #pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             
#             x_pos -= 1
#             #x_pos =- 1
#             #print(x_pos)
#             
#         if keys[pygame.K_RIGHT]:
#             x_pos += 1
#             #x_pos =+ 1
#             
#         if keys[pygame.K_UP]:
#             y_pos -= 1
#             #y_pos =- 1
#             
#         if keys[pygame.K_DOWN]:
#             y_pos += 1
#             #y_pos =+ 1
        
        if x_pos < 0:
            x_pos = 0
        
        if y_pos < 0:
            y_pos = 0
            
        if x_pos > win_width-width:
            x_pos = win_width-width
        
        if y_pos > win_height-height:
            y_pos = win_height-height
        
        win.fill((RED_VALUE,GREEN_VALUE,BLUE_VALUE))   
            
        #k = random.randint(0, 255)
        #red_value = random.randint(0, 255)
        #green_value = random.randint(0,255)
        #blue_value = random.randint(0, 255)
        #win.fill((red_value,green_value,blue_value))
        #win.fill((k,k,k))
        
        
    
        
        #x_pos = 100
        #y_pos = 100
        color_box = (0,0,0)  
        size_box = (x_pos,y_pos,width,height)
        pygame.draw.rect(win,
                         color_box,
                         size_box,
                         )
        
        
            
        """
        x_pos = random.randint(0, 800)
        y_pos = random.randint(0, 600)
        width = random.randint(0, 100)
        height = random.randint(0, 100)
        
        pygame.time.delay(200)
        
        color_box = (0,0,0)
        color_box2 = (255,255,255)
        size_box = (x_pos,y_pos,width,height)
        pygame.draw.rect(win,
                         color_box,
                         size_box,
                         )
        
        """
        """
        x2_pos = 600
        y2_pos = 100
        
        
        size_box2 = (x2_pos,y2_pos,width,height)
        pygame.draw.rect(win,
                         color_box,
                         size_box2,
                         )


        x3_pos = 300
        y3_pos = 400
        width_mouth = 200
        height_mouth = 70
        
        
        size_box3 = (x3_pos,y3_pos,width_mouth,height_mouth)
        pygame.draw.rect(win,
                         color_box,
                         size_box3,
                         )
        
        
        """'''blinking'''"""
        
        pygame.time.delay(1000)
        
        pygame.draw.rect(win,
                         color_box2,
                         size_box,
                         )
        
        
        
        pygame.draw.rect(win,
                         color_box2,
                         size_box2,
                         )
        
        """
        
        
        
        pygame.display.update()
    
    
    
    
    pygame.quit()



if __name__ == '__main__':
    main()
