import pygame
import time
from pynput.keyboard import Key, Controller

# Initialize pygame and the joystick
pygame.init()
pygame.joystick.init()

# Initialize the keyboard controller
keyboard_controller = Controller()

# Flags to control the loop and button states
running = False
l3_pressed = False
r3_pressed = False
last_toggle_time = 0

def toggle_f10_press():
    global running, last_toggle_time
    current_time = time.time()
    if current_time - last_toggle_time > 0.5:  # Prevent rapid toggling
        running = not running
        if running:
            print("F10 pressing started. Press L3 + R3 again to stop.")
        else:
            print("F10 pressing stopped.")
        last_toggle_time = current_time

def press_f10():
    keyboard_controller.press(Key.f10)
    keyboard_controller.release(Key.f10)
    print("F10 pressed")

print("Press L3 + R3 on your Xbox One controller simultaneously to start/stop F10 pressing every 30 seconds.")

try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    print("No joystick detected. Please connect an Xbox One controller.")
    exit()

last_f10_press_time = 0

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 8:  # L3 button
                    l3_pressed = True
                elif event.button == 9:  # R3 button
                    r3_pressed = True
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 8:  # L3 button
                    l3_pressed = False
                elif event.button == 9:  # R3 button
                    r3_pressed = False
        
        # Check if both L3 and R3 are pressed
        if l3_pressed and r3_pressed:
            toggle_f10_press()
            # Wait a bit to avoid multiple toggles
            time.sleep(0.5)
        
        current_time = time.time()
        if running and current_time - last_f10_press_time >= 8:
            press_f10()
            last_f10_press_time = current_time
        
        time.sleep(0.1)  # Small sleep to prevent high CPU usage
        pygame.event.pump()  # Process event queue
except KeyboardInterrupt:
    print("\nProgram terminated.")

# Clean up
pygame.quit()
