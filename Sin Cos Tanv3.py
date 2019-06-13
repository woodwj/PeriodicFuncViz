import pygame
import sys
import math



#Config class - pass a reference into functions.Dont pass arguements individually but can call each attribute it needs by reference
class Config:
    def __init__(self,):
        self.width = 1024
        self.height = 768
        self.offset_forward = int(0.025*self.width)
        self.offset_back = int(0.025*self.width)
        self.center_y = int(0.5*self.height)
        self.amplitude = 0.25*self.height
        self.speed = 2
        self.radius = 3
        self.true_width = self.width - (self.offset_forward + self.offset_back)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.Func = CalcSine
        self.MenuFunc = CloseMenu



#Subroutines
def Draw(cfg):
    width, height = pygame.display.get_surface().get_size()
    pygame.draw.line(screen,cfg.WHITE,(cfg.offset_forward,0),(cfg.offset_forward,height),1)
    pygame.draw.line(screen,cfg.WHITE,(cfg.offset_forward,cfg.center_y),(width,cfg.center_y),1)
    pygame.draw.circle(screen,cfg.RED,(x,y),cfg.radius,0)

def Clear(cfg):
    x = cfg.offset_forward
    y = cfg.center_y
    screen.fill(cfg.BLACK)
    return(x,y)
    
def Update(x,cfg):
    width, height = pygame.display.get_surface().get_size()
    if x < width - cfg.offset_back:
        x += cfg.speed
    else:
        x,y = Clear(cfg)
    cfg.true_width = width - (cfg.offset_forward + cfg.offset_back)
    return(x,cfg.Func(x,cfg))
    
def CalcSine(x,cfg):
    true_x = x - cfg.offset_forward
    scale_x = 360/cfg.true_width * true_x
    rads_x = math.radians(scale_x)
    sin_x = math.sin(rads_x)
    return (CalcHeight(sin_x,cfg))

def CalcCos(x,cfg):
    true_x = x - cfg.offset_forward
    scale_x = 360/cfg.true_width * true_x
    rads_x = math.radians(scale_x)
    cos_x = math.cos(rads_x)
    return (CalcHeight(cos_x,cfg))

def CalcTan(x,cfg):
    true_x = x - cfg.offset_forward
    scale_x = 360/cfg.true_width * true_x
    rads_x = math.radians(scale_x)
    tan_x = math.tan(rads_x)
    return (CalcHeight(tan_x,cfg))
    
def CalcHeight(SinCosTanX,cfg):
    y_height = -1* SinCosTanX * cfg.amplitude
    y = int(y_height+cfg.center_y)
    return(y)

def MenuManager(cfg):
    cfg.MenuFunc(cfg)
    return(Clear(cfg))

def OpenMenu(cfg):
    width, h = pygame.display.get_surface().get_size()
    cfg.offset_forward = int(0.25*width)
    # code to write giu here
def CloseMenu(cfg):
    width, height = pygame.display.get_surface().get_size()
    cfg.offset_forward = int(0.025*width)
    
def speedUp(cfg):
    cfg.speed += 1
    if cfg.speed <= 5:
        cfg.radius +=1
    print(cfg.speed, cfg.radius)
    
def speedDown(cfg):
    cfg.speed -=1
    if cfg.speed < 5:
        cfg.radius -=1
    print(cfg.speed, cfg.radius)
pygame.init()
 
# Initialization
cfg = Config()
size = (cfg.width,cfg.height)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
x = cfg.offset_forward
y = cfg.center_y

pygame.display.set_caption("Sin Cos Tan")
 
# Loop until the user clicks the close button.
done = False 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#event dict
d_kEvents = {

pygame.K_s:CalcSine,
pygame.K_c:CalcCos,
pygame.K_t:CalcTan,
}

d_mEvents = {

pygame.K_RIGHT:OpenMenu,
pygame.K_LEFT:CloseMenu,
pygame.K_UP: speedUp,
pygame.K_DOWN: speedDown

}

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
            x,y = Clear(cfg)
        elif event.type == pygame.KEYDOWN:
            cfg.MenuFunc = d_mEvents.get(event.key,cfg.MenuFunc)
            cfg.Func = d_kEvents.get(event.key,cfg.Func)
            x,y = MenuManager(cfg)

		

    # --- Game logic should go here
    
 
    # --- Drawing code should go here
    x,y = Update(x,cfg)
    if y <= cfg.height and y>=0:
        Draw(cfg)
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
