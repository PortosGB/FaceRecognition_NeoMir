#pragma once
#include<opencv2/opencv.hpp>
#include<iostream>
#include <opencv2/objdetect.hpp> 
#include <opencv2/highgui.hpp> 
#include <opencv2/imgproc.hpp> 
#include <vector>


class WebcamStream
{
public :
	WebcamStream() = default;
	~WebcamStream() = default;
	bool startStream();
	bool retrieveFrame(bool display);

	cv::Mat getFrame();

private:
	cv::VideoCapture _capture;
	cv::Mat _frame;

};