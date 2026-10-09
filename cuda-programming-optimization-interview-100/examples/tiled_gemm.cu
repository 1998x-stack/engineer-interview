#include <cuda_runtime.h>
template<int TILE>
__global__ void gemm(const float* A, const float* B, float* C, int M, int N, int K) {
    __shared__ float As[TILE][TILE];
    __shared__ float Bs[TILE][TILE];
    int row = blockIdx.y * TILE + threadIdx.y;
    int col = blockIdx.x * TILE + threadIdx.x;
    float acc = 0.0f;
    for (int k0 = 0; k0 < K; k0 += TILE) {
        As[threadIdx.y][threadIdx.x] = (row < M && k0 + threadIdx.x < K) ? A[row*K + k0 + threadIdx.x] : 0.0f;
        Bs[threadIdx.y][threadIdx.x] = (k0 + threadIdx.y < K && col < N) ? B[(k0 + threadIdx.y)*N + col] : 0.0f;
        __syncthreads();
        #pragma unroll
        for (int k = 0; k < TILE; ++k) acc += As[threadIdx.y][k] * Bs[k][threadIdx.x];
        __syncthreads();
    }
    if (row < M && col < N) C[row*N + col] = acc;
}
