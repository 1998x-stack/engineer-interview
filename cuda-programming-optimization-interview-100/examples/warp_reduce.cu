#include <cuda_runtime.h>

__device__ float warp_reduce_sum(float x, unsigned mask) {
    for (int offset = warpSize / 2; offset > 0; offset >>= 1)
        x += __shfl_down_sync(mask, x, offset);
    return x;
}
