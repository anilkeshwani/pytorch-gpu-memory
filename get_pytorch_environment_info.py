import platform
import subprocess
import sys

import numpy as np
import torch


# PyTorch info
print(f"PyTorch version: {torch.__version__}")
print(f"Is debug build: {torch.version.debug}")
print(f"CUDA used to build PyTorch: {torch.version.cuda}")

# OS info
print(f"\nOS: {platform.platform()}")

# GCC version (Unix-like systems)
try:
    gcc_version = subprocess.check_output(["gcc", "--version"]).decode().split("\n")[0]
    print(f"GCC version: {gcc_version}")
except:
    print("GCC version: Not available")

# CMake version (if installed)
try:
    cmake_version = subprocess.check_output(["cmake", "--version"]).decode().split("\n")[0]
    print(f"CMake version: {cmake_version}")
except:
    print("CMake version: Not available")

# Python version
print(f"\nPython version: {sys.version.split()[0]}")

# CUDA availability
print(f"Is CUDA available: {torch.cuda.is_available()}")
print(f"CUDA runtime version: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}")

# GPU info
if torch.cuda.is_available():
    print("GPU models and configuration:")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_properties(i)}")
else:
    print("No GPUs detected")

# Nvidia driver version (Unix-like systems)
try:
    driver_version = (
        subprocess.check_output(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"]).decode().strip()
    )
    print(f"Nvidia driver version: {driver_version}")
except:
    print("Nvidia driver version: Not available")

# cuDNN version (if available)
try:
    cudnn_version = torch.backends.cudnn.version()
    print(f"cuDNN version: {cudnn_version}")
except:
    print("cuDNN version: Not available")

# Other libraries
print(f"\nVersions of relevant libraries:")
print(f"numpy ({np.__version__})")
