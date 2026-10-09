#include <cuda_runtime.h>

__global__ void scale(float* x, int n, float a) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) x[i] *= a;
}

// Pseudocode-like host pattern:
// 1) allocate pinned host buffers
// 2) create two or more non-blocking streams
// 3) for each chunk:
//      cudaMemcpyAsync(H2D, stream[k])
//      scale<<<..., stream[k]>>>()
//      cudaMemcpyAsync(D2H, stream[k])
// 4) use Nsight Systems to verify actual overlap.
