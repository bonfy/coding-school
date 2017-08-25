package main

import "fmt"

// 我们将通过两个函数：`zeroval` 和 `zeroptr` 来比较指针和
// 值类型的不同。`zeroval` 有一个 `int` 型参数，所以使用值
// 传递。`zeroval` 将从调用它的那个函数中得到一个 `ival`
// 形参的拷贝。
func zeroval(ival int) {
	ival = 0
}

// `zeroptr` 有一和上面不同的 `*int` 参数，意味着它用了一
// 个 `int`指针。函数体内的 `*iptr` 接着_解引用_ 这个指针，
// 从它内存地址得到这个地址对应的当前值。对一个解引用的指
// 针赋值将会改变这个指针引用的真实地址的值。
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("intial i:", i)

	// zeroval 过后 i 不变，传的是形参copy
	zeroval(i)
	fmt.Println("zeroval i:", i)

	// zeroptr 过后 i 改变了值，传的是地址
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	fmt.Println("pointer:", &i)
}
