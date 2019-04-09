#pragma once
#include<opencv2/opencv.hpp>
#include<iostream>
#include <opencv2/objdetect.hpp> 
#include <opencv2/highgui.hpp> 
#include <opencv2/imgproc.hpp> 
#include <vector>
#include <thread>
#include <mutex>

extern std::mutex lok;

class WebcamStream
{
public :
	WebcamStream() {}
	~WebcamStream() {}
	bool startStream();
	bool retrieveFrame(bool display);

	cv::Mat getFrame();

private:
	cv::VideoCapture _capture;
	cv::Mat _frame;

};