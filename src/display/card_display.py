import pygame

class CardDisplay(pygame.sprite.Sprite):
    def __init__(self, card, surface_size, x, y):
        super().__init__()
        self.card = card  # Reference to the card object
        self.image = pygame.Surface(surface_size)
        self.image.fill((255, 255, 255))  # White background

        # Load card face image based on the card data from the Card object
        card_face_image = pygame.image.load(f"card_faces/{card.rank.value}_of_{card.suit.value}.png")
        self.image.blit(card_face_image, (x, y))

        self.rect = self.image.get_rect()

    # Optional method to draw card back (using Card class info)
    def draw_back(self):
        self.image.fill((0, 0, 0))  # Black background for card back

    # Optional method to update display based on card changes (e.g., flipping)
    def update(self):
        # Update image or other visual aspects based on the card object's state
        pass
