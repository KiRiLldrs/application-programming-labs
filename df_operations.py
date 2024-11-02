import pandas as pd

import visual


def data_frame(filename: str)->pd.DataFrame:
    """
    Creates a DataFrame from annotation file and adds 3 new columns: Height, Width and Number of channels
    :param filename: path to the annotation file
    :return: Completed DataFrame
    """
    list_of_names = ["Absolute_path", "Relative_path"]
    df = pd.read_csv(filename, names=list_of_names)
    return df

def new_columns(df:pd.DataFrame, folder: str):
    """
    Adds new columns to the DataFrame
    :param df: original DataFrame
    :param folder: folder with the images
    :return: DataFrame with new columns
    """
    height, width, channels = visual.get_info(folder)
    df["Height"] = height
    df["Width"] = width
    df["Number of channels"] = channels
    return df


def new_data_frame(df: pd.DataFrame)->pd.DataFrame:
    """
    Creates a new DataFrame in which height<max_height and width<max_width
    max_height and max_width are selected by the user
    :param df: Original DataFrame
    :return: New DataFrame in which the conditions height<max_height and width<max_width are met
    """
    params = print_request()
    new_df = df.copy(deep=True)[(df["Height"]<params[0]) & (df["Width"]<params[1])].reset_index(drop=True)
    return new_df

def print_request()->list:
    """
    Requests max height and max width
    :return: returns list of parameters
    """
    print(f"Введите максимальное значение высоты:")
    max_height = int(input())
    print(f"\nВведите максимальное значение ширины:")
    max_width = int(input())
    list_of_params = [max_height, max_width]
    return list_of_params



def add_area(df: pd.DataFrame)->pd.DataFrame:
    """
    Creates a new column to DataFrame that represents area of the picture
    :param df: DataFrame
    :return: Converted DataFrame
    """
    df["Area"] = df["Height"] * df["Width"]
    return df


def sorted_data_frame(df: pd.DataFrame)->pd.DataFrame:
    """
    Sorts the DataFrame by column "Area" from the smallest to the largest value
    :param df: DataFrame
    :return: Converted DataFrame
    """
    final_frame = df.copy(deep=True).sort_values(by="Area").reset_index(drop=True)
    return final_frame
