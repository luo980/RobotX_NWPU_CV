# RobotX_NWPU_CV

## 写在前面

### 如何下载仓库信息
`git clone https://github.com/luo980/RobotX_NWPU_CV.git`

### 如何更新库信息
`git add .`

### 如何push request
`git push -u origin master`

### 成为contributor 点主页右上角fork
`fork`

### 如果显示remote contains work that you do not have locally
### 使用如下命令关联本地与远程分支
`git branch --set-upstream-to=origin/<branch> master`

### 更新方式如下


`git fetch origin master:tmp `
//在本地新建一个temp分支，并将远程origin仓库的master分支代码下载到本地temp分支


`git diff tmp `
//来比较本地代码与刚刚从远程下载下来的代码的区别


`git merge tmp`
//合并temp分支到本地的master分支


`git branch -d temp`
//如果不想保留temp分支 可以用这步删除


## 进阶部分

###基本概念
1、 master 主分支
2、 origin 远程主机

#### git pull
`git pull <远程主机名> <远程分支名>:<本地分支名>`

//取回远程主机某个分支的更新，再与本地的指定分支合并。

`git pull origin//远程主机 master//主分支 ： cv_tmp//本地分支`
git过程： 本地自己拥有一个分支，从远程下载一个分支，git diff比较不同

#### git push
`git push -u origin master`
将本地的master推送到远程主机的master
