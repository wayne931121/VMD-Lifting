import os

os.environ["NUMPY_EXPERIMENTAL_DTYPE_API"] = "1"

#os.environ["PATH"] += r";C:\waifu2x-caffe"
#os.environ["PATH"] += r";C:\Program Files\Ultimate Vocal Remover\torch\lib"
"""
(if you use cpu, no need to see here.)
debug:

!!!!!!!!!!!!!!!!! ptxas error recored by wayne931121: not use correct path


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


print("Environment Setup")
