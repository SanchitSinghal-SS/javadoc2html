package oop.gamebot;

import oop.gamebot.games.calculate.GameCalculate;
import oop.gamebot.games.cities.GameCities;
import oop.gamebot.games.thesaurus.GameThesaurus;
import oop.gamebot.games.words.GameWords;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

/**
 * Class for processing chat user messages and managing games in it
 * @author Katyaeva Daria
 * @version 2.1
 * @since   1.2
 * @see Game
*/

public class ChatManager
{
    private Long chatId;
    private Map<Integer, User> users;
    private MessageHandler messageHandler;
    private boolean isPlaying;
    private boolean isPlayingWord;
    private boolean isPlayingCity;
    private boolean isPlayingCalculate;
    private boolean isPlayingThesaurus;
    private GameWords gameWords;
    private GameCities gameCities;
    private GameCalculate gameCalculate;
    private GameThesaurus gameThesaurus;
    private User user = new User(0);


    /**
    * Class Constructor
    * @param chatId Long
    * @exception IOException
    * @throws ParseException
    */
    ChatManager(Long chatId)
    {
        this.chatId = chatId;
        users = new HashMap<>();
        messageHandler = new MessageHandler(user);
        gameWords = new GameWords(user);
        gameCalculate = new GameCalculate(user);
        gameCities = new GameCities(user);
        gameThesaurus = new GameThesaurus(user);
        isPlaying = false;
        isPlayingWord = false;
        isPlayingCity = false;
        isPlayingCalculate = false;
        isPlayingThesaurus = false;

    }

    /**
    * @return Long chat ID
    */
    public Long getChatId()
    {
        return chatId;
    }

    /**
    * @return Map<Integer, User> Key - user ID, value - user
    */
    Map<Integer, User> getUsers()
    {
        return users;
    }

    /**
    * @return User user who last sent message
    */
    User getUser()
    {
        return user;
    }

    /**
    * @return GameThesaurus
    * It is super class of {@link Game}
    */
    GameThesaurus getGameThesaurus()
    {
        return gameThesaurus;
    }

    GameWords getGameWords()
    {
        return gameWords;
    }

    GameCalculate getGameCalculate()
    {
        return gameCalculate;
    }

    GameCities getGameCities()
    {
        return gameCities;
    }

    /**
    *  Method for adding a new user to Map
    *  @param userId
    *  @param user object with user data
    */
    void addUser(Integer userId, User user)
    {
        if(!users.containsKey(userId))
        {
            users.put(userId, user);
        }
    }

    MessageHandler getMessageHandler()
    {
        return messageHandler;
    }


    boolean isPlaying()
    {
        return isPlaying;
    }

    boolean isPlayingWord()
    {
        return isPlayingWord;
    }

    boolean isPlayingCalculate()
    {
        return isPlayingCalculate;
    }

    boolean isPlayingCity()
    {
        return isPlayingCity;
    }

    void isPlaying(boolean status)
    {
        isPlaying = status;
    }

    void isPlayingWord(boolean status)
    {
        isPlayingWord = status;
    }

    void isPlayingCalculate(boolean status)
    {
        isPlayingCalculate = status;
    }

    void isPlayingCity(boolean status)
    {
        isPlayingCity = status;
    }

    boolean isPlayingThesaurus()
    {
        return isPlayingThesaurus;
    }

    void isPlayingThesaurus(boolean status)
    {
        isPlayingThesaurus = status;
    }
}