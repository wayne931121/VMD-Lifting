#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# vmdlifting.py - estimate 3D pose by "Lifting-from-the-Deep", and convert the pose data to VMD
#
# This program is derived from demo.py in Lifting-from-the-Deep which is created by Denis Tome'

from __future__ import print_function

import os

os.environ["NUMPY_EXPERIMENTAL_DTYPE_API"] = "1"

#os.environ["PATH"] += r";C:\waifu2x-caffe"
#os.environ["PATH"] += r";C:\Program Files\Ultimate Vocal Remover\torch\lib"
"""
(if you use cpu, no need to see here.)
debug:
2025-10-15 11:46:34.494588: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1616] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 5120 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 4050 Laptop GPU, pci bus id: 0000:01:00.0, compute capability: 8.9
2025-10-15 11:46:34.508761: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:354] MLIR V1 optimization pass is not enabled
2025-10-15 11:46:35.374835: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8907
2025-10-15 11:46:35.467239: W tensorflow/stream_executor/gpu/asm_compiler.cc:111] *** WARNING *** You are using ptxas 11.0.167, which is older than 11.1. ptxas before 11.1 is known to miscompile XLA code, leading to incorrect results or invalid-address errors.

You may not need to update to CUDA 11.1; cherry-picking the ptxas binary is often sufficient.
2025-10-15 11:46:35.496206: W tensorflow/stream_executor/gpu/redzone_allocator.cc:314] INTERNAL: ptxas exited with non-zero error code -1, output:
Relying on driver to perform ptx compilation.
Modify $PATH to customize ptxas location.
This message will be only logged once.
2025-10-15 11:46:36.044988: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.247123: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.383745: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.622170: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.745375: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.892642: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
2025-10-15 11:46:36.980500: E tensorflow/stream_executor/cuda/cuda_blas.cc:218] failed to create cublas handle: cublas error
"""
#set this because there is many cuda versions in my device!!!
#os.environ["PATH"] = os.environ["PATH"].replace(r"Toolkit\CUDA","icannotfindorruntodisable")
#os.environ["PATH"] += r";C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin"
#os.environ["PATH"] += r";C:\Users\原神\Downloads\cudnn-windows-x86_64-8.9.7.29_cuda11-archive\cudnn-windows-x86_64-8.9.7.29_cuda11-archive\bin"

#os.environ["TEMP"] = r"C:\ProgramData\TEST"
#os.environ["TMP"] = r"C:\ProgramData\TEST"

def usage(prog):
    print('usage: ' + prog + ' IMAGE_FILE VMD_FILE')
    sys.exit()

import __init__

from lifting import PoseEstimator
from lifting.utils import draw_limbs
from lifting.utils import plot_pose

import cv2
import matplotlib.pyplot as plt
from os.path import dirname, realpath
from pos2vmd import positions_to_frames, make_showik_frames, convert_position
from VmdWriter import VmdWriter
from refine_position import *
from adjust_center import adjust_center
from dump_positions import dump_positions
import argparse;

import pickle

vmd_file = "posfile"


def smooth_position(positions_list,smoothlevels):
    minimum_length = 3
    total_length = len(positions_list)
    if total_length < minimum_length:
        return

    joint = []
    for i in range(0, 17):
        joint.append([[], [], []])

    for pos in positions_list:
        for i in range(0, 17):
            if len(pos)+smoothlevels < i + 1:
                joint[i][0].append(None)
                joint[i][1].append(None)
                joint[i][2].append(None)
            else:
                joint[i][0].append(pos[i].x())
                joint[i][1].append(pos[i].y())
                joint[i][2].append(pos[i].z())

    for i in range(0, 17):
        for j in range(0, 3):
            interpolate(joint[i][j])
            #lowpass_filter(joint[i][j])
                                   
    for i in range(0, total_length):
        positions_list[i] = []
        for j in range(0, 17):
            p = QVector3D(joint[j][0][i], joint[j][1][i], joint[j][2][i])
            positions_list[i].append(p)
            
            
def normalize_for_vmd(positions_list):
    center_offset = QVector3D(0, 0, 0)
    spine_len = 0
    ground_y = float("inf")
    count = 0
    for pos in positions_list:
        if len(pos) < 17:
            continue
        if pos[3].y() < ground_y:
            ground_y = pos[3].y() # 右足首
        if pos[6].y() < ground_y:
            ground_y = pos[6].y() # 左足首
        center_offset += pos[7]
        spine_len = spine_len + (pos[8] - pos[7]).length()
        count += 1
    #import cdebug
    #cdebug.main(locals())
    center_offset /= count
    spine_len /= count
    scale = 3.2 / spine_len

    for pos in positions_list:
        for p in pos:
            #p -= center_offset
            p *= scale

def refine_position(positions_list,smoothlevels):
    smooth_position(positions_list,smoothlevels)
    normalize_for_vmd(positions_list)



def run(smoothlevels):

    
    with open("posfile","rb") as f:
        positions_list, visibility_list = pickle.load(f)
    
    
    bone_frames = []
    frame_num = 0
    center_enabled=False
    
    
    refine_position(positions_list,smoothlevels)
    
    for positions, visibility in zip(positions_list, visibility_list):
        if positions is None:
            frame_num += 1
            continue
        #import cdebug
        #cdebug.main(locals())
        bf = positions_to_frames(positions, visibility, frame_num, center_enabled)
        bone_frames.extend(bf)
        frame_num += 1
    
    showik_frames = make_showik_frames()
    writer = VmdWriter()
    writer.write_vmd_file(vmd_file+"smoothlevels"+str(smoothlevels)+".vmd", bone_frames, showik_frames)

l = len(list(range(-30,31,1)))

elog = 0

for smoothlevels in range(-30,31,1):
    print("\r",elog,"/",l,end="")
    try:
        run(smoothlevels)
    except Exception as e:
        print("\n","  Warn: ",smoothlevels, e)

    elog+=1

