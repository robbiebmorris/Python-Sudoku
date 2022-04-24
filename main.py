import pygame
import sys, time, random

bg = [178, 190, 181]
words = 'words.txt'
restart = 'restartfile'

class Snek:
    def __init__(self):
        
        print("Arangutype: typing at a fingers reach.")
        #presets
        self.running = False
        self.results = "analytics tbd"
        self.accuracy = "0%"
        self.reset=True

        pygame.init()
        self.w = 500
        self.h = 500
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.update()
        

    def analytics(self):
        #to do...
        return

    def reset(self):
        return
        #upon pressing tab, reselt values

    def get_word_list(self):
        return random.choice(open(words).read().split(' '))

    def running(self):
        self.running = True
        while(self.active):
            timer = pygame.time.Clock()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  running = False


if __name__ == '__main__':
    Snek().running()

    
