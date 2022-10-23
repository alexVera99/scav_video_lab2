import exercise_1 as ex_1
import exercise_2 as ex_2
import exercise_3 as ex_3
import exercise_1 as ex_4


def exercise_1_option():
    """
    Execute logic for exercise 1

    :return: no return
    """
    video_filename = input("Video filename (it must be a valid relative"
                           " or absolute valid path): ")

    start_cut = input("Second number to start cut: ")
    n_secs_cut = input("Number of seconds of the resulting video: ")

    ex_1.cut_n_secs(video_filename, _st, n_secs_cut)

def main():
    """

    :return:
    """
    N = 4
    options = [i for i in range(1, N + 1)]

    while True:
        option = input("Select the exercise: \n"
                   "1) Exercise 1\n"
                   "2) Exercise 2\n"
                   "3) Exercise 3\n"
                   "4) Exercise 4\n")

        if option in options:
            print(f"You have selected option {option}")
            break






if __name__ == "__main__":
    main()
