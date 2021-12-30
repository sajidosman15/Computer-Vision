
import cv2
import numpy as np
import mediapipe as mp

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils


# Initialize the webcam for Hand Gesture Recognition Python project
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    x , y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)

    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get hand landmark prediction
    result = hands.process(framergb)
    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []

        for handslms in result.multi_hand_landmarks:
            i = 0
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])
                # cv2.putText(frame, '{}'.format(i), (lmx+50, lmy-90), cv2.FONT_HERSHEY_SIMPLEX,
                #             1, (0, 0, 255))
                # i = i + 1

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            gesture=""

            if landmarks[20][1]>landmarks[16][1]>landmarks[12][1]>landmarks[8][1]>landmarks[4][1] \
                    and landmarks[2][1] > landmarks[3][1] > landmarks[4][1] \
                    and (landmarks[3][1]-landmarks[4][1])>25\
                    and (landmarks[6][1]-landmarks[4][1])>25:
                        if landmarks[0][0]>landmarks[6][0]:
                            if landmarks[8][0]>landmarks[6][0] and landmarks[12][0]>landmarks[10][0]\
                                    and landmarks[16][0]>landmarks[14][0] and landmarks[20][0]>landmarks[18][0]:
                                gesture = "Like"
                        else:
                            if landmarks[8][0] < landmarks[6][0] and landmarks[12][0] < landmarks[10][0] \
                                    and landmarks[16][0] < landmarks[14][0] and landmarks[20][0] < landmarks[18][0]:
                                gesture = "Like"

            elif landmarks[20][1]<landmarks[16][1]<landmarks[12][1]<landmarks[8][1]<landmarks[4][1] \
                    and landmarks[2][1] < landmarks[3][1] < landmarks[4][1] \
                    and (landmarks[4][1]-landmarks[3][1])>25\
                    and (landmarks[4][1]-landmarks[6][1])>25:
                if landmarks[0][0] > landmarks[6][0]:
                    if landmarks[8][0] > landmarks[6][0] and landmarks[12][0] > landmarks[10][0] \
                            and landmarks[16][0] > landmarks[14][0] and landmarks[20][0] > landmarks[18][0]:
                        gesture = "Dislike"
                else:
                    if landmarks[8][0] < landmarks[6][0] and landmarks[12][0] < landmarks[10][0] \
                            and landmarks[16][0] < landmarks[14][0] and landmarks[20][0] < landmarks[18][0]:
                        gesture = "Dislike"


            elif (landmarks[5][1]-landmarks[6][1])>25\
                    and (landmarks[6][1]-landmarks[7][1])>25\
                    and (landmarks[7][1]-landmarks[8][1])>25\
                    and (landmarks[9][1]-landmarks[10][1])>25\
                    and (landmarks[10][1]-landmarks[11][1])>25\
                    and (landmarks[11][1]-landmarks[12][1])>25\
                    and (landmarks[4][1] - landmarks[16][1])<30\
                    and (landmarks[16][0] - landmarks[4][0]) < 30\
                    and landmarks[20][1] > landmarks[17][1]:
                gesture = "Victory"

            elif (landmarks[7][1]-landmarks[8][1])>25\
                    and (landmarks[6][1]-landmarks[7][1])>25\
                    and (landmarks[19][1]-landmarks[20][1])>25\
                    and (landmarks[18][1]-landmarks[19][1])>25\
                    and landmarks[12][1]>landmarks[9][1]\
                    and landmarks[16][1]>landmarks[13][1]:
                        if landmarks[20][0]>landmarks[4][0]:
                            if landmarks[4][0]>landmarks[5][0]:
                                gesture = "Rock"
                        else:
                            if landmarks[4][0]<landmarks[5][0]:
                                gesture = "Rock"

            elif landmarks[6][1]>landmarks[5][1] and landmarks[4][1]>landmarks[8][1]\
                    and landmarks[10][1]>landmarks[9][1] and landmarks[4][1]>landmarks[12][1]\
                    and landmarks[14][1]>landmarks[13][1] and landmarks[4][1]>landmarks[16][1]\
                    and landmarks[18][1]>landmarks[17][1] and landmarks[4][1]>landmarks[20][1]:
                gesture = "Punch"
            elif (landmarks[19][1]-landmarks[20][1])>20\
                    and (landmarks[18][1]-landmarks[19][1])>20\
                    and (landmarks[15][1]-landmarks[16][1])>25\
                    and (landmarks[14][1]-landmarks[15][1])>25\
                    and (landmarks[11][1]-landmarks[12][1])>25\
                    and (landmarks[10][1]-landmarks[11][1])>25 \
                    and (landmarks[4][1] - landmarks[8][1])<30\
                    and (landmarks[8][0] - landmarks[4][0])<30:
                gesture = "Super"

            elif (landmarks[0][1]-landmarks[8][1])>150\
                    and landmarks[12][1]>landmarks[11][1]>landmarks[10][1]\
                    and landmarks[16][1]>landmarks[15][1]>landmarks[14][1]\
                    and landmarks[20][1]>landmarks[19][1]>landmarks[18][1]\
                    and landmarks[8][1]<landmarks[7][1]<landmarks[6][1]:
                gesture = "One"

            elif (landmarks[0][1]-landmarks[4][1])>100 and (landmarks[0][1]-landmarks[8][1])>150\
                    and (landmarks[0][1]-landmarks[12][1])>190 and (landmarks[0][1]-landmarks[16][1])>180\
                    and (landmarks[0][1]-landmarks[20][1])>150 and landmarks[4][1]<landmarks[3][1]\
                    and landmarks[8][1]<landmarks[7][1] and landmarks[12][1]<landmarks[11][1]\
                    and landmarks[16][1]<landmarks[15][1] and landmarks[20][1]<landmarks[19][1]:
                gesture = "Stop"

            cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0,0,255), 4, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()