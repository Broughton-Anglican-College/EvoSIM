import pygame
import sys

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (64, 64, 64)

class Button:
    def __init__(self, x, y, width, height, text, font, accessible_name=None, image_path=None, light_style=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.hovered = False
        self.accessible_name = accessible_name or text
        self.image = None
        self.light_style = light_style
        
        # Load image if provided
        if image_path:
            try:
                self.image = pygame.image.load(image_path)
                # Scale image to fit button with more padding (half size)
                padding = 20
                img_size = min(width - padding, height - padding)
                self.image = pygame.transform.scale(self.image, (img_size, img_size))
            except pygame.error:
                print(f"Could not load image: {image_path}")
                self.image = None
        
    def draw(self, screen):
        if self.light_style:
            # Lighter green style for settings button
            color = (80, 120, 90) if not self.hovered else (100, 140, 110)
            border_color = (120, 160, 130) if self.hovered else (100, 140, 110)
        else:
            # Darker green/teal rounded rectangle style for regular buttons
            color = (30, 45, 35) if not self.hovered else (40, 55, 45)
            border_color = (60, 80, 70) if self.hovered else (50, 70, 60)
        
        pygame.draw.rect(screen, color, self.rect, border_radius=15)
        pygame.draw.rect(screen, border_color, self.rect, width=2, border_radius=15)
        
        # Draw image if available, otherwise draw text
        if self.image:
            img_rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, img_rect)
        else:
            text_surface = self.font.render(self.text, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class BaseState:
    def __init__(self, screen, background=None):
        self.screen = screen
        self.background = background
    
    def handle_event(self, event):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def draw_background(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(BLACK)

class HomePage(BaseState):
    def __init__(self, screen, background=None):
        super().__init__(screen, background)
        self.font_title = pygame.font.Font(None, 120)
        self.font_subtitle = pygame.font.Font(None, 48)
        self.font_button = pygame.font.Font(None, 36)
        
        # Button dimensions and positioning - smaller buttons
        button_width = 400
        button_height = 70
        button_spacing = 25
        start_y = SCREEN_HEIGHT // 2 - 20
        
        # Settings button in top right
        settings_size = 60
        settings_margin = 20
        
        self.buttons = {
            'new': Button(
                SCREEN_WIDTH // 2 - button_width // 2,
                start_y,
                button_width, button_height,
                "Start New Simulation",
                self.font_button
            ),
            'load': Button(
                SCREEN_WIDTH // 2 - button_width // 2,
                start_y + button_height + button_spacing,
                button_width, button_height,
                "Load Saved Simulation",
                self.font_button
            ),
            'tutorial': Button(
                SCREEN_WIDTH // 2 - button_width // 2,
                start_y + 2 * (button_height + button_spacing),
                button_width, button_height,
                "Tutorial",
                self.font_button
            ),
            'settings': Button(
                SCREEN_WIDTH - settings_size - settings_margin,
                settings_margin,
                settings_size, settings_size,
                "Settings",
                pygame.font.Font(None, 18),
                "Settings Menu",
                "settings_icon.png",  # Add your settings icon here
                light_style=True     # Use lighter green style
            )
        }
    
    def handle_event(self, event):
        for name, button in self.buttons.items():
            if button.handle_event(event):
                return name
        return None
    
    def draw(self):
        self.draw_background()
        
        # Main title "EvoSim" - darker color for better contrast
        title_text = self.font_title.render("EvoSim", True, (40, 60, 50))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(title_text, title_rect)
        
        # Buttons
        for button in self.buttons.values():
            button.draw(self.screen)

class SimulationState(BaseState):
    def __init__(self, screen):
        super().__init__(screen)
    
    def draw(self):
        self.screen.fill(DARK_GRAY)
        font = pygame.font.Font(None, 48)
        text = font.render("Simulation Running - Press ESC to return", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

class LoadState(BaseState):
    def __init__(self, screen):
        super().__init__(screen)
    
    def draw(self):
        self.screen.fill(DARK_GRAY)
        font = pygame.font.Font(None, 48)
        text = font.render("Load Menu - Press ESC to return", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

class TutorialState(BaseState):
    def __init__(self, screen):
        super().__init__(screen)
    
    def draw(self):
        self.screen.fill(DARK_GRAY)
        font = pygame.font.Font(None, 48)
        text = font.render("Tutorial - Press ESC to return", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

class SettingsState(BaseState):
    def __init__(self, screen):
        super().__init__(screen)
    
    def draw(self):
        self.screen.fill(DARK_GRAY)
        font = pygame.font.Font(None, 48)
        text = font.render("Settings - Press ESC to return", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Evolution Simulator")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Load background
        try:
            self.background = pygame.image.load("background1.jpg")
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except pygame.error:
            self.background = None
        
        # State management
        self.states = {
            'home': HomePage(self.screen, self.background),
            'simulation': SimulationState(self.screen),
            'load': LoadState(self.screen),
            'tutorial': TutorialState(self.screen),
            'settings': SettingsState(self.screen)
        }
        self.current_state = 'home'
    
    def change_state(self, new_state):
        if new_state in self.states:
            self.current_state = new_state
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # ESC key returns to home from any state
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.current_state != 'home':
                    self.change_state('home')
                    continue
            
            # Handle current state events
            current_state_obj = self.states[self.current_state]
            
            if self.current_state == 'home':
                button_clicked = current_state_obj.handle_event(event)
                if button_clicked:
                    self.handle_button_click(button_clicked)
            else:
                current_state_obj.handle_event(event)
    
    def handle_button_click(self, button_name):
        if button_name == 'new':
            self.change_state('simulation')
        elif button_name == 'load':
            self.change_state('load')
        elif button_name == 'tutorial':
            self.change_state('tutorial')
        elif button_name == 'settings':
            self.change_state('settings')
    
    def update(self):
        self.states[self.current_state].update()
    
    def draw(self):
        self.states[self.current_state].draw()
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.run()