

# 226逆向记录



### 分包分析

请求该数据包、可以发下每次都会弹出验证码，这里简称为阿里系吧！

![image-20231030143532870](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030143532870.png)



### 参数分析

手动划过验证可以发现请求多了几个参数，然后就能拿到数据了

![image-20231030143721285](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030143721285.png)





在工具里面搜索可以发现参数的来源于以下的接口，可以发现发现`u_asession`和`u_asig`是通过这个文件返回的，但是需要带上以下参数，其中的`p、t、n`可能会发生变化，需要注意的是这里的 t 和前面的`u_atoken`相同，所以目前还缺少`u_aref、p、n、u_atoken（t）`

![image-20231030143833671](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030143833671.png)



 搜索一下`u_aref`的值，会发现`u_aref、u_atoken（t`）在滑块的`html`里返回的，所以现在只剩下`p、n`两个

![image-20231030144059468](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030144059468.png)



 通过上面的分析可以：逆向到`p、n`两个参数的生成即可通过滑块,可以发现P是`226`开头、就简称为226吧！ 世人都这么喊来着~

### 逆向分析

定位到鼠标定位，断点断住后滑动滑块，尝试后发现验证通过时会经过 `m` 方法

![image-20231030145704963](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030145704963.png)

然后跟进`m`方法、可以找到参数生成的位置

![f](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030145637453.png)



继续跟`o.__fy.getFYToken`函数，这个`o`参数是不会变化的，增加复制下来就行,持续往里面跟进可以发现最终生成位置在这

![image-20231030145918986](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030145918986.png)



`I`方法就是用来生成滑块值的，如果想扣代码的同学可以尝试从这里入手。

![image-20231030150011744](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20231030150011744.png)









