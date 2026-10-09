#include <cuda_runtime.h>

// Educational single-block exclusive scan. BLOCK must be a power of two.
template<int BLOCK>
__global__ void exclusive_scan_block(const float* in, float* out, int n) {
    __shared__ float s[BLOCK];
    int t = threadIdx.x;
    int i = blockIdx.x * BLOCK + t;
    s[t] = (i < n) ? in[i] : 0.0f;
    __syncthreads();

    for (int offset = 1; offset < BLOCK; offset <<= 1) {
        int idx = (t + 1) * offset * 2 - 1;
        if (idx < BLOCK) s[idx] += s[idx - offset];
        __syncthreads();
    }

    if (t == 0) s[BLOCK - 1] = 0.0f;
    __syncthreads();

    for (int offset = BLOCK >> 1; offset > 0; offset >>= 1) {
        int idx = (t + 1) * offset * 2 - 1;
        if (idx < BLOCK) {
            float tmp = s[idx - offset];
            s[idx - offset] = s[idx];
            s[idx] += tmp;
        }
        __syncthreads();
    }

    if (i < n) out[i] = s[t];
}
