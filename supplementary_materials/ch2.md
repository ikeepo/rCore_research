# [第二章：批处理系统](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/0intro.html)
- 特权级 Priviledge
保护计算机系统不受应用程序破坏的机制被称为特权级机制。
实现运行态的分离，应用程序运行在用户态，操作系统运行在内核态，并且两个运行态隔离，这需要软硬件共同努力。
## [特权级机制](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/1rv-privilege.html)
特权级是通过软硬件共同作用，处理器设置两个不同安全等级的执行环境。
ecall(EnvironmentCall): 具有用户态到内核态的执行环境切换能力的函数调用指令；
- 异常控制流ECF ExceptionControlFlow(异常Exception)
常规控制流：顺序、循环、分支、函数调用；
特权级之间也需要环境切换，类似函数调用的环境切换；
从用户态到内核态的异常原因有两种：
1. 为了获取内核服务而执行特殊指令（breakpoint，ecall称为陷入trap）
2. 执行了不运行的指令而出错
- RISC-V异常一览表疑问
1. interrupt为0表示什么？
手册3.1.15 Machine Cause Register(mcause) 的数值，interrupt是mcause寄存器首位指示是中断还是异常。
2. ExceptionCode 11, ecall from M-mode
M态下用ecall是为了方便，此时还需要M态自己处理，US态下的ecall一定是M层处理。
- [RISC-V的特权指令](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/1rv-privilege.html#term-csr-instr)
每个特权级有自己特有的指令和控制状态寄存器CSR, Control and Status Register;
## [实现应用程序](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/2application.html)
- [系统调用](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/2application.html#term-call-syscall)
```
fn sys_exit(exit_code: usize) -> !;
```
返回类型!(never type)表示永远不会返回。
不返回指的是执行某种程序中止操作，退出程序或者panic。
系统调用，实际上是汇编指令级的二进制接口。
- 寄存器编号与别名
a0-a6保存系统调用参数，a0保存系统调用的返回值。
a7用来传递syscall ID,所有的syscall都是通过ecall指令触发，因此除了常规的输入参数之外，还需要额外一个寄存器来保存要请求哪个系统调用。
- [编译生成应用程序二进制码](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/2application.html#id8)
## [实现批处理操作系统](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/3batch-system.html)
## [实现特权级的切换](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/4trap-handling.html)
- [特权级切换相关的控制状态寄存器](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter2/4trap-handling.html#id4)
