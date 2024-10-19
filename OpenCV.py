import cv2
import numpy as np


def get_histogram(img:np.ndarray)->list:
    """
    Gets a histogram of the picture
    :param img: image whose histogram you need to find
    :return: list of image histogram for each color
    """
    hist_list = []
    for i in range(0,3):
        hist = cv2.calcHist(img,[i],None,[256],[0,256])
        hist_list.append(hist)
    return hist_list


def get_inverted_img(img:np.ndarray)->np.ndarray:
    """
    Inverts the colors of the specified image
    :param img: the image whose colors need to be inverted
    :return: image-result
    """
    return cv2.bitwise_not(img)


def save_inverted_img(img:np.ndarray, f_img:str)->None:
    """
    Saves the image-result to directory f_img
    :param img: image
    :param f_img: save-directory
    """
    cv2.imwrite(f_img,img)


