# PyTorch GPU Memory Profiling & Debugging

- **scripts/**: Memory profiling scripts. These are minimal examples using ResNet50 as a model for demonstration purposes.
    - **memorysnapshot.py**: Visualisation of memory usage over time via a stack trace.
    - **convert_snapshot.sh**: Executable to convert the snapshot produced with _torch/cuda/_memory_viz.py_ (as shown below but without having to manually specify your torch install path)
    - **memoryprofile.py**: Running profiling gives visualisation of memory usage aggregated by usage type, i.e. classified into optimizer, activations, parameters, backwards pass (autograd-related)
- **get_pytorch_environment_info.py**: snippet prints out relevant information about the user's environment including PyTorch, Python and CUDA (Toolkit/Runtime) versions, the NVIDIA CUDA Deep Neural Network library (cuDNN) version and more. 
    - It is [available as a Gist](https://gist.github.com/anilkeshwani/ada329b193d2c097e1f6efadad5ace04).

Manual conversion of memory snapshot:

```sh
python torch/cuda/_memory_viz.py trace_plot snapshot.pickle -o snapshot.html
```

---

Code Source: [Understanding GPU Memory 1: Visualizing All Allocations over Time](https://pytorch.org/blog/understanding-gpu-memory-1/) (December 14, 2023) by Aaron Shi, Zachary DeVito
