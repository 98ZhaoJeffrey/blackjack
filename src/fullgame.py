
    
import pygame

class FullGame:
    def __init__(self) -> None:
        self._running = True
        self._height = 640
        self._width = 400

    def on_render(self) -> None:
        pass

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self) -> None:
        pass

    def run(self) -> None:
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()