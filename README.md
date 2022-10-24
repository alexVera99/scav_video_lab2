# Description
Here you can find the solution for Lab 2 exercises from Audio and Video 
encoding systems.

Also, in exercise 5, you can find an application
to execute any of the other exercises using your
own configurations.

# Known issues
This is a list of known issues:
* In exercise 3, if we convert bbb.mp4 with dimensions
640x360 to `target width = 200` and `target height = -1`,
which means automatically computing target height. It outputs
a video with dimensions 199x112. The target height is correct
but the target width is not.