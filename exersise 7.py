import time
import datetime
from pygame import mixer
with open('Programer health.txt','a') as file:

    program_input = int(input('Enter 1 to start the program or 2 to retreave privious data: '))
    if program_input is 1:
        user_name = input('Enter your name : ')
        user_input = input("Enter 'Hy' to start the program :" )
        if user_input == 'Hy':
            print(f'Hy {user_name} welcome to the office')
            water = 240
            eye  = 180
            exersie = 270
            in_water = time.time()
            in_eye = time.time()
            in_ex = time.time()


            while True:
                if time.time()-in_water > water:
                    water_mp3 = 'C:\Eknath folder\program for python\water.mp3'
                    mixer.init()
                    mixer.music.load(water_mp3)
                    mixer.music.play()
                    user_input1 = input('Drink water and Enter Drank to stop audio:')

                    if user_input1 == 'Drank':
                        mixer.music.stop()
                        file.write(f'{datetime.datetime.now()} {user_name} Drank water\n')
                        in_water= time.time()


                if time.time()-in_eye > eye:
                    eye_mp3 = 'C:\Eknath folder\program for python\eyes.mp3'
                    mixer.init()
                    mixer.music.load(eye_mp3)
                    mixer.music.play()
                    user_input2 = input('Do any eye exercise and type EyDone to stop audio:')
                    if user_input2 == 'eydone':
                        mixer.music.stop()
                        file.write(f'{datetime.datetime.now()} {user_name} Did eye Exercise\n')
                        in_eye= time.time()


                if time.time()-in_ex > exersie:
                    Exercise_mp3 = 'C:\Eknath folder\program for python\exersise.mp3'
                    mixer.init()
                    mixer.music.load(Exercise_mp3)
                    mixer.music.play()
                    user_input2 = input('Do any  exercise and type ExDone to stop audio:')

                    if user_input2 == 'exdone':
                        mixer.music.stop()
                        file.write(f'{datetime.datetime.now()} {user_name} Did Exercise\n')
                        in_ex = time.time()

    else:
        with open('Programer health.txt') as file:
            print(file.read())
    user_exit_input = input('Enter Bey to Exit the program :')
    if user_exit_input is "Bey":
        print(f'Good by {user_name} see you leter')

# Harry bhai ka program

#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio
#
# from pygame import mixer
# from datetime import datetime
# from time import time
#
# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break
#
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")
#
# if __name__ == '__main__':
#     # musiconloop("water.mp3", "stop")
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     watersecs = 40*60
#     exsecs = 30*60
#     eyessecs = 45*60
#
#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking time. Enter 'drank' to stop the alarm.")
#             musiconloop('water.mp3', 'drank')
#             init_water = time()
#             log_now("Drank Water at")
#
#         if time() - init_eyes >eyessecs:
#             print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
#             musiconloop('eyes.mp3', 'doneeyes')
#             init_eyes = time()
#             log_now("Eyes Relaxed at")
#
#         if time() - init_exercise > exsecs:
#             print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
#             musiconloop('physical.mp3', 'donephy')
#             init_exercise = time()
#             log_now("Physical Activity done at")
#
#
#
#
