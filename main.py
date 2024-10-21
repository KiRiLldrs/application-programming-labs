import argparse

import df_operations
import visual


def create_parser()->tuple:
    """
    Gets a path to annotation file and to a folder with images
    :return: Tuple of two string
    """
    parser=argparse.ArgumentParser()
    parser.add_argument("csv_file",type=str,help="the name of annotation file")
    parser.add_argument("image_folder", type=str,help="the name of the image_folder")
    args=parser.parse_args()
    return args.csv_file, args.image_folder


def main():
    ann, folder = create_parser()
    df=df_operations.data_frame(ann,folder)

    print(df)
    visual.print_statistic(df)

    new_frame = df_operations.new_data_frame(df)
    print(new_frame)

    new_frame = df_operations.new_column(new_frame)
    print(new_frame)

    final_frame = df_operations.sorted_data_frame(new_frame)
    print(final_frame)

    visual.get_graph(df_operations.sorted_data_frame(df_operations.new_column(new_frame)))


if __name__ == "__main__":
    main()