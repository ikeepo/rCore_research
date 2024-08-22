# [第七章：进程间通信与 I/O 重定向](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/0intro.html)
通过用户在shell里面输入输出，叫做标准输入输出。
其他的“不标准”有进程间通讯之类。
当谈及进程间通讯，就引出了概念“管道”;进一步扩展，让操作系统不仅仅是被动相应程序的调用，而能够主动让进程相应 OS出发的通知，就引入了信号Signal；
Signal作用机理：用户（一个进程）通过系统调用给目标进程发送信号，操作系统修改目标进程控制块中的signal结构，然后优先处理signal结构再决定对目标进程其他功能的实现；
标准输入输出+管道（进程间通讯）+文件 = Everything is a file；
## [基于文件的标准输入/输出](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/1file-descriptor.html)
- 文件描述符
1. 标准输入 0，Stdin
2. 标准输出 1，Stdout
3. 标准错误 2，Stderr
## [管道](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/2pipe.html)
## [命令行参数与标注I/O重定向](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/3cmdargs-and-redirection.html)
## [信号](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter7/4signal.html)
当信号发送给一个进程时，OS会中断目标进程的执行流程，先对信号进行处理；因此又可以称为软件中断。



