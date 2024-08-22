# [第四章：地址空间](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/index.html)
## [引言](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/0intro.html)
## [Rust中的动态内存分配](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/1rust-dynamic-allocation.html)
## [地址空间](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/2address-space.html)
- [增加硬件加速虚实地址转换](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/2address-space.html#id6)
固定间隔分配，方便，产生内碎片；按需不固定分配，高效，产生外碎片；分页内存管理结合两者优点。
虚拟空间分为页面Page具有虚拟页号VPN(Virtual Page Number)，物理空间分为页帧Frame具有物理页号PPN(Physical Page Number)，两者大小相同。
每个应用都有表示地址映射关系的页表Page Table.
页表里还针对虚拟页号设置了一组保护位，限制应用对转换得到的物理地址对应的内存的使用方式，比如rwx。
r表示当前应用可以读取该内存，w表示当前应用可以写该内存，x表示当前应用可以从该内存中取指令用来执行。

## [SV39多级页表的硬件机制](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/3sv39-implementation-1.html)
分页功能是MMU物理使能，默认CPU操作的是物理地址，使能分页功能才操作的是虚拟地址。
39指的是虚拟页地址表示方法需要39位，其中0-11低位表示PageOffset寻址2^12=4KiB，即一个Page大小；剩余39-12=27高位表示虚拟页号；
128M页号 x 4KiB = 512G内存空间。
在页表PageTable中，物理页号与标志位整体构成一个结构体，称为页表项PTE(PageTableEntry),是利用虚拟页号在也表中查到的结果。
## [管理SV39多级页表](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/4sv39-implementation-2.html)
## [内核与应用的地址空间](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/5kernel-app-spaces.html)
## [基于地址空间的分时多任务](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/6multitasking-based-on-as.html)
## [超越物理内存的地址空间](https://rcore-os.cn/rCore-Tutorial-Book-v3/chapter4/7more-as.html)
CPU有分时计算，内存也有分时复用，即SWAP，临时不用的内存放到硬盘上交换以扩展可用内存空间。
