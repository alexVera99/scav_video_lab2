"""Solution for Exercise 4."""
import pathlib
import utils as ut


def video_audio_mono_2_stereo(filename_path: pathlib.Path,
                              output_filename: str = ""):
    """
    Convert mono audio from a video to stereo. Inspired from \
    https://trac.ffmpeg.org/wiki/AudioChannelManipulation.

    :param filename_path: video filename path
    :param output_filename: output filename
    :return: the filename path of the created video
    """
    if output_filename == "":
        video_name = filename_path.name.split(".")[0]
        output_filename = f"{video_name}_stereo_audio"

    output_filename_path = ut.rename_from_path(filename_path, output_filename)

    cmd = ["ffmpeg", "-y", "-i", filename_path,
           "-ac", "2",
           output_filename_path]

    _, stderr = ut.exec_in_shell_wrapper(cmd)

    ut.check_shell_stderr(stderr,
                          "Could not convert "
                          f"video audio to stereo {filename_path}")

    return output_filename_path


def video_audio_stereo_2_mono(filename_path: pathlib.Path,
                              output_filename: str = ""):
    """
    Convert stereo audio from a video to mono. Inspired from \
    https://trac.ffmpeg.org/wiki/AudioChannelManipulation.

    :param filename_path: video filename path
    :param output_filename: output filename
    :return: no return
    """
    if output_filename == "":
        video_name = filename_path.name.split(".")[0]
        output_filename = f"{video_name}_mono_audio"

    output_filename_path = ut.rename_from_path(filename_path, output_filename)

    cmd = ["ffmpeg", "-y", "-i", filename_path,
           "-ac", "1",
           output_filename_path]

    _, stderr = ut.exec_in_shell_wrapper(cmd)

    ut.check_shell_stderr(stderr,
                          "Could not convert "
                          f"video audio to stereo {filename_path}")

    return output_filename_path


def main():
    """
    Test the above functions.

    :return no return
    """
    video_filename = pathlib.Path("../data/bbb.mp4")

    filename_mono = video_audio_stereo_2_mono(video_filename)
    _ = video_audio_mono_2_stereo(filename_mono)


if __name__ == "__main__":
    main()
