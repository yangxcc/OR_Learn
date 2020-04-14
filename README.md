# OR_Learn  运筹学知识总结，以及经典模型代码的编写（python）
## 线性回归
在用代码实现线性回归模型之前，最重要的是模型的确定与建立，之后直接调用linprog()函数即可，需要注意的是：matlab中线性模型的标准形式为<br>
![](https://github.com/yangxcc/OR_Learn/raw/master/image/standard.png) <br>
因此在使用linprog()时，要注意把非标准化的数学形式转化成标准形式。<br>
灵敏度分析研究的是模型参数的取值变化对最优解或者最优基的影响，模型参数的变化包括三个部分：<br>
(1)目标函数系数的变化<br>
(2)约束条件右端值的变化<br>
(3)目标函数中价值系数的变化<br>
每种不同的变化都对应不同的解题方法。<br>
**运输问题**通常有m个产地，n个销地，其中还存在产销平衡，产销不平衡两种形式，运输问题显然是一个线性规划问题，但是其约束条件的系数矩阵相当特殊，
可以使用更为简单的计算方法，通常称为表上作业法，通过最小元素法（或者最大差额法，或者西北角法）求得初始基本解，通过位势法（或者闭回路）检验是否为
最优基。<br>
**整数规划**是在基本线性回归模型的基础上，添加决策变量均为整数的约束条件，求解方法有`分支定界法`和`割平面法`，两种方法最开始都是先不考虑整数条件，求出最优解，然后根据最优解来进行下一步，分支定界法是根据最优解中某一非整决策变量进行调整，找出小于其的最大整数和大于其的最小整数，经过不断的分支筛选，找出其中最优解为整数且最优值最大的一组数据。割平面法也是根据最开始求出的最优解进行下面的操作，其中最主要的操作就是将每行的系数（包括决策变量前的系数和约束条件右端的值）分解为整数部分和非负真分数部分，然后将整数部分移到一边，非整数部分移到一边，进行之后的操作，具体见文档。<br>
**0-1规划**是整数规划的一种特殊形式，整数规划中的全部变量为0或1的逻辑变量求解0-1规划的有效方法是`隐枚举法`，隐枚举法的实质是一种特殊的分支定界法，但一般用分支定界法求解整数规划时，替代问题是放松变量的整数约束，但用枚举法是，替代问题是在保持变量0或1的约束条件下先不考虑主要约束。隐枚举法的使用步骤见文档。<br>
**标准指派问题**在实际中经常会遇到这样的问题，有n项不同的任务，需要n个人分别完成其中的一项，但由于任务的性质和各人的专长不同，因此各人去完成不同的任务的效率（或花费的时间或费用）也就不同。于是产生了一个问题：应指派哪个人去完成哪项任务，使完成n项任务的总效率最高（或所需时间最少），**非标准形的指派问题**有人数、任务数不相等（通过增加任务、人数来标准化），一个人可完成多件任务的分配问题，某事一定不能由某人完成。这些非标准化的指派问题都要先化为标准化的指派问题，然后再用`匈牙利算法`计算，匈牙利算法比较麻烦，具体的步骤见文档。<br>
**目标规划**研究企业考虑现有的资源条件下，在多个目标中去寻求满意解，使得完成目标的总体结果与事先制定目标的差距最小。线性规划是在一组线性约束条件下寻求某一项目标的最优值，而经营管理中人们希望更多目标达到较好水平。线性规划最优解存在的前提条件是可行域为非空集，否则线性规划无解。在目标规划中求出的解通常不能满足所有的约束条件，因此称其解为满意解。在建模过程中，首先需要设置偏差变量，表明实际值同目标值之间的差异，然后再将约束条件分成绝对约束和目标约束，最后确定优先因子和权系数，高一级的优先因子远远大于低一级的优先因子，因此，在计算过程中，要首先满足高一级的约束条件。目标规划问题求解时，把绝对约束做最高优先级考虑。能依先后顺序都满足，则𝑧∗ = 0，但在大多数问题中并非如此，会出现某些约束得不到满足，故将目标规划问题的最优解称为满意解。目标规划的模型如下：<br>
![](https://github.com/yangxcc/OR_Learn/blob/master/image/%E7%9B%AE%E6%A0%87%E8%A7%84%E5%88%92%E6%A8%A1%E5%9E%8B.png)<br>
**动态规划**解决的一般是多阶段性决策问题，在解决这类问题时通常需要逆推得出最优解，然后顺推得出结论，在使用动态规划解决问题之前，首先要弄清其中的基本概念，包括：`阶段（变量）`，`状态（变量）`，`状态转移（方程）`，`决策（变量）`，`指标（函数）`，动态规划的基本类型有离散确定型、离散随机型、连续确定型、连续随机型。是用动态规划解决问题的步骤如下：**建立模型、逆推得出最优解、顺推得出结论**，其中建立模型的过程包括：
* 划分阶段，设定 k
* 设定状态变量s<sub>k</sub>，设定决策变量 x<sub>k</sub>，
* 建立状态转移方程
* 确定指标函数 v<sub>k</sub>，f<sub>k</sub><sup>*</sup> ，建立函数基本方程
**网络规划**包括图、树的基本概念，最大流问题，最短路径问题，最小费用最大流问题等，在概念问题中要注意两个定理：（1）图G=(V,E)中,所有点的次之和是边数的两倍 （2）任意一图中, 奇点的个数为偶数，最小支撑树的求法有三种，破圈法、避圈法以及顶点扩充法，三种方法基本思路大同小异，在避免形成环的前提下，尽量找到权值小的边。

