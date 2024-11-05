import serial
import time
import keyboard  # Requires 'keyboard' library for keypress detection

arduino_port = "COM7"
baud_rate = 9600

# Establish serial communication with Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow time for connection to establish

print("Press 's' to stop the servo control.")

try:
    while True:
        # Check for user input to send stop command to Arduino
        if keyboard.is_pressed('s'):
            ser.write(b's')  # Send 's' to Arduino to stop the loop
            print("Stop command sent to Arduino.")
            break

        # Read and display the servo angle (0-180 degrees) sent from Arduino
        if ser.in_waiting > 0:
            angle = ser.readline().decode().strip()
            print(f"Servo Angle: {angle}°")

        time.sleep(0.1)  # Small delay to prevent high CPU usage

except KeyboardInterrupt:
    print("Process interrupted by user.")

finally:
    ser.close()
    print("Serial connection closed.")

