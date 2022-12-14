"""Exercise 5: It is an application merging the behaviour of all the\
other exercises."""
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
    preset_resolutions = {1: ["720p", [1280, 720]],
                          2: ["480p", [640, 480]],
                          3: ["360x240", [360, 240]],
                          4: ["160x120", [160, 120]]}

    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    use_presets = input("Do you wan to use presets? (Y) or (N): ")

    if use_presets.lower() == "y":
        for key, value in preset_resolutions.items():
            print(f"{key}) {value[0]}")

        while True:
            preset_option = int(input("Select option: "))
            if preset_option in list(preset_resolutions.keys()):
                break
        preset = preset_resolutions[preset_option]
        target_width = preset[1][0]
        target_height = preset[1][1]

    else:
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
    Execute logic for exercise 4.

    :return: no return
    """
    options = ["m", "s"]

    while True:
        option = input("Output audio of the video to (M)ono or (S)tereo?\n")
        option = option.lower()

        if option in options:
            print(f"\nYou have selected option {option}\n")
            break

        print("\nError: Please select (M) for mono or (S) for stereo.")

    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")
    video_filename = pathlib.Path(video_filename)

    if option == options[0]:
        out_filename = ex_4.video_audio_stereo_2_mono(video_filename)

    elif option == options[1]:
        out_filename = ex_4.video_audio_mono_2_stereo(video_filename)

    print(f"Video created in {out_filename}")


def main():
    """
    Execute the logic of the main menu to select which exercise you \
    want to use.

    :return: no return
    """
    n_options = 4
    options = list(range(1, n_options + 1))

    while True:
        option = int(input("Select the exercise: \n"
                           "1) Exercise 1: Trim a video.\n"
                           "2) Exercise 2: Overlay YUV histogram in video.\n"
                           "3) Exercise 3: Resize a video.\n"
                           "4) Exercise 4: Change audio of a video"
                           "from stereo to mono, and vice versa.\n"))

        if option in options:
            print(f"\nYou have selected option {option}\n")
            break

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
