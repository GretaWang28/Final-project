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
        self.mpDraw = self.mp.solutions.drawing_utils
        self.mpFaceMesh = self.mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
                                                 self.minDetectionCon, self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh (self, img, draw= True)


#     # accepts only RGB image, so we have to convert it
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = faceMesh.process(imgRGB)
#     if results.multi_face_landmarks:
#         for faceLms in results.multi_face_landmarks:
#             mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,
#                                   drawSpec, drawSpec)
#             # in oder to go further deep and find out all the different points
#             # for lm in faceLms.landmark:
#             for id, lm in enumerate(faceLms.landmark):
#                 # print(lm)
#                 ih, iw, ic = img.shape
#                 x, y = int(lm.x * iw), int(lm.y * ih)
#                 # print(x, y)
#                 print(id, x, y)
#



def main():
    cap = cv2.VideoCapture("video/1.mp4")
    pTime = 0
    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
