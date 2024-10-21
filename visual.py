import cv2
import os

import matplotlib.pyplot as plt
import pandas as pd

def get_info(folder: str)->tuple:
    """
    Gets values for height, width and the number of channels for each picture in the folder
    :param folder: Image-folder
    :return: lists of values for height, width and the number of channels
    """
    height=[]
    width=[]
    channels=[]
    image_paths = [os.path.join(folder, f) for f in os.listdir(folder)]

    for img_folder in image_paths:
        img=cv2.imread(img_folder)
        height.append(img.shape[0])
        width.append(img.shape[1])
        channels.append(img.shape[2])

    return height, width, channels


def print_statistic(df:pd.DataFrame)->None:
    """
    Prints statistic information for columns of DataFrame, that contains information about the size of the image
    :param df: DataFrame
    """
    list_for_height =[int(df["Height"].value_counts().idxmax()), int(df["Height"].value_counts().max())]
    list_for_width = [int(df["Width"].value_counts().idxmax()), int(df["Width"].value_counts().max())]
    list_for_channels = [int(df["Number of channels"].value_counts().idxmax()), int(df["Number of channels"].value_counts().max())]
    print(f"Чаще всего встречается высота: {list_for_height[0]}, количество повторений: {list_for_height[1]}\n"
          f"Чаще всего встречается ширина: {list_for_width[0]}, количество повторений: {list_for_width[1]}\n"
          f"Чаще всего встречается глубина: {list_for_channels[0]}, количество повторений: {list_for_channels[1]} ")


def get_graph(df: pd.DataFrame)->None:
    """
    Builds a histogram and shows a graph of its changes
    :param df: DataFrame
    """
    plt.figure(figsize=(10,6))
    plt.hist(df["Area"], bins=15, color="blue", edgecolor="black" )
    plt.title("Area histogram")
    plt.xlabel("Image area")
    plt.ylabel("Frequency")
    plt.show()