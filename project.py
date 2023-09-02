import cv2 as cv

print(''' \n
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')

print("Welcome to Real Time Color Grading System for Webcam...\n")

loop = "y"

while (loop == "y"):
    print("1. Grayscale Mode")
    print("2. HSV Mode")
    print("3. LAB Mode")
    print("4. Inversion Mode")

    print("\n🚩 Note: Press 'q' for exiting from webcam 🚩")

    op = int(input("\nOption Number: "))

    capture = cv.VideoCapture(0)

    if(op == 1):
        # BGR to Grayscale
        while True:
            isTrue, frame = capture.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow("LIVE - GRAYSCALE", frame)
            if (cv.waitKey(20) & 0xFF == ord('q')):
                break
        capture.release()
        cv.destroyAllWindows()

    elif (op == 2):
        # BGR to HSV
        while True:
            isTrue, frame = capture.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            cv.imshow("LIVE - HSV", frame)
            if (cv.waitKey(20) & 0xFF == ord('q')):
                break
        capture.release()
        cv.destroyAllWindows()

    elif (op == 3):
        # BGR to LAB or L*a*b
        while True:
            isTrue, frame = capture.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
            cv.imshow("LIVE - LAB", frame)
            if (cv.waitKey(20) & 0xFF == ord('q')):
                break
        capture.release()
        cv.destroyAllWindows()

    elif (op == 4):
        # BGR to RGB (Inversion)
        while True:
            isTrue, frame = capture.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            cv.imshow("LIVE - INVERSION", frame)
            if (cv.waitKey(20) & 0xFF == ord('q')):
                break
        capture.release()
        cv.destroyAllWindows()

    else:
        print("❌ Invalid Input ❌\n")

    loop = str(input("Do you want to use the Program again? (y / n) : "))
    if (loop == "y"):
        print("\n------------------------------------------------------------------------------------------------------------------------------------\n")

print("\n ✨ Thanks for using the Program!!! ✨")
