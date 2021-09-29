from Utils.functions import Write
from States.basestate import Base

class Start(Base):
    """
    This is the first state of our game. This is the screen when player enters the game

    Inherits Base state
    """

    def __init__(self) -> None:
        super().__init__()
    
    def render(self):
        Write(text="Umbrella Game", screen=self.screen)
    
    def update(self):

        self.render()
    
    def enter(self, **params):
        self.screen = params["screen"]