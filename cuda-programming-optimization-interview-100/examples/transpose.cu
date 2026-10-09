#include <cuda_runtime.h>
constexpr int TILE = 32;
constexpr int BLOCK_ROWS = 8;

__global__ void transpose(float* out, const float* in, int width, int height) {
    __shared__ float tile[TILE][TILE + 1];
    int x = blockIdx.x * TILE + threadIdx.x;
    int y = blockIdx.y * TILE + threadIdx.y;
    #pragma unroll
    for (int j = 0; j < TILE; j += BLOCK_ROWS)
        if (x < width && y + j < height) tile[threadIdx.y + j][threadIdx.x] = in[(y + j) * width + x];
    __syncthreads();
    x = blockIdx.y * TILE + threadIdx.x;
    y = blockIdx.x * TILE + threadIdx.y;
    #pragma unroll
    for (int j = 0; j < TILE; j += BLOCK_ROWS)
        if (x < height && y + j < width) out[(y + j) * height + x] = tile[threadIdx.x][threadIdx.y + j];
}
