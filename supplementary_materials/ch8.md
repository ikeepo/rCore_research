# [第八章：并发](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/0intro.html)
并发是通过OS不断地切换进程来达到的。
线程Thread的出现是为了提高整个系统的并行/并发执行效率。
线程=ID+执行状态+当前指令指针PC+寄存器集合+栈；
线程作为一个基本单位可以被用户态或OS态调度；
- 同步互斥
因为线程间共享进程的内存，因此需要同步互斥机制。
临界区critical section：访问共享资源的一段代码；
同步synchronization：多个并发执行的进程在一些关键点上需要互相等待，这种相互制约的等待称为同步；
条件变量Conditional Variable: 允许一个线程在另一个线程完成某些操作之前等待；
信号量Semaphore：用于在多个线程或进程之间贡献资源时进行互斥访问；
## [用户态的线程管理](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/1thread.html)
## [内核态的线程管理](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/1thread-kernel.html)
进程的主要目的是隔离，线程是共享，也就是同步。
## [互斥锁](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/2lock.html)
锁是用来锁资源的，资源被锁之后，只有拿到锁的线程才可以进入临界区；
## [信号量机制](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/3semaphore.html)
信号量比互斥锁更灵活的同步互斥机制；
信号量描述的同步需求：初始状态下，某种资源的可用数量为一个非负整数N；
信号量支持两种操作：
1. P尝试，占用一个资源
2. V增加，归还一个资源
当N=1时称为二值信号量Binary Semaphore，等价于互斥锁；
## [条件变量机制](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/4condition-variable.html)
## [并发中的问题](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter8/5concurrency-problem.html)

