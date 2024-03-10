import cv2
import qrcode
import sys
import webbrowser
from pyzbar.pyzbar import decode




print("Welcome to the QRcode utility!\n")
print("Action :\n(1) Read from file.\n(2) Read from Camera.\n(3) Make a QRcode.\n")
user_input = input("> ")

def makeQRCode(data, file_name) :
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)

    img = qrcode.make(data)
    img.save(file_name)

    #display
    img = cv2.imread(file_name, cv2.IMREAD_ANYCOLOR)

    while True:
        cv2.imshow(file_name, img)
        cv2.waitKey(5000)
        sys.exit()
        break

    cv2.destroyAllWindows()
    return

def ReadQRWebcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        qr_codes = decode(gray)

        for qr_code in qr_codes:
            (x, y, w, h) = qr_code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            qr_data = qr_code.data.decode('utf-8')
            qr_type = qr_code.type

            cv2.putText(frame, f"{qr_type}: {qr_data}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            print(f"QR Code Type: {qr_type}, Data: {qr_data}")

            cv2.imshow('QR Code Reader', frame)
            
            cv2.waitKey(2000)

            cap.release()
            cv2.destroyAllWindows()
            
            return

        cv2.imshow('QR Code Reader', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def ReadQRimg(file_name) :
    img = cv2.imread(file_name)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    if bbox is not None:
        print(f"QRCode data:\n{data}")



if user_input == "1" :
    file_name = input("What's the file name ?\n> ")
    ReadQRimg(file_name)

elif user_input == "2" :
    ReadQRWebcam()

elif user_input == "3" :
    file_name = input("What's the output file name ?\n> ")
    data = input("Data?\n> ")
    makeQRCode(data, file_name)

else :
    print("Invalid input !")
