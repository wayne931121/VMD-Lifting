
See: https://www.tensorflow.org/install/pip

Wayne931121:

tensorflow==2.10.0

The following NVIDIA® software are only required for GPU support.

- NVIDIA® GPU drivers
- CUDA® Toolkit 11.2.
- cuDNN SDK 8.

Download from:

https://www.nvidia.com/en-us/drivers/

https://developer.nvidia.com/cuda-11.2.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

https://developer.nvidia.com/rdp/cudnn-archive

My GPU Info
```
(C:\ai1) C:\TEST\VMD-Lifting-master\VMD-Lifting-master\applications>python vmdlifting.py "C:\TEST\testv\4.mp4" 4.vmd
2025-10-15 11:56:30.282717: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2025-10-15 11:56:30.700008: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1616] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6144 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 4050 Laptop GPU, pci bus id: 0000:01:00.0, compute capability: 8.9
1 Physical GPUs, 1 Logical GPUs
pose estimation start
C:\ai1\lib\site-packages\tensorflow\python\keras\engine\base_layer_v1.py:1694: UserWarning: `layer.apply` is deprecated and will be removed in a future version. Please use `layer.__call__` method instead.
  warnings.warn('`layer.apply` is deprecated and '
2025-10-15 11:56:31.969289: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1616] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6144 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 4050 Laptop GPU, pci bus id: 0000:01:00.0, compute capability: 8.9
2025-10-15 11:56:31.986615: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:354] MLIR V1 optimization pass is not enabled
2025-10-15 11:56:34.624213: I tensorflow/stream_executor/cuda/cuda_dnn.cc:384] Loaded cuDNN version 8907
2025-10-15 11:56:35.113439: W tensorflow/stream_executor/gpu/redzone_allocator.cc:314] INTERNAL: ptxas exited with non-zero error code -1, output:
Relying on driver to perform ptx compilation.
Modify $PATH to customize ptxas location.
This message will be only logged once.
2025-10-15 11:56:35.864590: I tensorflow/stream_executor/cuda/cuda_blas.cc:1614] TensorFloat-32 will be used for the matrix multiplication. This will only be logged once.
2025-10-15 11:56:38.483048: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.483389: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.483667: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.483911: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.484208: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.485684: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.486440: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.486631: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.486752: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.486828: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.486969: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.487101: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
2025-10-15 11:56:38.516540: W tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc:189] Failed to compile generated PTX with ptxas. Falling back to compilation by driver.
 1642 / 1642
(C:\ai1) C:\TEST\VMD-Lifting-master\VMD-Lifting-master\applications>nvidia-smi
Wed Oct 15 12:15:11 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 566.14                 Driver Version: 566.14         CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4050 ...  WDDM  |   00000000:01:00.0 Off |                  N/A |
| N/A   46C    P0             16W /   85W |       0MiB /   6141MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

(C:\ai1) C:\TEST\VMD-Lifting-master\VMD-Lifting-master\applications>
```

Set path in:

https://github.com/wayne931121/VMD-Lifting/blob/master/applications/vmdlifting.py#L39
