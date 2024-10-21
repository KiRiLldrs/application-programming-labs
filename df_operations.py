import pandas as pd
import visual


def data_frame(filename: str, folder: str)->pd.DataFrame:
    """
    Creates a DataFrame from annotation file and adds 3 new columns: Height, Width and Number of channels
    :param filename: path to the annotation file
    :param folder: path to the folder with images
    :return: Completed DataFrame
    """
    list_of_names = ["Absolute path", "Relative path"]
    height, width, channels = visual.get_info(folder)
    df = pd.read_csv(filename, names=list_of_names)
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
    print(f"Введите максимальное значение высоты:")
    max_height = int(input())
    print(f"\nВведите максимальное значение ширины:")
    max_width = int(input())
    new_df = df[(df["Height"]<max_height) & (df["Width"]<max_width)].reset_index(drop=True)
    return new_df


def new_column(df: pd.DataFrame)->pd.DataFrame:
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
    df = df.sort_values(by="Area").reset_index(drop=True)
    return df
