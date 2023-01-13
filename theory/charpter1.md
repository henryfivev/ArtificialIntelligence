# Knowledge Representation and Inference

## 2.1 Hanoi

设P(x, y)表示x在y的上方，Q(x)表示x可移动，L(x, y)表示x比y小，

K(x)表示可移动x个盘子，M(x)表示x在柱子3，N(x)表示x在柱子1

则Hanoi问题可表示为：

$$
N(A),N(B),N(C),\\
K(1),\neg (\exist xP(x, y))\to Q(y),P(x,y)\and L(x,y)
$$

目标为：
$$
M(A),M(B),M(C)
$$

## 2.2 合一

### （1）

$$
\begin{aligned}
1.\quad\delta_{0}&=\varepsilon, W_{0}=W\\
2.\quad W_{0}&未合一,\\
D_{0}&=\{a,z\}\\
3.\quad \delta_{1}&=\{a/z\}\\
W_{1}&=\{P(a,x,f(g(y))),P(z,h(z,u),f(u))\}\{a/z\}\\
&=\{P(a,x,f(g(y))),P(a,h(a,u),f(u))\}\\

4.\quad W_{1}&未合一,\\
D_{1}&=\{x,h(a,u)\}\\
5.\quad \delta_{2}&=\{a/z,h(a,u)/x\}\\
W_{2}&=\{P(a,x,f(g(y))),P(a,h(a,u),f(u))\}\{h(a,u)/x\}\\
&=\{P(a,h(a,u),f(g(y))),P(a,h(a,u),f(u))\}\\

6.\quad W_{2}&未合一,\\
D_{2}&=\{g(y),u\}\\
7.\quad \delta_{3}&=\{a/z,h(a,u)/x,g(y)/u\}\\
W_{3}&=\{P(a,h(a,u),f(g(y))),P(a,h(a,u),f(u))\}\{g(y)/u\}\\
&=\{P(a,h(a,g(y)),f(g(y)))\}\\

8.\quad W_{3}&中只含一个元素，所以\\
\delta_{3}&=\{a/z,h(a,u)/x,g(y)/u\}\\
是W&的最一般合一，终止。

\end{aligned}
$$

### （2）

$$
\begin{aligned}
1.\quad\delta_{0}&=\varepsilon, W_{0}=W\\

2.\quad W_{0}&未合一,\\
D_{0}&=\{f(a),y\}\\
3.\quad \delta_{1}&=\{f(a)/y\}\\
W_{1}&=\{P(f(a),g(s)),P(y,y)\}\{f(a)/y\}\\
&=\{P(f(a),g(s)),P(f(a),f(a))\}\\

4.\quad W_{1}&未合一,\\
D_{1}&=\{f(a),g(s)\}\\
5.\quad D_{1}&中的元素为两个函数，所以W不可合一

\end{aligned}
$$

### （3）

$$
\begin{aligned}
1.\quad\delta_{0}&=\varepsilon, W_{0}=W\\

2.\quad W_{0}&未合一,\\
D_{0}&=\{a,z\}\\
3.\quad \delta_{1}&=\{a/z\}\\
W_{1}&=\{P(a,x,h(g(z))),P(z,h(y),h(y))\}\{a/z\}\\
&=\{P(a,x,h(g(a))),P(a,h(y),h(y))\}\\

4.\quad W_{1}&未合一,\\
D_{1}&=\{h(y),x\}\\
5.\quad \delta_{2}&=\{a/z,h(y)/x\}\\
W_{2}&=\{P(a,x,h(g(a))),P(a,h(y),h(y))\}\{h(y)/x\}\\
&=\{P(a,h(y),h(g(a))),P(a,h(y),h(y))\}\\

6.\quad W_{2}&未合一,\\
D_{2}&=\{g(a),y\}\\
7.\quad \delta_{3}&=\{a/z,h(y)/x,g(a)/y\}\\
W_{3}&=\{P(a,h(y),h(g(a))),P(a,h(y),h(y))\}\{g(a)/y\}\\
&=\{P(a,h(g(a)),h(g(a)))\}\\

8.\quad W_{3}&中只含一个元素，所以\\
\delta_{3}&=\{a/z,h(y)/x,g(a)/y\}\\
&是W的最一般合一，终止。

\end{aligned}
$$

## 2.3 归结

$$
设P(x,y)表示y是x的兄弟\\
L(x)表示x是女性\\
Q(x,y)表示y是x的姐妹\\
则规则1可表示为\forall xP(x,y)\to\neg L(y)\\
规则2可表示为\forall xQ(x,y)\to L(y)\\
事实可表示为Q(Bill,Mary)\\
"Mary不是Tom的兄弟"的否定为P(Tom,Mary)\\
而\forall xP(x,y)\to\neg L(y)即\neg P(x,y)\or \neg L(y)\quad 实例化得(1)\\
\forall xQ(x,y)\to L(y)即\neg Q(x,y)\or L(y)\quad 实例化得(2)\\
(1)\neg P(Tom,y)\or \neg L(y)\\
(2)\neg Q(Bill,y)\or L(y)\\
(3)Q(Bill,Mary)\\
(4)P(Tom,Mary)\\
(5)\neg P(Tom,y) \or \neg Q(Bill,y) \qquad (1)(2)归结\\
(6)\neg Q(Bill,Mary) \quad (4)(5)\{Mary/y\}\\
(7)\{\} \quad (3)(6)归结
$$



## 2.4 支持集策略

$$
(1)\\
设A(x)表示x是贼\\
B(x,y)表示x喜欢y\\
C(x,y)表示x可能会偷窃y\\
则子句1至5分别为\\
1.A(John)\\
2.B(Paul,wine)\\
3.B(Paul,cheese)\\
4.\neg B(Paul,x)\or B(John,x)\\
5.\neg A(x)\or \neg B(x,y) \or \neg C(x,y)\\
(2)\\
假设John可能会偷窃wine或cheese\\
则目标子句的否定为\neg C(John,wine)\and \neg C(John,cheese)\\
1.A(John)\\
2.B(Paul,wine)\\
3.B(Paul,cheese)\\
4.\neg B(Paul,x)\or B(John,x)\\
5.\neg A(x)\or \neg B(x,y) \or C(x,y)\\
6.\neg C(John,wine)\\
7.\neg C(John,cheese)\\
8.\neg A(John) \or \neg B(John,wine) \quad (5)(6)归结\{John/x，wine/y\}\\
9.\neg B(John,wine) \quad (1)(8)归结\\
10.\neg B(Paul,wine)\quad (4)(9)归结\{wine/x\}\\
11.\{\} \quad (2)(10)归结\\
所以John可能会偷窃wine\\
12.\neg A(John) \or \neg B(John,cheese) \quad (5)(7)归结\{John/x，cheese/y\}\\
13.\neg B(John,cheese) \quad (1)(12)归结\\
14.\neg B(Paul,cheese)\quad (4)(13)归结\{cheese/x\}\\
15.\{\} \quad (3)(14)归结\\
所以John可能会偷窃cheese\\
综上，John可能会偷窃wine或cheese
$$

## 2.5 逻辑推导

$$
设A(x,y)表示x通过了y的考试\\
B(x)表示x中了彩票\\
C(x)表示x是快乐的\\
D(x)表示x肯学习\\
E(x)表示x是幸运的\\
则由题可得\\
1.\forall x(A(x,历史)\and B(x) \to C(x))即\\
\neg A(x,历史) \or \neg B(x) \or C(x)\\
2.\forall x \forall y(D(x) \or E(x) \to A(x,y))即\\
(\neg D(x) \or A(x,y)) \and (\neg E(x) \or A(x,y)) \\
3.\neg D(小张)\\
4. E(小张)\\
5.\forall x (E(x) \to B(x))即\\
\neg E(x) \or B(x) \\
开始归结\\
1.\neg A(x,历史) \or \neg B(x) \or C(x)\\
2.\neg D(x) \or A(x,y)\\
3.\neg E(x) \or A(x,y)\\
4.\neg D(小张)\\
5.E(小张)\\
6.\neg E(x) \or B(x)\\
7.A(小张,y) \quad (3)(5)归结\{小张/x\}\\
8.B(小张)\quad (5)(6)归结\{小张/x\}\\
9.\neg A(小张,历史) \or C(小张) \quad (1)(8)归结\{小张/x\}\\
10.C(小张) \quad (7)(9)归结\{历史/y\}\\
所以小张是快乐的
$$
