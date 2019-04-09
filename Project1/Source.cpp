#include "FaceDetection.h"
 





using namespace std;
using namespace cv;





int main()
{
	
	WebcamStream ws;
	FaceDetection face_detection;
	ws.startStream();
	while (1)
	{

		if (!ws.retrieveFrame(false))
			cout << "erreur retrieving frame !" << endl;
		Mat frame = face_detection.detect_and_Draw(ws.getFrame(), true);
		imshow("Webcam Stream", frame);
	
		char c = waitKey(10);
		if (c == 27 || c == 'e' || c == 'Q')
			break; // stop capturing by pressing ESC
		
		std::cout << "lol";
	}
}