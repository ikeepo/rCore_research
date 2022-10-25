
How to delete commit/contributor in github
====================

## Delete Commit

```
git reset --hard hash_str
git push --force orign master
```

[重置](https://stackoverflow.com/questions/38402396/how-to-delete-commits-from-git-on-github-and-bitbucket)成之前一个commit, 就相当于把之后的commit删除了。

## Delete Contributor

这个没找到好办法。

即便删除某个contributor的所有commit，Contributors依然有。

Contributors are not collaboratores.

可以通过修改分支名称，然后再改回来的方式删除错误提交的contributor name。

## References

1. [Remove contributor from main page of github repo](https://stackoverflow.com/questions/64485896/remove-contributor-from-main-page-of-github-repo)  
2. [Removing contributor from github.com?](https://stackoverflow.com/questions/44563131/removing-contributor-from-github-com)