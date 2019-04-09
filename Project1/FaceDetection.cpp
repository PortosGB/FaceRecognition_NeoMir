#include "FaceDetection.h"

using namespace std;
using namespace cv;

FaceDetection::FaceDetection()
{
	if (!_face_cascade.load(frontalface)) { printf("--(!)Error loading face cascade\n"); throw "--(!)Error loading face cascade\n"; };
	if (!_eyes_nestedCascade.load(eye_tree_eyeglasses)) { printf("--(!)Error loading eyes cascade\n"); throw "--(!)Error loading face cascade\n"; };
}

Mat FaceDetection::detect_and_Draw(Mat frame, bool display)
{
	Mat frame_gray;

	cvtColor(frame, frame_gray, COLOR_BGR2GRAY);
	equalizeHist(frame_gray, frame_gray);

	//-- Detect faces
	_face_cascade.detectMultiScale(frame_gray, _faces, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));

	for (size_t i = 0; i < _faces.size(); i++)
	{
		Point center(_faces[i].x + _faces[i].width / 2, _faces[i].y + _faces[i].height / 2);
		ellipse(frame, center, Size(_faces[i].width / 2, _faces[i].height / 2), 0, 0, 360, Scalar(0, 0, 255), 4, 8, 0);
		Mat faceROI = frame_gray(_faces[i]);
	
		//-- In each face, detect eyes
		_eyes_nestedCascade.detectMultiScale(faceROI, _eyes, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));
		for (size_t j = 0; j < _eyes.size(); j++)
		{
			Point eye_center(_faces[i].x + _eyes[j].x + _eyes[j].width / 2, _faces[i].y + _eyes[j].y + _eyes[j].height / 2);
			int radius = cvRound((_eyes[j].width + _eyes[j].height)*0.25);
			circle(frame, eye_center, radius, Scalar(255, 0, 0), 4, 8, 0);
		}
	}

	return frame;

}

bool FaceDetection::run()
{
	WebcamStream ws;

	ws.startStream();
	while (1)
	{

		if (!ws.retrieveFrame(false))
		{
			cout << "erreur retrieving frame !" << endl;
			return false;
		}
		Mat frame = detect_and_Draw(ws.getFrame(), true);
		imshow("Webcam Stream", frame);

		char c = waitKey(10);
		if (c == 27 || c == 'q' || c == 'Q')
			break; // stop capturing by pressing ESC or q

	}
	return true;
}