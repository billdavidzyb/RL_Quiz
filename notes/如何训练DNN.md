# ���ѵ��DNN

ԭ������[How to train your Deep Neural Network](http://rishy.github.io//ml/2017/01/05/how-to-train-your-dnn/)By Rishabh Shukla

## ���
���Ľ��ṩһ����ѵ��DNN��tricks������ѵ�����ݵ���������������ѡ�õȡ��󲿷�tricks�Ѿ������������֤ʵ���ɲο�[Efficient BackProp(Yann LeCun et al.)](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)��[Practical Recommendations for Deep Architectures(Yoshua Bengio)](https://arxiv.org/pdf/1206.5533v2.pdf)�ȡ�

## ѵ������
ֱ�ӽ�ԭʼ��������DNN��һ���ܵõ��õĽ����
- ��ȡ�����ܶ�����ݣ�DNNѵ����Ҫ�������ݣ�Խ��Խ�ã�
- �޳�����Ⱦ���������������ı����߶�Ť����ͼ�񡢴�������ݱ�ǩ���кܶ��ֵ�������ȣ�
- ��������-����������������ͼ��Ϊ�������ô�С�����������ȣ�

## ѡ����ʵļ����
- �����������������ģ�͡�������sigmoid������������ȱ�ݣ�1�������ͣ����ܵ����ݶ���ʧ��2��������0Ϊ���ĵġ�
- ���������tanh��ReLU��SoftSign�ȡ�

## ���ص�Ԫ�����ز�����
- ��֤�����ܶ�����ص�Ԫͨ���ǰ�ȫ�ģ���Ϊ�κ����򻯷���������ĳ�̶ֳ��ϴ������ĵ�Ԫ�����ص�Ԫ����ʱ�����ܻᵼ��ģ��Ƿ��ϡ�
- �������޼ලԤѵ������ʱ���������ص�Ԫ��ͨ����ܴ���ΪԤѵ���������ܻ�����������޹���Ϣ������ض��ල������˵����
- �����ܼ�ѵ���㣬ֱ���������ٸ���Ϊֹ����[Yoshua Bengio](https://www.quora.com/profile/Yoshua-Bengio)��

## ��ʼ��Ȩ��
- ����С�����������ʼ��Ȩ�أ��Դ��Ƶ�Ԫ֮��ĶԳ��ԡ�ͬʱ����ʹ��sigmoid�����ʱ������ʼȨ�ع���sigmoid������ͣ����µ�ԪʧЧ������Ȩ�ع�С���ݶȽ����С��
- ���þ��ȷֲ�����ʼ��Ȩ�ظ��ã�ӵ�и����������ӵĵ�ԪӦ������Խ�С��Ȩ�ء�

## ѧϰ����
- ����Ҫ�ĳ�����֮һ�����ʹ�С�ᵼ�������������ʹ���ᵼ����ʧ����ͨ������Ϊ0.01��
- ѧϰ����Ҳ������Ϊ������ͨ�������ÿ�ε��������ʼ��롣
- ���ڶ����ķ������Ը��������������ı�ѧϰ���ʣ�ͬʱҲ�������ģ���еĲ�ͬ�������ò�ͬ�����ʡ�
- ����Ӧѧϰ���ʣ���Adagrad��Adam�������Զ�����ѧϰ���ʡ�

## ѧϰ����
- ��DNN������ݶ��½�Ч�����ܲ��ã��ɲ���Adagrad��Adam��AdaDelta��RMSProp�ȣ������ṩ����Ӧѧϰ���ʣ���Щ����ͬʱΪ��ͬģ�Ͳ����ṩ��ͬ���ʣ�����������

## ��Ȩ��ά������Ϊ2��ָ��
- ��Ȩ�ز�������Ϊ2��ָ������64,128,1024�ȣ������ھ����Ȩ�صȷ��������ѧϰЧ�ʣ���GPU��ѵ��ģ��ʱЧ����������

## С���������ѧϰ
- �������ѧϰ����ʱ��Ȩ���ݶ���ÿ��ѵ����������и��£��������ݶ���������Ԥ������ϣ�ͬʱ�ᵼ������������
- ����ʹ��С����ѧϰ��ѡ����ʴ�С�������������Ա�֤����������ͬʱ��߼���Ч�ʡ�ͨ������16-128������Ϊһ��С������

## ����ѵ������
- ���Ӳ�̫���ܷ������¼���ѧϰ�ȴӳ����¼���ѧϰЧ�ʸ��ߡ�����ѵ�������Ĵ�����������������
- *��DQN�У��Ӿ���������������ɴ�������֮�����ϵ��*

## Dropout����
- ����dropout������L1/L2�ɱ������ϣ�ͬʱ�ɼ���ѧϰ���ʣ�ͨ������0.5�����ģ�ͽϼ򵥿ɲ���0.2����ϸ�μ�[ԭ��](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)��

## �Ӿ����
- ��ѵ��������ͼ������������bug������ʧ��ѵ�����Ͳ������ȡ�
- ����Ȩ���ڲ�ͬѵ������������ϵ�ֱ��ͼ�����㶨λ���⣬���ݶ���ʧ���ݶȱ�ը�ȡ�

## ��˼��������GPU
- ���CPU�Ͷ�GPU����������ѵ��

## ʹ��֧��GPU���Զ�΢�ֵĿ�
- [Theano](http://deeplearning.net/software/theano/)��[Tensorflow](https://www.tensorflow.org/)��[Keras](https://keras.io/)��DL�ⶼ�ṩGPU������Զ�΢��֧�֣�Tensorflowͬʱ֧�ֲַ�ʽ�ܹ���

## �ο�����
1.[Efficient BackProp(Yann LeCun et al.)](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

2.[Practical Recommendations for Deep Architectures(Yoshua Bengio)](https://arxiv.org/pdf/1206.5533v2.pdf)

3.[Understanding the difficulty of training deep feedforward neural networks(Glorot and Bengio, 2010)](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf)

4.[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

5.[Andrej Karpathy - Yes you should understand backprop(Medium)](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b#.yd17cx8ml)
