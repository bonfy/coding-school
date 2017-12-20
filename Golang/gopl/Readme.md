# GOPL (GO语言圣经)

> [https://www.gitbook.com/book/yar999/gopl-zh/details](https://www.gitbook.com/book/yar999/gopl-zh/details)

> [源码](https://github.com/adonovan/gopl.io/)

## 入门

Go语言不需要在语句或者声明的末尾添加分号，除非一行上有多条语句。实际上，编译器会主动把特定符号后的换行符转换为分号, 因此换行符添加的位置会影响Go代码的正确解析10。。举个例子, 函数的左括号{必须和func函数声明在同一行上, 且位于末尾，不能独占一行，而在表达式x + y中，可在+后换行，不能在+前换行。

从功能和实现上说，Go的map类似于Java语言中的HashMap，Python语言中的dict，Lua语言中的table，通常使用hash实现。遗憾的是，对于该词的翻译并不统一，数学界术语为映射，而计算机界众说纷纭莫衷一是。为了防止对读者造成误解，保留不译

`input := bufio.NewScanner(os.Stdin)`
该变量从程序的标准输入中读取内容。每次调用input.Scanner，即读入下一行，并移除行末的换行符；读取的内容可以调用input.Text()得到。Scan函数在读到一行时返回true，在无输入时返回false

```
%d          十进制整数
%x, %o, %b  十六进制，八进制，二进制整数。
%f, %g, %e  浮点数： 3.141593 3.141592653589793 3.141593e+00
%t          布尔：true或false
%c          字符（rune） (Unicode码点)
%s          字符串
%q          带双引号的字符串"abc"或带单引号的字符'c'
%v          变量的自然形式（natural format）
%T          变量的类型
%%          字面上的百分号标志（无操作数）
```

