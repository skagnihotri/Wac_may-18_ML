import cv2

def detect_face() :
	cam = cv2.VideoCapture(0) # to open webcam
	face_clf = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

	while True:
		ret, frame = cam.read()

		if ret == False:
			continue

		faces = face_clf.detectMultiScale(frame, 1.3, 5) #frame , scalling , neigb

		for x,y,w,h in faces :
			cv2.putText(frame, "Person", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), cv2.LINE_AA)	
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

		cv2.imshow("FACES", frame) # display

		key = cv2.waitKey(1) & 0xff

		if key == ord('q'):
			cam.release()
			break

if __name__ == '__main__':
	detect_face()
	cv2.destroyAllWindows()