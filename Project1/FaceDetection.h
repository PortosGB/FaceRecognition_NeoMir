#pragma once

#include "WebcamStream.h"

constexpr auto eye_tree_eyeglasses = "C:/Users/Portos/Downloads/opencv/build/etc/haarcascades/haarcascade_eye_tree_eyeglasses.xml";
constexpr auto frontalface = "C:/Users/Portos/Downloads/opencv/build/etc/lbpcascades/lbpcascade_frontalface.xml";

class FaceDetection
{
	
public :

	FaceDetection();
	~FaceDetection() = default;
	FaceDetection(FaceDetection &) = delete;
	FaceDetection &operator=(FaceDetection &) = delete;

	bool run();
	cv::Mat detect_and_Draw(cv::Mat frame, bool display);

private :
	cv::CascadeClassifier _face_cascade;
	cv::CascadeClassifier _eyes_nestedCascade;
	std::vector<cv::Rect> _faces;
	std::vector<cv::Rect> _eyes;
};