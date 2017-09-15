# Sublime Text 3

Sublime Text 可以说是一款非常好的编辑器了，我这个人一贯随大流，配过 Vim、 Spacemacs 等等，最终还是决定追随 `KENNETH REITZ` 的配置

## 安装

安装不用说了，直接 Homebrew

```cmd
$ brew cask install sublime-text
```

## 配置

这里有篇大神的配置 [https://www.kennethreitz.org/essays/sublime-text-3-heaven](https://www.kennethreitz.org/essays/sublime-text-3-heaven)

跟着配置就行了


## 遇到的坑

### SideBar 配置

SideBar 显得太小，所以要配置一个稍微大的字体

参照 [https://stackoverflow.com/questions/23045968/increase-the-font-size-of-text-in-sublime-side-bar](https://stackoverflow.com/questions/23045968/increase-the-font-size-of-text-in-sublime-side-bar)

然后简单的步骤：

1. 安装 PackageResourceViewer: command+shift+p -> Install package -> prv
2. Open Resource: command+shift+p -> Open Resource -> Material Theme -> Material-Theme-Darker.sublime-theme
3. 修改 sidebar_label 增加 "font.size": 15