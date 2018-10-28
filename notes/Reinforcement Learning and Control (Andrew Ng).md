# Reinforcement Learning and Control (Andrew Ng)

标签（空格分隔）： RL

---
## MDP介绍
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
- 马尔科夫决策过程$\{S,A,P,\gamma,R\}$，$R:S\times A \rightarrow \mathbb{R}$是reward函数
- RL的目标是最大化决策过程中的期望value，$\mathbb{E}[R(s_0,a_0)+\gamma R(s_1,a_1)+\gamma^2R(s_2,a_2)+...]$
- 策略是状态到行为的映射$\pi:S\rightarrow A$。Value函数据此定义为：$V^{\pi}(s)=\mathbb{E}[R(s_0,a_0)+\gamma R(s_1,a_1)+\gamma^2R(s_2,a_2)+...|s_0=s,\pi]$
- Value函数符合Bellman方程：$V^{\pi}(s)=R(s)+\gamma \sum_{s'\in S}P_{s,\pi(s)}(s')V^{\pi}(s')$
- 优化目标函数转换为$V^*(s)=\mathop{\max}\limits_{\pi}V^{\pi}(s)$
- 策略到行为的映射$\pi^*:S\rightarrow A$：$\pi^*(s)=\mathop{\arg}\mathop{\max}\limits_{a\in A}\sum_{s'\in S}P_{s,a}(s')V^*(s')$

## Value迭代和策略迭代
本文关注有限状态MDP，即$|S|<\infty, |A|<\infty$。
value迭代和策略迭代目前没有优劣之分，对于小规模MDP，策略迭代收敛较快；对于状态空间较大的MDPs，直接求解$V^{\pi}$比较困难，因而常用value迭代。
### value迭代

- 对于每个状态$s$，初始化$V(s):=0$；
- 重复直到收敛
 - 对于每个状态，更新$V(s):=R(s)+\mathop{\max}_{a\in A}\gamma\sum_{s'}P_{s,a}(s')V(s')$
- value函数收敛至$V^*$，可利用策略到行为的映射$\pi^*:S\rightarrow A$找到最优策略

    **更新方法：**

- 同步更新：计算每个$s$的value函数$V(s)$，对旧值进行更新
- 异步更新：遍历所有状态，每次更新一个
 
### 策略迭代

- 随机初始化策略$\pi$
- 重复直到收敛
 - 令$V:=V^{\pi}$（利用Bellman方程求解）
 - 对于每个状态，令$\pi(s):=\mathop{\arg}\mathop{\max}\limits_{a\in A}\sum_{s'}P_{s,a}(s')V(s')$（贪婪算法）
- 经过有限次迭代，得到收敛的$V^*$和$\pi^*$

## MDP学习模型
在MDP的实际应用中，状态转移函数和回报函数常常是未知的，仅能够从数据中进行估计。

- 状态转移函数是经过大量的训练，经过极大似然估计得到的：$P_{s,a}(s')=\frac{N_{s,a}(s')}{N_{s,a}}$，其中N表示次数。
- 如果$N_{s,a}=0$，则认为$P_{s,a}(s')=1/|S|$，即各状态均匀分布。
- 如果回报函数$R$未知，利用$R(s)$的期望估计值作为状态$s$的平均回报。

**算法举例：**

- 随机初始化$\pi$
- 重复以下步骤
 - 针对部分训练执行策略$\pi$
 - 利用MDP中的累积经验，对状态转移函数$P_{s,a}$和回报函数$R(s)$进行更新
 - 利用更新后的$P_{s,a}$和$R(s)$执行value迭代，得到新的value函数$V$
 - 根据新value函数$V$和贪婪算法更新$\pi$

## 连续状态MDP
例如，对于汽车来说，其状态可表示为$(x,y,\theta,\dot{x},\dot{y},\dot{\theta})$，表示状态集合无限
### 离散化

 1. 将状态空间离散化，使用value或策略迭代算法。
 2. 利用离散状态MDP$(\bar{S},A,\{P_{s,a}\},\gamma,R)$来近似连续状态MDP，其中$\bar{S}$是离散状态空间集合，$\{P_{s,a}\}$是离散空间上的状态转移函数。
 3. 使用value迭代或策略迭代求解离散空间状态中的$V^*(\bar{s})$和$\pi^*(\bar{s})$。
 4. 离散化的主要缺点：
 5. 离散化假设value方程在各个离散间隔中是一个常数，造成连续函数不够光滑，此时只能最大地对空间进行离散化
 6. Curse of dimensionality，离散状态随着空间维度指数型增长，不适用于大规模问题。
### Value函数估计
直接对value函数$V^*$进行估计。
#### 1. 利用模型或仿真器
**基本思想：**假设存在一个黑盒模型，输入此刻状态$s_t$和行为$a_t$，根据状态转移函数$P_{s_t,a_t}$输出下一刻状态$s_{t+1}$。

 7. **物理仿真方法**。利用物理仿真软件，将物理特性作为模型参数进行运动学/动力学仿真
 8. **数据处理方法**。在一个MDP中重复训练，随机产生行为，利用最大似然估计根据此刻的状态和行为对下一刻的状态进行预测，如针对线性随机模型（实际上可能是非线性的）：
$$\mathop{\arg}\mathop{\max}\limits_{A,B}\sum_{i=1}^{m}\sum_{t=0}^{T-1}||s_{t+1}^{(i)}-(As_t^{(i)}+Ba_t^{(i)}+\epsilon_t^{(i)})||^2$$
    - $s_{t+1}=As_t+Ba_t+\epsilon_t$，其中噪声$\epsilon_t \sim \rm{N}(0,\Sigma)$，协方差阵$\Sigma$从数据中估计得到
    - 对于非线性模型，可用$s_{t+1}=A\phi_s(s_t)+b\phi_a(a_t)+\epsilon_t$，利用非线性学习算法，如局部加权线性回归来估计
#### 2.拟合value迭代
**假设：**在此假设问题是连续状态空间$S=\mathbb{R}^n$，而行为空间$A$较小且离散。
**基本思想：**在有限采样空间$s^{(1)},s^{(2)},...,s^{(m)}$上对拟合value进行估计。利用监督学习算法来估计value函数（以状态为变量的线性/非线性函数）

 1. 对于采样的$m$状态空间中的每个状态$s$，拟合value函数首先计算$y^{(i)}$作为value函数$R(s)+\gamma\mathop{\max}\limits_aE_{s'\sim P_{s,a}}[V(s')]$的估计
 2. 利用监督学习算法使$V(s)$逼近$R(s)+\gamma\mathop{\max}\limits_aE_{s'\sim P_{s,a}}[V(s')]$，或者逼近$y^{(i)}$
 3. 拟合value迭代输出$V$，即$V^*$的近似，由此可计算策略。根据策略和状态选择行为：$\mathop{\arg}\mathop{\max}\limits_aE_{s'\sim P_{s,a}}[V(s')]$

**第2步详细算法如下：**
    
 - 随机抽样$m$个状态$s^{(1)},s^{(2)},...,s^{(m)}\in S$
 - 初始化$\theta:=0$
 - 重复执行：
 for $i=1,..,m${
 $\quad$for each action $a \in A${
        $\qquad$利用MDP模型采样$s'_1,...,s'_k \sim P_{s^(i),a}$
        $\qquad$设$q(a)=\frac{1}{k} \sum_{j=1}^k {R(s^{(i)})+\gamma V(s'_j)}$
        $\qquad$// $q(a)$是value函数的估计
    $\quad$}
    $\quad$设$y^{(i)}=\mathop{\max}\limits_a q(a)$
    $\quad$// $y^{(i)}$是最优value函数的估计
 }
 //离散空间初始value函数迭代算法
 //根据$V(s^{(i)}):=y^{(i)}$更新value函数
 //利用监督学习（线性回归）使$V(s^{(i)}) \approx y^{(i)}$[^hello]
 设$\theta := \mathop{\arg}\mathop{\max}\limits_{\theta}\frac{1}{2} \sum_{i=1}^m (\theta^T \phi(s^{(i)})-y^{(i)})^2$

**拟合value迭代缺点：**

- 拟合value迭代不能保证收敛
 
[^hello]: 此处类似标准监督学习过程，即得到状态$s$到$y^{(i)}$的映射。
 