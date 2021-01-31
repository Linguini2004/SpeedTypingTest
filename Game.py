import pygame
from pygame.locals import *
import Maker
import time
import string

pygame.init()

counter = 0
previous_x = 688
keys = []
character_list = []
wpm = 0

def game_screen(surface, increment, start_time, correct_words):
    global counter
    global keys
    global previous_x
    global character_list
    global wpm
    letter_list = []
    duration = (time.time() - start_time) + 0.00001

    surface.fill((40, 40, 40))

    f = open("C:/Users/david/Documents/other_documents/pyhton/Arkwright project/Speed_typing_test/Sample_text", "r")
    for line in f:
        for letter in line:
            letter_list.append(letter)

    text = "".join(letter_list)
    text = text.replace("\n", " ")
    encoded = text.encode('cp1252')
    final_text = encoded.decode('utf-8')

    counter += 1

    pygame.draw.rect(surface, (255, 255, 255), [0, 75, 1400, 50])
    pygame.draw.line(surface, (150, 150, 150), (0, 75), (1400, 75), 2)
    pygame.draw.line(surface, (150, 150, 150), (0, 125), (1400, 125), 2)
    pygame.draw.polygon(surface, (34, 97, 146), ((695, 126), (705, 126), (700, 118)))
    pygame.draw.polygon(surface, (34, 97, 146), ((695, 76), (705, 76), (700, 85)))

    to_type = "Time left: {} s".format(round((60 - duration), 1))
    time_text = Maker.text((255, 255, 255), 20, 20)
    time_text.draw(to_type, surface)

    if round((60 - duration), 1) % 1 == 0 and duration > 3:
        wpm = correct_words / (duration / 60)
    wpm_to_type = "WPM: {}".format(round(wpm, 1))
    time_text = Maker.text((255, 255, 255), 625, 20)
    time_text.draw(wpm_to_type, surface)

    words = final_text.split()
    letters = list(final_text)

    if counter == 1:
        keys = create_button()
        for letter in letters:
            character_list.append(Maker.letter(letter))
        x_coord = 700

    x_coord = previous_x

    if increment != 0:
        x_coord -= increment
        previous_x = x_coord

    for i, char in enumerate(character_list):
        if i == 0:
            char.draw(surface, x_coord, 83)
            previous_charx = x_coord
        else:
            char.draw(surface, previous_charx + width + 1, 83)
            previous_charx = previous_charx + width + 1
        width, height = char.get_info()

    for key in keys:
        keys[key][0].draw(surface)

    return keys, character_list, words, letters, (60 - duration), wpm


def create_button():
    one_button = Maker.button(180, 200, 60, 70, (20, 20, 20), "1")
    two_button = Maker.button(260, 200, 60, 70, (20, 20, 20), "2")
    three_button = Maker.button(340, 200, 60, 70, (20, 20, 20), "3")
    four_button = Maker.button(420, 200, 60, 70, (20, 20, 20), "4")
    five_button = Maker.button(500, 200, 60, 70, (20, 20, 20), "5")
    six_button = Maker.button(580, 200, 60, 70, (20, 20, 20), "6")
    seven_button = Maker.button(660, 200, 60, 70, (20, 20, 20), "7")
    eight_button = Maker.button(740, 200, 60, 70, (20, 20, 20), "8")
    nine_button = Maker.button(820, 200, 60, 70, (20, 20, 20), "9")
    zero_button = Maker.button(900, 200, 60, 70, (20, 20, 20), "0")

    us_button = Maker.button(980, 200, 60, 70, (20, 20, 20), "-")
    equal_button = Maker.button(1060, 200, 60, 70, (20, 20, 20), "=")
    back_button = Maker.button(1140, 200, 120, 70, (20, 20, 20), "bck")
    tab_button = Maker.button(100, 290, 80, 70, (20, 20, 20), "tab")

    Q_button = Maker.button(200, 290, 60, 70, (20, 20, 20), "Q")
    W_button = Maker.button(280, 290, 60, 70, (20, 20, 20), "W")
    E_button = Maker.button(360, 290, 60, 70, (20, 20, 20), "E")
    R_button = Maker.button(440, 290, 60, 70, (20, 20, 20), "R")
    T_button = Maker.button(520, 290, 60, 70, (20, 20, 20), "T")
    Y_button = Maker.button(600, 290, 60, 70, (20, 20, 20), "Y")
    U_button = Maker.button(680, 290, 60, 70, (20, 20, 20), "U")
    I_button = Maker.button(760, 290, 60, 70, (20, 20, 20), "I")
    O_button = Maker.button(840, 290, 60, 70, (20, 20, 20), "O")
    P_button = Maker.button(920, 290, 60, 70, (20, 20, 20), "P")

    sqro_button = Maker.button(1000, 290, 60, 70, (20, 20, 20), "[")
    sqrc_button = Maker.button(1080, 290, 60, 70, (20, 20, 20), "]")
    bslash_button = Maker.button(1160, 290, 100, 70, (20, 20, 20), "\\")

    caps_button = Maker.button(100, 380, 100, 70, (20, 20, 20), "caps")
    A_button = Maker.button(220, 380, 60, 70, (20, 20, 20), "A")
    S_button = Maker.button(300, 380, 60, 70, (20, 20, 20), "S")
    D_button = Maker.button(380, 380, 60, 70, (20, 20, 20), "D")
    F_button = Maker.button(460, 380, 60, 70, (20, 20, 20), "F")
    G_button = Maker.button(540, 380, 60, 70, (20, 20, 20), "G")
    H_button = Maker.button(620, 380, 60, 70, (20, 20, 20), "H")
    J_button = Maker.button(700, 380, 60, 70, (20, 20, 20), "J")
    K_button = Maker.button(780, 380, 60, 70, (20, 20, 20), "K")
    L_button = Maker.button(860, 380, 60, 70, (20, 20, 20), "L")
    scol_button = Maker.button(940, 380, 60, 70, (20, 20, 20), ";")
    apos_button = Maker.button(1020, 380, 60, 70, (20, 20, 20), "'")
    enter_button = Maker.button(1100, 380, 160, 70, (20, 20, 20), "Enter")

    lshift_button = Maker.button(100, 470, 160, 70, (20, 20, 20), "shift")
    Z_button = Maker.button(280, 470, 60, 70, (20, 20, 20), "Z")
    X_button = Maker.button(360, 470, 60, 70, (20, 20, 20), "X")
    C_button = Maker.button(440, 470, 60, 70, (20, 20, 20), "C")
    V_button = Maker.button(520, 470, 60, 70, (20, 20, 20), "V")
    B_button = Maker.button(600, 470, 60, 70, (20, 20, 20), "B")
    N_button = Maker.button(680, 470, 60, 70, (20, 20, 20), "N")
    M_button = Maker.button(760, 470, 60, 70, (20, 20, 20), "M")
    com_button = Maker.button(840, 470, 60, 70, (20, 20, 20), ",")
    stop_button = Maker.button(920, 470, 60, 70, (20, 20, 20), ".")
    fslash_button = Maker.button(1000, 470, 60, 70, (20, 20, 20), "/")
    rshift_button = Maker.button(1080, 470, 180, 70, (20, 20, 20), "shift")

    space_button = Maker.button(440, 560, 380, 70, (20, 20, 20), "space")

    return {K_1: [one_button, "1", "!"], K_2: [two_button, "2", '"'], K_3: [three_button, "3", "£"], K_4: [four_button, "4", "$"]
        , K_5: [five_button, "5", "%"], K_6: [six_button, "6", "^"], K_7: [seven_button, "7", "&"]
        , K_8: [eight_button, "8", "*"], K_9: [nine_button, "9", "("], K_0: [zero_button, "0", ")"], K_MINUS: [us_button, "-", "_"]
        , K_EQUALS: [equal_button, "=", "+"], K_BACKSPACE: [back_button, "", ""], K_TAB: [tab_button, "", ""]
        , K_q: [Q_button, "q", "Q"], K_w: [W_button, "w", "W"], K_e: [E_button, "e", "E"], K_r: [R_button, "r", "R"]
        , K_t: [T_button, "t", "T"], K_y: [Y_button, "y", "Y"], K_u: [U_button, "u", "U"], K_i: [I_button, "i", "I"]
        , K_o: [O_button, "o", "O"], K_p: [P_button, "p", "P"], K_LEFTBRACKET: [sqro_button, "[", "{"], K_RIGHTBRACKET: [sqrc_button, "]", "}"]
        , K_BACKSLASH: [bslash_button, '\\', "|"], K_CAPSLOCK: [caps_button, "", ""], K_a: [A_button, "a", "A"]
        , K_s: [S_button, "s", "S"], K_d: [D_button, "d", "D"], K_f: [F_button, "f", "F"], K_g: [G_button, "g", "G"], K_h: [H_button, "h", "H"]
        , K_j: [J_button,"j", "J"], K_k: [K_button, "k", "K"], K_l: [L_button, "l", "L"], K_SEMICOLON: [scol_button, ";", ":"]
        , K_QUOTE: [apos_button, "’", "@"], K_RETURN: [enter_button, "", ""], K_LSHIFT: [lshift_button, "", ""]
        , K_z: [Z_button, "z", "Z"], K_x: [X_button, "x", "X"], K_c: [C_button, "c", "C"], K_v: [V_button, "v", "V"]
        , K_b: [B_button, "b", "B"], K_n: [N_button, "n", "N"], K_m: [M_button, "m", "M"], K_COMMA: [com_button, ",", "<"]
        , K_PERIOD: [stop_button, ".", ">"], K_SLASH: [fslash_button, "/", "?"], K_RSHIFT: [rshift_button, "", ""]
        , K_SPACE: [space_button, " ", " "]}
