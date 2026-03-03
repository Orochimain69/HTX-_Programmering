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
    
    """
    paddles
    """
    x_pos_paddle1 = win_width-40
    y_pos_paddle1 = 400
    y_movement_paddle1 = 1
    
    x_pos_paddle2 = 0
    y_pos_paddle2 = 400
    y_movement_paddle2 = 1
    
    
    
    """
    ball
    """
    x_pos = 700
    x_movement = 1
    y_pos = 400
    y_movement = 1
    
    
    
    
    
    
    run = True
    while run:
        #pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
        
        x_pos += x_movement
        y_pos += y_movement
    
    
        #keys = pygame.key.get_pressed()
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
            x_movement = x_movement*(-1)
            
            
            
        
        if y_pos < 0:
            y_pos = 0
            y_movement = y_movement*(-1)
            
        if x_pos > win_width-width:
            x_pos = win_width-width
            x_movement = x_movement*(-1)
        
        if y_pos > win_height-height:
            y_pos = win_height-height
            y_movement = y_movement*(-1)
        
        win.fill((RED_VALUE,GREEN_VALUE,BLUE_VALUE))   
            
        #k = random.randint(0, 255)
        #red_value = random.randint(0, 255)
        #green_value = random.randint(0,255)
        #blue_value = random.randint(0, 255)
        #win.fill((red_value,green_value,blue_value))
        #win.fill((k,k,k))
        
        
    
        
        #x_pos = 100
        #y_pos = 100
        """
        paddles
        """
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y_pos_paddle1 -= 1
             
        if keys[pygame.K_DOWN]:
             y_pos_paddle1 += 1
             
             
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y_pos_paddle2 -= 1
             
        if keys[pygame.K_s]:
            y_pos_paddle2 += 1
        
        
        
        color_box1 = (0,0,100)  
        size_box1 = (x_pos_paddle1,y_pos_paddle1,40,100)
        pygame.draw.rect(win,
                         color_box1,
                         size_box1,
                         )
        
        
         
        size_box2 = (x_pos_paddle2,y_pos_paddle2,40,100)
        pygame.draw.rect(win,
                         color_box1,
                         size_box2,
                         )
        
        
        """
        ball
        """
        
        color_box = (0,0,0)  
        size_box = (x_pos,y_pos,width,height)
        pygame.draw.rect(win,
                         color_box,
                         size_box,
                         )
        
        pygame.display.update()
    
    
    
    
    pygame.quit()

if __name__ == '__main__':
    main()
