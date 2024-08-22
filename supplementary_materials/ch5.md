# [第五章：进程](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/0intro.html)
之前内容的核心是通过各类演化形成了分时、虚拟化、分层、隔离等指导思想，着力点在于让程序能合理高效的运行；
到了进程，着力点成为让开发者能够控制程序的运行，所谓控制离不开交互，这就是shell的使命与到来。
“任务”是从OS执行角度的抽象，设计用户控制交互时候，需要将“任务”升级为“进程”抽象。
所谓抽象之后的对象，程序中意味着api，“进程”（进行中的程序）这个对象的基本API有create,destroy,wait,info,other。
## [进程概念及重要系统调用](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/1process.html)
Process vs. Task差异在于动态，同一个可执行文件可以启动两个不同进程，他们对于硬件资源的绑定、解绑不同。
线程之间共享进程的内存空间，但是有自己独立的栈和控制流；
线程既可以在 OS控制也可以在用户态控制（GreenThread）；
多个协程Coroutine，Fiber共享一个线程的栈，存在于用户态，因此OS看不到协程，也就谈不上对协程的管理；
## [进程管理的核心数据结构](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/2core-data-structures.html)
## [进程管理机制的设计实现](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/3implement-process-mechanism.html)
## [进程调度](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter5/4scheduling.html)

