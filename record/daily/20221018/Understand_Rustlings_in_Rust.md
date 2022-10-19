# 理解Rustlings in Rust

[rustlings](https://github.com/rust-lang/rustlings) is project host by [rust-lang](https://github.com/rust-lang), which contains small exercises to get you used to reading and writing Rust code.

From r1, rustlings is a set of exercises that serves as a great introduction to the Rust language. It covers many concepts from the [Rust book](https://doc.rust-lang.org/book/title-page.html) by asking you to work through sets of exercises.

From r2, rustlings is an open source project by the Rust team that helps you learn Rust through the process of debugging.

## Install & Use & Uninstall

```
####### Linux ########
# install gcc
curl -L https://raw.githubusercontent.com/rust-lang/rustlings/main/install.sh | bash
cd rustlings
rustlings watch	# 实时监控你修改后的代码并重新编译
rustlings verify	# 只运行一次, 碰到编译错误就退出
rustlings list		# 查看所有exercise以及状态
rustlings run specific_exercise		# specific_exercise 是`rustlings list`列出的name
rustlings hint specific_exercise	# 请求提示
rustlings run next	# 运行下一个unsolved exercise by verify mode
rustlings lsp		# enable rust-analyzer
# Uninstalling rustlings
cd ..
rm -rf rustlings
cargo uninstall rustlings
```

## rustlings watch not work

在Windows WSL2上，用`rustlings watch`不能自动刷新；

根据[#79](https://github.com/rust-lang/rustlings/issues/417)，as a workaround, rustlings watch will work correctly if you move rustlings into your WSL2 filesystems (like ~ )

## References

1. [Learning Rust by Working Through the Rustlings Exercises](https://egghead.io/courses/learning-rust-by-solving-the-rustlings-exercises-a722)
2. [Learn Rust by debugging Rust](https://opensource.com/article/22/7/learn-rust-rustlings) 

