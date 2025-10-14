# VMD-Lifting

official: https://github.com/DenisTome/Lifting-from-the-Deep-release

# wayne9311211/VMD-Lifting

forked from: https://github.com/errno-mmd/VMD-Lifting

# Intro

I installed, debug, successful run these files in only 3 hours. It is very good.

# Download Model by Yourself

https://github.com/wayne931121/VMD-Lifting/tree/master/data/saved_sessions

# MY ENV

https://github.com/wayne931121/VMD-Lifting/blob/master/env.yml

## Key Points

- python and pip version (or you may install or build package failed)
- tensorflow and some other relation packages version
- matplotlib version
- numpy version

# MY DEVICE INFO

 - Windows 11
 - Miniforge Conda
 - CUDA 12.1 device with cudnn (installed and setted up env path)
 - NVIDIA GeForce RTX 4050 (6GB, installed driver)

# Example
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3f46123b-acea-423b-ad5c-208d4a42571c" />

# Notice

## If you use cpu, that's good.

## If you use GPU, 

### set the memoey limit here:

https://github.com/wayne931121/VMD-Lifting/blob/master/packages/lifting/_pose_estimator.py#L19

### check your tmp folder is all in ansi code (or tensorflow may give you a error)

If not, set here:

https://github.com/wayne931121/VMD-Lifting/blob/master/applications/vmdlifting.py#L19

# Reference
https://www.tensorflow.org/guide/migrate#a_note_on_slim_contriblayers

https://stackoverflow.com/questions/56561734/runtimeerror-tf-placeholder-is-not-compatible-with-eager-execution

https://stackoverflow.com/questions/10475198/retrieving-the-current-frame-number-in-opencv

https://stackoverflow.com/questions/2435062/what-happened-to-the-tmp-environment-variable

https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow

# Notice

https://stackoverflow.com/questions/78266102/opencv-throws-error-215assertion-failed/79790464#79790464
