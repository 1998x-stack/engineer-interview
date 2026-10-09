#include <cuda_runtime.h>
#include <cstdio>

template<int BLOCK>
__global__ void reduce_sum(const float* x, float* out, int n) {
    float v = 0.0f;
    for (int i = blockIdx.x * BLOCK * 2 + threadIdx.x; i < n; i += gridDim.x * BLOCK * 2) {
        v += x[i];
        if (i + BLOCK < n) v += x[i + BLOCK];
    }
    unsigned mask = __activemask();
    for (int off = 16; off > 0; off >>= 1) v += __shfl_down_sync(mask, v, off);
    __shared__ float warp_sum[32];
    int lane = threadIdx.x & 31;
    int wid = threadIdx.x >> 5;
    if (lane == 0) warp_sum[wid] = v;
    __syncthreads();
    if (wid == 0) {
        int nw = (BLOCK + 31) / 32;
        float s = lane < nw ? warp_sum[lane] : 0.0f;
        unsigned m = __ballot_sync(0xffffffffu, lane < nw);
        for (int off = 16; off > 0; off >>= 1) s += __shfl_down_sync(m, s, off);
        if (lane == 0) atomicAdd(out, s);
    }
}
