class state:
    """
    The GameState class manages the current state of the game, 
    including the round number and the player's score.
    """

    def __init__(self):
        """
        Initialize the game state with the first round (0) and a score of 0.
        """
        self.current_round = 0
        self.score = 0

    def increment_round(self):
        """
        Increment the current round by 1. This method is called at the start of each new round.
        """
        self.current_round += 1

    def update_score(self, points):
        """
        Update the player's score by adding the specified number of points.
        
        Parameters:
        - points (int): The number of points to add to the current score.
        """
        self.score += points

    def is_game_over(self):
        """
        Check if the game is over. The game ends after 3 rounds.

        Returns:
        - bool: True if the game is over, False otherwise.
        """
        return self.current_round >= 3
