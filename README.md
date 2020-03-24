# OR_Learn  运筹学知识总结，以及经典模型代码的编写（python）
## 线性回归
在用代码实现线性回归模型之前，最重要的是模型的确定与建立，之后直接调用linprog()函数即可，需要注意的是：matlab中线性模型的标准形式为<br>
![](https://github.com/yangxcc/OR_Learn/raw/master/image/standard.png) <br>
因此在使用linprog()时，要注意把非标准化的数学形式转化成标准形式。
