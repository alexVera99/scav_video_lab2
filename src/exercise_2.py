"""Solution for Exercise 2."""
import pathlib
import exercise_3 as ex_3
import utils as ut


def create_video_with_yuv_histogram(filename_path: pathlib.Path,
                                    output_filename: str = ""):
    """
    Create a video with the YUV histogram overlaid. \
    Inspired from\
    https://trac.ffmpeg.org/wiki/Histogram.

    :param filename_path: video filename path
    :param output_filename: output filename
    :return: video created filename
    """
    if output_filename == "":
        video_name = filename_path.name.split(".")[0]
        output_filename = f"{video_name}_with_hist"

    output_filename_path = ut.rename_from_path(filename_path, output_filename)

    # Computing histogram size
    w_video, h_video = ex_3.get_video_dims(filename_path)
    w_hist = w_video // 4
    h_hist = h_video // 2

    cmd = ["ffmpeg", "-y", "-i", filename_path,
           "-vf",
           f"split=2[a][b],"
           f"[b]histogram,format=yuva444p,scale={w_hist}:{h_hist}[hh],"
           f"[a][hh]overlay",
           output_filename_path]

    _, stderr = ut.exec_in_shell_wrapper(cmd)

    ut.check_shell_stderr(stderr,
                          f"Could not get the YUV histogram {filename_path}")

    return output_filename_path


def main():
    """
    Test the above functions.

    :return no return
    """
    video_filename = pathlib.Path("../data/bbb.mp4")

    out_filename = create_video_with_yuv_histogram(video_filename)

    print(f"Video created in {out_filename}")


if __name__ == "__main__":
    main()
