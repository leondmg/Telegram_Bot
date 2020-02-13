import file_id_constants
import cv2
while True:
    '''
    # Get user supplied values
    imagePath = sys.argv[1]
    cascPath = "haarcascade_frontalface_default.xml"
    '''

    imagePath = "C:\Projects\Telegram_bot_2.0/" + file_id_constants.raw1 + ".jpg"
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))
    face = "found {0} faces!".format(len(faces))
    print(face)
