#include <cuda_runtime.h>

// Educational example for a small number of bins.
template<int BINS>
__global__ void histogram_shared(const unsigned char* x, int n, unsigned int* hist) {
    __shared__ unsigned int local[BINS];
    for (int b = threadIdx.x; b < BINS; b += blockDim.x) local[b] = 0;
    __syncthreads();

    for (int i = blockIdx.x * blockDim.x + threadIdx.x; i < n; i += blockDim.x * gridDim.x)
        atomicAdd(&local[x[i]], 1u);
    __syncthreads();

    for (int b = threadIdx.x; b < BINS; b += blockDim.x)
        atomicAdd(&hist[b], local[b]);
}
