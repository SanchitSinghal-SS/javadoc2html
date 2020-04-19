package oop.gamebot.games;

/**
 * Game implementation interface
 * @author Katyaeva Daria (https://github.com/DariaKatyaevaa)
 * @version 2.1
 * @deprecated  As of release 2.3
 */
public interface Game {
    boolean isPlaying;
    String startGame();
    void resetGame();
    String giveAnswerToUser(String message);
}
