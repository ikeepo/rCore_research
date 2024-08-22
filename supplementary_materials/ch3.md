# [第三章：多道程序与分时多任务](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/0intro.html)
- 批处理batch vs. 多道程序multiprogramming vs. 分时多任务Multitasking
批处理是不停歇的一个接一个执行任务；
多道程序是内存中同时驻留多个应用，一个程序被执行完或主动放弃执行，处理器才能执行另外一个；
分时TimeSharing多任务Multitasking是一种抢占式分配计算资源；
## [多道程序放置与加载](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/1multi-loader.html)
## [任务切换](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/2task-switching.html)
- [不同类型的上下文与切换](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/2task-switching.html#id4)
## [多道程序与协作式调度](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/3multiprogramming.html)
## [分时多任务系统与抢占式调度](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter3/4time-sharing-system.html)
同步是一条指令流，异步是两条指令流。
