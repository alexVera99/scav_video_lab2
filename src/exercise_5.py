import pathlib

import exercise_1 as ex_1
import exercise_2 as ex_2
import exercise_3 as ex_3
import exercise_4 as ex_4


def execute_exercise_1_option():
    """
    Execute logic for exercise 1.

    :return: no return
    """
    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    start_cut = int(input("Second number to start cut: "))
    n_secs_cut = int(input("Number of seconds of the resulting video: "))

    out_filename = ex_1.cut_n_secs(video_filename, start_cut, n_secs_cut)

    print(f"Video created in {out_filename}")


def execute_exercise_2_option():
    """
    Execute logic for exercise 2.

    :return: no return
    """
    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    out_filename = ex_2.create_video_with_yuv_histogram(video_filename)

    print(f"Video created in {out_filename}")


def execute_exercise_3_option():
    """
    Execute logic for exercise 3.

    :return:
    """
    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    target_width = int(input("Target width (must be multiple of 2 or "
                             "-1 to create automatically based on the "
                             "other dimension):\n"))

    target_height = int(input("Target height (must be multiple of 2 or "
                              "-1 to create automatically based on the "
                              "other dimension):\n"))

    out_filename = ex_3.resize_video(video_filename,
                                     target_width,
                                     target_height)

    print(f"Video created in {out_filename}")


def execute_exercise_4_option():
    """
    Execute logic for exercise 4

    :return: no return
    """
    options = ["m", "s"]

    while True:
        option = input("Output audio of the video to (M)ono or (S)tereo?\n")
        option = option.lower()
        if option.lower() in options:
            print("\nError: Please select (M) for mono or (S) for stereo.")
            continue

    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    if option == "m":
        out_filename = ex_4.video_audio_stereo_2_mono(video_filename)

    elif option == "s":
        out_filename = ex_4.video_audio_mono_2_stereo(video_filename)

    print(f"Video created in {out_filename}")


def main():
    """

    :return:
    """
    N = 4
    options = [i for i in range(1, N + 1)]

    while True:
        option = int(input("Select the exercise: \n"
                           "1) Exercise 1\n"
                           "2) Exercise 2\n"
                           "3) Exercise 3\n"
                           "4) Exercise 4\n"))

        if option in options:
            print(f"\nYou have selected option {option}")
            continue

        print("Please, provide a valid option")
    if option == 1:
        execute_exercise_1_option()
    if option == 2:
        execute_exercise_2_option()
    if option == 3:
        execute_exercise_3_option()
    if option == 4:
        execute_exercise_4_option()


if __name__ == "__main__":
    main()
