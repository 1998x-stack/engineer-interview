cmake_minimum_required(VERSION 3.24)
project(cuda_interview_examples LANGUAGES CXX CUDA)
set(CMAKE_CUDA_STANDARD 17)

add_library(cuda_examples OBJECT
  grid_stride.cu
  reduction.cu
  transpose.cu
  tiled_gemm.cu
  warp_reduce.cu
  blelloch_scan.cu
  histogram_shared.cu
  stream_overlap.cu
)
