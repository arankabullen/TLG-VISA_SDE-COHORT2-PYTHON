from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_app.gameService import GameService  # Import the GameService
import random
from FINAL_PROJECT.song import Song

# Create a Flask blueprint for the game routes
game_routes = Blueprint('game_routes', __name__)

# Initialize the game service
game_service = GameService()

@game_routes.route('/')
def start_screen():
    """
    Render the start screen where the user can enter the YouTube playlist ID and start the game.
    
    Returns:
    - Rendered HTML template: The start screen template.
    """
    print("Rendering start screen.")
    return render_template('startScreen.html')

@game_routes.route('/start', methods=['POST'])
def start_game():
    """
    Start the game by fetching the playlist from YouTube and initializing the session variables.
    The user provides a playlist ID via a form, which is then used to fetch the songs.

    Returns:
    - Redirect: Redirects the user to the first round of the game.
    """
    playlist_id = request.form.get('playlist_id')  # Get the playlist ID from the form input
    print(f"Received playlist ID: {playlist_id}")

    if not playlist_id:
        print("No playlist ID provided. Redirecting back to start screen.")
        return redirect(url_for('game_routes.start_screen'))
    
    # Reset the game state
    session['playlist'] = {title: song.to_dict() for title, song in game_service.fetch_youtube_playlist(playlist_id).items()}
    session['round'] = 0  # Reset the round counter
    session['score'] = 0  # Reset the score counter
    session['current_song'] = None  # Reset the current song
    print(f"Game state reset. Number of songs: {len(session['playlist'])}")

    return redirect(url_for('game_routes.play_round'))  # Redirect to the play round route

@game_routes.route('/round', methods=['GET', 'POST'])
def play_round():
    """
    Handle the game logic for each round. If it's a POST request, process the user's guess.
    If the guess is correct, increase the score. Otherwise, give a hint and allow another guess.
    After 3 rounds, the game ends.

    Returns:
    - Rendered HTML template: The game screen with the current song, or the end screen if the game is over.
    """
    
    current_round = session.get('round', None)
    if current_round is None:
        print("Error: Round not initialized in session.")
        return redirect(url_for('game_routes.start_game'))

    print(f"Starting round {session.get('round') + 1}...")

    if request.method == 'POST':
        # Process the user's guess
        guess = request.form['guess']  # Get the user's guess from the form
        current_song = session['current_song']  # Get the current song from the session
        correct_song_dict = session['playlist'][current_song]  # Fetch the correct song from the playlist in the session
        correct_song = Song.from_dict(correct_song_dict)

        print(f"User guessed: {guess}. Correct song: {correct_song.title}")

        if guess.lower() == correct_song.title.lower():
            # If the guess is correct, increase the score by 2 points
            session['score'] += 2
            print(f"Correct guess! Score updated to {session['score']}")
        else:
            # If the guess is incorrect, increase the score by 1 point (and give a hint)
            session['score'] += 1
            print(f"Incorrect guess. Score updated to {session['score']}")

        # Increment the round counter
        game_service.increment_round()
        print(f"Round incremented to {session['round']}")

        # Check if the game is over (3 rounds completed)
        if game_service.is_game_over():
            print("Game over. Redirecting to end screen.")
            return redirect(url_for('game_routes.end_screen'))  # Redirect to the end screen

    # If it's a GET request or the guess has been processed, move to the next song
    next_song_title = random.choice(list(session['playlist'].keys()))  # Randomly select the next song
    session['current_song'] = next_song_title  # Store the selected song in the session
    video_url = session['playlist'][next_song_title]['album_cover']  # Assuming this contains the YouTube URL

    # Sanitize the song title to create a valid filename
    sanitized_title = sanitize_filename(next_song_title)
    audio_filename = f"{sanitized_title}.wav"
    audio_path = f"static/audio/{audio_filename}"

    # Download the audio file as WAV
    if game_service.download_audio_clip(video_url, 'static/audio'):
        session['current_audio'] = f"/static/audio/{audio_filename}"  # Ensure proper path with .wav extension
        print(f"Serving audio file: {session['current_audio']}")
    else:
        print("Failed to download audio.")
        session['current_audio'] = None

    return render_template('gameScreen.html', song=next_song_title, audio_file=session['current_audio'])


@game_routes.route('/end')
def end_screen():
    """
    Display the end screen when the game is over, showing the player's final score.

    Returns:
    - Rendered HTML template: The end screen template with the final score.
    """
    final_score = session.get('score', 0)
    print(f"Game ended. Final score: {final_score}")
    return render_template('endScreen.html', score=final_score)
