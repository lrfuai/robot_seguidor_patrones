import cv
camera = cv.CreateCameraCapture(int(0))
foto = cv.QueryFrame(camera)
cv.Line(foto, (0,300), (foto.width,300), cv.RGB(255, 0, 0))
cv.SaveImage("prueba.jpg", foto)