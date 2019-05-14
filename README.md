# 在写 《关于script异步是否可以使用DOMContentLoaded》 的 DEMO/MOCK

博客地址 [关于script异步是否可以使用DOMContentLoaded](https://www.jianshu.com/p/53aa9c754173)

---

 # 首先要了解

 #### script/defer

defer是html4.0中定义的，该属性使得浏览器能延迟脚本的执行，等文档完成解析完成后会按照他们在文档出现顺序再去下载解析。也就是说defer属性的<script>就类似于将<script>放在body的效果。

如果script标签设置了该属性，则浏览器会异步的下载该文件并且不会影响到后续DOM的渲染；

如果有多个设置了defer的script标签存在，则会按照顺序执行所有的script。

defer脚本会在文档渲染完毕后，DOMContentLoaded事件调用前执行。 （defer为延迟的脚本按照定义它们的顺序运行，但它们仅在DOMContentLoaded事件被触发之前的片刻结束时执行。）

#### script/async

async是HTML5新增的属性，IE10和浏览器都是支持该属性的。该属性的作用是让脚本能异步加载，也就是说当浏览器遇到async属性的<script>时浏览器加载css一样是异步加载的。

async 属性规定一旦脚本可用，则会异步执行。

注释：async 属性仅适用于外部脚本（只有在使用 src 属性时）。

个人理解 ”async==不稳定的defer”


# DOMContentLoaded

#### DOMContentLoaded介绍

当初始的 HTML 文档被完全加载和解析完成之后，DOMContentLoaded 事件被触发，而无需等待样式表、图像和子框架的完成加载。另一个不同的事件 load 应该仅用于检测一个完全加载的页面。
注意：DOMContentLoaded 事件必须等待其所属script之前的样式表加载解析完成才会触发。
```
DOMContentLoaded：
  document.addEventListener("DOMContentLoaded", function(event) {
      console.log("LOADED");
  });
```

#### DOMContentLoaded兼容性
Chrome |	Firefox (Gecko) | Internet Explorer | Opera | Safari
:-:|:-:|:-:|:-:|:-:
0.2 | 1.0 (1.7 or earlier) | 9.0 | 9.0 | 3.1


# async、 defer、 没有defer或async 三者使用&比较

```<script src="script.js"></script>```
没有 defer 或 async，浏览器会立即加载并执行指定的脚本，“立即”指的是在渲染该 script 标签之下的文档元素之前，也就是说不等待后续载入的文档元素，读到就加载并执行。
```<script async src="script.js"></script>```
有 async，加载和渲染后续文档元素的过程将和 script.js 的加载与执行并行进行（异步）。
```<script defer src="myscript.js"></script>```
有 defer，加载后续文档元素的过程将和 script.js 的加载并行进行（异步），但是 script.js 的执行要在所有元素解析完成之后，DOMContentLoaded 事件触发之前完成。

点击执行后都为:
![](https://upload-images.jianshu.io/upload_images/14197274-e30d733a0081f966.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 以上都可以执行，接下来就是DOMContentLoaded

Dom

```<script  src="./DOMContentLoaded.js"></script>```

DOMContentLoaded.js

```
document.addEventListener("DOMContentLoaded",function(){
  var span=document.getElementById("demo\");
  console.log(span,"DOMContentLoaded")
})
```
 直接执行（没有问题）
![](https://upload-images.jianshu.io/upload_images/14197274-896455feda76c76c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

“defer”执行（没有问题）
<script defer src="./DOMContentLoaded.js"></script>
![](https://upload-images.jianshu.io/upload_images/14197274-51017cf4738af03b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

“async”执行（没有出现结果）

<script  async  src="./DOMContentLoaded.js"></script>
![](https://upload-images.jianshu.io/upload_images/14197274-2a34df97f947a573.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##总结

从上可知，需要了解HTML如何加载

> ![](https://upload-images.jianshu.io/upload_images/14197274-e562035200ebaaed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

猜想：DOMContentLoaded都执行完了，async还在异步执行中 （async是让这个script独立于页面其他部分加载，所以可能整个页面加载完成了，并且DOMContentLoaded在加载脚本或注册事件之前就执行了，所以就错过了事件）

> ![](https://upload-images.jianshu.io/upload_images/14197274-b62fa1dd76963c54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

参考：

[DOMContentLoaded 与 load事件](https://developer.mozilla.org/zh-CN/docs/Web/Events/DOMContentLoaded) 

[ js并行加载，顺序执行](http://www.cnblogs.com/grefr/p/5046307.html)

[Running Your Code at the Right Time](https://www.kirupa.com/html5/running_your_code_at_the_right_time.htm) 

---


当时写的时候用 python 生成文件的简单代码也存一下(手动滑稽)
