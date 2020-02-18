# pix2pix
基于GAN的黑白漫画自动上色,使用pix2pix模型
&nbsp;&nbsp;&nbsp;这个项目是很久之前的项目了，由于平时喜欢看漫画，而大多数漫画网站提供的都是黑白漫画，加上当时想做点有趣的东西，所以看了很多github跌跌撞撞的用tensorflow实现了上色，但是当时仅仅会用，而不理解，现在由于要做毕业设计，所以从基本的gan开始看起来，做了pix2pix的分析模型，用Pytorch实现了pix2pix模型，并且在电脑运行了一下，效果还行。<!--more-->
首先看一下pix2pix的生成器。
<img src="https://ae01.alicdn.com/kf/U4e1603c2a442412a99cf5c4ed262f710q.png">
生成器使用了UNET网络结构,相比于普通网络在上采样时会保留原始信息。
<img src="https://ae01.alicdn.com/kf/U2ef8e9047b404cf5863ac3dbc48b2c41G.png">
判别器相比于普通GAN模型使用了patchGAN，即判别器不是仅仅输出待判别的图片的真假，而是输出一个矩阵，最终结果求平均，相当于经“投票”后再判断是真是假。<br>
完整代码见[github](https://github.com/SawabeMaho/pix2pix) <br>
最终结果如下：
5000轮训练后：

<img src="https://ae01.alicdn.com/kf/U9d483aaf125f4e1cb75ec4d1bf2304fcn.png"  title="5000轮"/>
20000轮训练后<br>

<img src="https://ae01.alicdn.com/kf/Uc2c69c19d5ad4a52996bf74ce2e12097m.png"  title="20000轮"/><br>
100000轮训练后<br>

<img src="https://ae01.alicdn.com/kf/U0f97a0ff4d3f4cf2ba3a841181810fb1P.png"  title="100000轮"/>

使用的数据集是基于[danbooru2018](https://www.gwern.net/Danbooru2019#danbooru2018)做了灰度转换拼接。 <br>

原始数据集类型如下：
<img src="https://ae01.alicdn.com/kf/U0b5b0e79e73d4321aca9bb9ee6d3cb39B.png">
做过灰度拼接之后：
<img src="https://ae01.alicdn.com/kf/U0634457ed8b94d64ac13422e5e13a9b0t.png">
