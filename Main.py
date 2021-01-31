import pygame
from pygame.locals import *
import Maker
import time
import math
import Game

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

pygame.init()

increment = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((40, 40, 40))
pygame.display.set_caption("Speed Typing Test")
running = True
current_screen = "menu"
previous_screen = ""
correct_words = 0
first_time = True
display_wpm = False
letter_to_type = 0
key_record = []
shift = 1


def main_menu(mouse_pos):
    global current_screen
    global increment

    button_colour_1 = (20, 20, 20)
    button_colour_2 = (255, 0, 0)
    font = pygame.font.SysFont("Rockwell", 40)
    # main game text
    game_text = font.render("Speed Typing Test", False, (255, 255, 255))
    screen.blit(game_text, (525, 100))

    # button1 - player statistics
    stats_button = Maker.button((SCREEN_WIDTH / 2) - 150, SCREEN_HEIGHT - 125, 100, 50, button_colour_1, "stats")
    stats_button.mouse_over(mouse_pos)
    stats_button.draw(screen)

    # button1 - start test
    play_button = Maker.button((SCREEN_WIDTH / 2) + 50, SCREEN_HEIGHT - 125, 100, 50, button_colour_1, "start")
    play_button.mouse_over(mouse_pos)
    play_button.draw(screen)

    for menu_event in pygame.event.get():
        if menu_event.type == MOUSEBUTTONDOWN:
            if play_button.mouse_click(pygame.mouse.get_pos()):
                current_screen = "game"
            elif stats_button.mouse_click(pygame.mouse.get_pos()):
                current_screen = "stats"


def stats_screen():
    pass


while running:
    # updates display
    if previous_screen != current_screen:
        #print("previous", previous_screen, "current", current_screen)
        screen.fill((40, 40, 40))
    if current_screen == "game":
        previous_screen = current_screen
        if first_time:
            start_time = time.time()
        button_keys, character_list, words, letters, time_left, wpm = Game.game_screen(screen, increment, start_time, correct_words)
        if time_left < 0:
            current_screen = "menu"
            display_wpm = True
        #print("letter to type", letters[letter_to_type])
        increment = False
    elif current_screen == "stats":
        previous_screen = current_screen
        stats_screen()
    elif current_screen == "menu":
        previous_screen = current_screen
        main_menu(pygame.mouse.get_pos())
        if display_wpm:
            wpm_to_type = "WPM: {}".format(round(wpm, 1))
            time_text = Maker.text((255, 255, 255), 625, 380)
            time_text.draw(wpm_to_type, screen)
            display_wpm = False


    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in button_keys.keys():
                if event.key == K_RSHIFT or event.key == K_LSHIFT:
                    shift = 2
                elif event.key == K_BACKSPACE:
                    increment = ((character_list[letter_to_type].get_info()[0] / 2) + 1 + (character_list[letter_to_type - 1].get_info()[0] / 2)) * -1
                    character_list[letter_to_type - 1].set_colour("normal")
                    key_record.pop()
                    letter_to_type -= 1

                elif button_keys[event.key][shift] == letters[letter_to_type]:
                    if first_time:
                        start_time = time.time()
                        first_time = False
                    increment = ((character_list[letter_to_type].get_info()[0] / 2) + 1) + (character_list[letter_to_type + 1].get_info()[0] / 2)
                    character_list[letter_to_type].set_colour("correct")
                    button_keys[event.key][0].colour_change("correct")
                    key_record.append(button_keys[event.key][shift])
                    letter_to_type += 1

                elif button_keys[event.key][shift] != letters[letter_to_type]:
                    if first_time:
                        start_time = time.time()
                        first_time = False
                    increment = ((character_list[letter_to_type].get_info()[0] / 2) + 1) + (character_list[letter_to_type + 1].get_info()[0] / 2)
                    character_list[letter_to_type].set_colour("wrong")
                    button_keys[event.key][0].colour_change("wrong")
                    key_record.append(button_keys[event.key][shift])
                    letter_to_type += 1

                typed_words = "".join(key_record)
                typed_words = typed_words.split()
                #print("typed", typed_words)
                #print("words", words)
                correct_words = 0
                checked = []
                for i in typed_words:
                    if i in words:
                        correct_words += 1
                #print(correct_words)


            elif event.key == K_ESCAPE:
                # quits the game is the ESCAPE key is pressed
                running = False

        elif event.type == KEYUP:
            if event.key == K_LSHIFT or event.key == K_RSHIFT:
                shift = 1
            if event.key in button_keys.keys():
                button_keys[event.key][0].colour_change("normal")
