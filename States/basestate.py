class Base:
    """
    This is the base state for our game. All the other states will inherit this class

    Base:
        __init__()          -> constructor function
        enter(**params)     -> used in statemachin class to enter in a certain state
        render()            -> used to render the state
        update(*params)     -> updates the state
        leave()             -> exits the state and used in statemachine class
    """

    def __init__(self) -> None:pass

    def enter(self, **params) -> None: pass

    def render(self) -> None: pass

    def update(self, *params) -> None:
        self.render()
    
    def leave(self) -> None: pass