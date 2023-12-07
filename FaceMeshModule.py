import cv2
import mediapipe as mp
import time

class FaceMeshDetect():

    def __init__(self, staticMode = False, maxFaces= 2, minDetectionCon= 0.5, minTrackCon= 0.5):
        self.staticMode= staticMode
        self.maxFaces= maxFaces
        self.minDetectionCon= minDetectionCon
        self.minTrackCon= minTrackCon


        # help us draw on our faces
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        #self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,self.minDetectionCon, self.minTrackCon)
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode= self.staticMode,
            max_num_faces = self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minDetectionCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh (self, img, draw= True):
        # accepts only RGB image, so we have to convert it
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,
                                               self.drawSpec, self.drawSpec)
                face = []
                # in oder to go further deep and find out all the different points
                # for lm in faceLms.landmark:
                for id, lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN,
                                1, (0, 255, 0), 1)
                    # print(x, y)
                    print(id, x, y)
                    face.append([x,y])
                faces.append(face)
        return img, faces
#

def main():
    #cap = cv2.VideoCapture("video/1.mp4")
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceMeshDetect()
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img) #(img, False)
        #if len(faces)!= 0:
         #   print(len(faces))
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
