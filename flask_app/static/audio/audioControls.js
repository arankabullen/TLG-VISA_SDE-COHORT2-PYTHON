// JavaScript for enhanced audio controls
document.addEventListener('DOMContentLoaded', function () {
    const audio = document.getElementById('audio');
    const playButton = document.getElementById('play');
    const pauseButton = document.getElementById('pause');
    const restartButton = document.getElementById('restart');

    playButton.addEventListener('click', function () {
        audio.play();
    });

    pauseButton.addEventListener('click', function () {
        audio.pause();
    });

    restartButton.addEventListener('click', function () {
        audio.currentTime = 0;
        audio.play();
    });
});
