# 如何训练DNN

原文链接[How to train your Deep Neural Network](http://rishy.github.io//ml/2017/01/05/how-to-train-your-dnn/)By Rishabh Shukla

## 简介
本文将提供一部分训练DNN的tricks，包括训练数据的质量、超参数的选用等。大部分tricks已经被试验和理论证实，可参考[Efficient BackProp(Yann LeCun et al.)](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)和[Practical Recommendations for Deep Architectures(Yoshua Bengio)](https://arxiv.org/pdf/1206.5533v2.pdf)等。

## 训练数据
直接将原始数据输入DNN不一定能得到好的结果。
- 获取尽可能多的数据（DNN训练需要大量数据，越多越好）
- 剔除被污染的数据样本（短文本、高度扭曲的图像、错误的数据标签、有很多空值的特征等）
- 数据扩充-创造更多的样本（以图像为例，重置大小、增加噪声等）

## 选择合适的激活函数
- 激活函数将非线性引入模型。以往的sigmoid函数具有两大缺陷：1）过饱和，可能导致梯度消失；2）不是以0为中心的。
- 替代函数有tanh，ReLU和SoftSign等。

## 隐藏单元和隐藏层数量
- 保证尽可能多的隐藏单元通常是安全的，因为任何正则化方法都能在某种程度上处理多余的单元；隐藏单元较少时，可能会导致模型欠拟合。
- 当采用无监督预训练表征时，最优隐藏单元数通常会很大，因为预训练表征可能会包含大量的无关信息（针对特定监督任务来说）。
- “尽管加训练层，直到测试误差不再改善为止”（[Yoshua Bengio](https://www.quora.com/profile/Yoshua-Bengio)）

## 初始化权重
- 利用小的随机数来初始化权重，以打破单元之间的对称性。同时，在使用sigmoid激活函数时，若初始权重过大，sigmoid会过饱和，导致单元失效。而若权重过小，梯度将会很小。
- 利用均匀分布来初始化权重更好；拥有更多输入连接的单元应设置相对较小的权重。

## 学习速率
- 最重要的超参数之一，速率过小会导致收敛慢，速率过大会导致损失增大。通常设置为0.01。
- 学习速率也可设置为变量，通常情况下每次迭代后速率减半。
- 基于动量的方法可以根据误差函数曲线来改变学习速率，同时也可以针对模型中的不同参数设置不同的速率。
- 自适应学习速率，如Adagrad或Adam方法可自动设置学习速率。

## 学习方法
- 在DNN中随机梯度下降效果可能不好，可采用Adagrad，Adam，AdaDelta，RMSProp等，除了提供自适应学习速率，这些方法同时为不同模型参数提供不同速率，加速收敛。

## 将权重维度设置为2的指数
- 将权重参数设置为2的指数，如64,128,1024等，有利于矩阵和权重等分区，提高学习效率；在GPU中训练模型时效果更显著。

## 小批量和随机学习
- 采用随机学习方法时，权重梯度在每个训练样本后进行更新，会引入梯度噪声，可预防过拟合；同时会导致收敛缓慢。
- 建议使用小批量学习，选择合适大小的样本批量，以保证部分噪声，同时提高计算效率。通常采用16-128个样本为一个小批量。

## 打乱训练样本
- “从不太可能发生的事件中学习比从常见事件中学习效率更高”，将训练样本的次序随机会加速收敛。
- *在DQN中，从经验区随机采样，可打破样本之间的联系。*

## Dropout正则化
- 利用dropout而不是L1/L2可避免过拟合，同时可加速学习速率；通常采用0.5，如果模型较简单可采用0.2。详细参见[原文](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)。

## 视觉输出
- 将训练过程以图像输出，方便调bug，如损失、训练误差和测试误差等。
- 画出权重在不同训练样本或迭代上的直方图，方便定位问题，如梯度消失和梯度爆炸等。

## 多核计算机，多GPU
- 多核CPU和多GPU可显著加速训练

## 使用支持GPU和自动微分的库
- [Theano](http://deeplearning.net/software/theano/)，[Tensorflow](https://www.tensorflow.org/)，[Keras](https://keras.io/)等DL库都提供GPU计算和自动微分支持；Tensorflow同时支持分布式架构。

## 参考文献
1.[Efficient BackProp(Yann LeCun et al.)](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

2.[Practical Recommendations for Deep Architectures(Yoshua Bengio)](https://arxiv.org/pdf/1206.5533v2.pdf)

3.[Understanding the difficulty of training deep feedforward neural networks(Glorot and Bengio, 2010)](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf)

4.[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

5.[Andrej Karpathy - Yes you should understand backprop(Medium)](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b#.yd17cx8ml)
