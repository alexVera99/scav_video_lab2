"""Solution for Exercise 1."""
import pathlib
import datetime

import utils as ut


def cut_n_secs(filename_path: pathlib.Path, start: int,
               n_secs: int, output_filename: str = ""):
    """
    Cut N seconds of the video at a given starting time.

    :param filename_path: path of the video to cut
    :param start: starting time in seconds
    :param n_secs: number of seconds to cut
    :param output_filename: filename of the output video
    :return: filename path of the created video
    """
    if output_filename == "":
        img_name = filename_path.name.split(".")[0]
        output_filename = f"{img_name}_cut_{start}_{n_secs}"

    output_filename_path = ut.rename_from_path(filename_path, output_filename)

    start_sexagesimal = str(datetime.timedelta(seconds=start))
    n_sexagesimal = str(datetime.timedelta(seconds=n_secs))

    cmd = ["ffmpeg", "-y", "-i", filename_path,
           "-ss", start_sexagesimal,
           "-t", n_sexagesimal,
           output_filename_path]

    _, stderr = ut.exec_in_shell_wrapper(cmd)

    ut.check_shell_stderr(stderr, f"Could not cut the video {filename_path}")

    return output_filename_path


def main():
    """
    Test the above functions.

    :return no return
    """
    video_filename = pathlib.Path("../data/bbb.mp4")

    n_secs_cut = 10
    start_cut_points = [i * n_secs_cut for i in range(0, 3)]
    print(start_cut_points)

    for _st in start_cut_points:
        out_filename = cut_n_secs(video_filename, _st, n_secs_cut)

        print(f"Created video {out_filename}")


if __name__ == "__main__":
    main()
