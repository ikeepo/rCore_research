# [第零章：操作系统概述](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter0/index.html)

## 引言
## 什么是操作系统
- 编译器：符号转换机器码设备；
- EDSAC 最早的OS雏形
在 1951-1954 年前后，Swinnerton-Dwyer 等在 EDSAC（Electronic Delay Storage Automatic Calculator）计算机上研制了监控程序，这也许是有记录的最早操作系统雏形；
这种类似监控程序的初级“辅助操作”过程一直持续到 20 世纪 50 年代中后期；
book: Peter H. Salus, A Quarter Century of UNIX;
## [操作系统的系统调用接口](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter0/2os-interface.html)
- API vs ABI
ABI是操作系统提供给软件系统调用接口（System Call Interface）,是二进制之间的交互接口；
API是编程语言层面的交互接口，基于编程语言自己的格式，定义的是参数、类型、返回值等函数层面的概念，因此约束的是Compiler；
不同编程语言实现的API编译成二进制之后，成为相同的ABI。
ABI描述的是对内存、寄存器、CPU等硬件资源的使用，也就是与CPU和硬件架构有关，这就必然的约束了Linker&Assembler，基于相同的ABI接口，不同编程语言编写的程序就可以正确的链接和执行。
## [操作系统抽象](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter0/3os-hw-abstract.html)
- 异常控制流
上下文恢复与保存，主要通过CPU和操作系统（手动编写在栈上保存和恢复寄存器的指令）；
- 函数转移控制流
上下文的恢复与保存，主要通过编译器（自动生成在栈上保留与恢复寄存器的指令）；
## [操作系统的特征](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter0/4os-features.html)

