#include "WebcamStream.h"
using namespace cv;
 
bool WebcamStream::startStream()
{
	return _capture.open(0);
}

bool WebcamStream::retrieveFrame(bool display)
{
	
	if (!_capture.isOpened())
		return false;
	_capture >> _frame;
	if (_frame.empty()) return false; // end of video stream
	if (display)
		imshow("Webcam Stream", _frame);
	return true;
}

Mat WebcamStream::getFrame()
{
	return _frame;
}