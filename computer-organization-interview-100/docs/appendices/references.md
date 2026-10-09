# 参考资料与校准基线

本仓库保留 PDF 的参考体系，并优先使用官方架构资料校准容易被教材简化的细节。

1. **Intel® 64 and IA-32 Architectures Software Developer’s Manuals**（Intel 页面 2026-08-19 更新，当前 downloadable SDM version 092）  
   https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
2. **Intel® 64 and IA-32 Architectures Optimization Reference Manual**  
   https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html
3. **Arm Learn the Architecture - Memory Management**  
   https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/LearnTheArchitecture-MemoryManagement-101811_0100_00_en.pdf
4. **RISC-V Ratified Specifications Library**（当前 core architecture stable release v20260120）  
   https://docs.riscv.org/
5. Patterson & Hennessy, *Computer Organization and Design* / *Computer Architecture: A Quantitative Approach*（概念教材参考）
6. IEEE Std 754, *IEEE Standard for Floating-Point Arithmetic*。
7. PCI-SIG / Arm AMBA 官方规范：协议细节需以目标 revision 为准。

## 使用原则

- 教材模型用于建立因果关系，例如五级流水线、3C miss、MAR/MDR。
- ISA/系统细节以 Intel、Arm、RISC-V 官方资料为准。
- 具体 Cache 容量、latency、branch predictor、ROB 大小等属于微架构参数，不应在没有目标 CPU 手册时写死。
