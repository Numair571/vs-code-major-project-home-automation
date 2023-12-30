import cv2
import mediapipe as mp
import pickle
model=pickle.load(open('model.pkl','rb'))
import urllib.request as url

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

flag=0
flag1=0
flag2=0
flag5=0
flag6=0
count1=0
count2=0
count5=0
count6=0

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        data=[] 
        for point in mp_hands.HandLandmark:
            normalizedlandmark=hand_landmarks.landmark[point]
            data.append(normalizedlandmark.x)
            data.append(normalizedlandmark.y)
            data.append(normalizedlandmark.z)
        # print(len(data))
        out=model.predict([data])
        if(out[0]=='guesture1'):
          out[0]='gesture1'
          flag=1
          flag1=1
          flag2=0
          flag5=0
          flag6=0
        if(out[0]=='guesture2'):
          out[0]='gesture2'
          flag=2
          flag1=0
          flag2=1
          flag5=0
          flag6=0
        if(out[0]=='guesture3'):
          out[0]='gesture3'
        if(out[0]=='guesture6'):
          out[0]='gesture6'
          flag=6
          flag1=0
          flag2=0
          flag6=1
          flag5=0
        if(out[0]=='guesture5'):
          out[0]='gesture5'
          flag=5
          flag1=0
          flag2=0
          flag5=1
          flag6=0
        if(flag==1):
          f=open('log.txt','w')
          f.write('1')
          f.close()
          count1+=1
          count2=0
          count6=0
          count5=0
        if(flag==2):
          f=open('log.txt','w')
          f.write('2')
          f.close()
          count2+=1
          count1=0
          count6=0
          count5=0
        if(flag==6):
          f=open('log.txt','w')
          f.write('6')
          f.close()
          count6+=1
          count1=0
          count2=0
          count5=0
        if(flag==5): 
          f=open('log.txt','w')
          f.write('5')
          f.close()
          count5+=1
          count1=0
          count2=0
          count6=0

        
          
        
    # image=cv2.flip(image,1)
        
        image=cv2.putText(image,out[0],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
        



    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands',image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()