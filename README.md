# auto-mvp

采用MVP模式做了不少应用了。
MVP的优点，就是层次分明，逻辑清晰，代码低耦合。缺点也是很明显：代码量大，文件多到要爆炸。

这个工具，解决不了代码多的问题，但是能为你自动生成这些代码。

## 思路
MVP即Model-View-Presenter。可能一千个人，能写出一千个写法，但只要是MVP模式，就能抽象出个模板。
我就根据项目中的一个接口的MVP全套代码，将其类名、方法名、参数等具体细节用占位符替代，形成一套模板。
然后，将具体的每一个几口，用json描述出来。再用python解析json，并将具体参数一一替换占位符，最终生成对应文件。

## 用法
```python auto_mvp.py [apiName]```

暂只能用与个人的项目，没有通用化，但代码比较简单，思路也简单，很容易扩展。


不了解MVP？参考[google-sample:MVP](https://github.com/googlesamples/android-architecture)