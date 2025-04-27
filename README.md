# 金融 AI 编程实战

> ### 曾用名：金融计算机语言、金融编程与计算、金融数据库

> 持续建设中，欢迎参与添砖加瓦🌹

<p align="center">
<img src="images/cueb-ftlab-courses-qr-code.jpg" alt="扫二维码" width=200 />
</br>
(扫二维码，在 手机端📱 进入
<a href="#教学大纲">教学大纲</a>
观看录播，在 电脑端💻 敲键盘完成操作任务)
</p>

## 常见问题

1. **现在各种大模型 (比如 DeepSeek) 已经能替我编程 (比如 Python) 了，网上也能找到许多现成代码，我没学过计算机 (非科班)，我只是想在自己的电脑 (PC 或 Mac) 上运行出结果 (或许稍微改一改)，这门课适合我吗？看大纲好像很复杂，能不能教得简单直接些？**

    同学你好，这门课完全适合你，可以说就是为你这种需求量身定制的。观看 **第 1～4 周 (初级)** 的录播并亲手操作一遍，就可以让你达到目的了。

    如果 4 周学习仍然令你感到痛苦，那么我猜你想要的可能是：给你个链接，下载双击 `exe`，一路下一步，安装完毕，双击打开，复制粘贴代码，点击运行，就能看到结果。但事情并不是这么简单：

    - 第一，你想象的是 Word、Excel 之类的软件，其特点是集成 (类似于 “全家桶”，你用得到/用不到的功能都有，都相互兼容)、图形界面 (看菜单点鼠标就行，不需要学习)，但 Python 是由 *许多* 开源社区 (而不是某一家大公司) 共同建设起来的开放生态体系，存在着碎片化、多版本、兼容性等问题 (类似于 “乐高积木”，你得阅读说明书才能玩，而且相当费时间)。集成图形界面 (“全家桶”) 其实也是有的，下载安装 [Anaconda](https://www.anaconda.com/download/success) 就可以，她就好比是 Python 界的 Microsoft，[第 1 周 (初级)](https://gitcode.com/cueb-fintech/courses/blob/main/01-beginner/01.tutorial.md) 教你的就是这。
    - 第二，你以为安装了 Anaconda 复制粘贴代码就能运行了？不。很多代码需要访问 (读/写) 数据文件 (如果一段代码不读/写你的文件，只是在内存里运行，那基本上没什么用)，如果不能把 “路径” 改对，代码运行就会报错 `FileNotFoundError`。要写对 “路径”，就需要知道计算机文件系统方面的一些必要的基础知识，[第 2 周 (初级)](https://gitcode.com/cueb-fintech/courses/blob/main/01-beginner/02.tutorial.md) 教你的就是这。
    - 第三，运行复制粘贴来的代码还会经常遇到 `ModuleNotFoundError`，意思是你的 “生产车间” 里仍缺少某个 “机床” 或 “零件”，无法开动。不是说 Anaconda 已经提供 “全家桶” 了吗？是也不是。因为 Python 生态实在太大了，第三方软件包实在太多了，Anaconda 确实囊括了非常多的常用软件包，但不可能把整个 Python 生态全部装进你的电脑，更何况 Python 生态每天都在诞生新物种，百花齐放，物竞天择，根本不是 Anaconda 公司能够集成的。所以 “全家桶” 是靠不住的，你终究还是需要配置搭建你自己的 Conda 环境。[第 3 周 (初级)](https://gitcode.com/cueb-fintech/courses/blob/main/01-beginner/03.tutorial.md) 教你的就是这。
    - 第四，复制粘贴运行后，仍然报告你看不懂的错误该怎么办？放弃吗？改，本来就看不太懂代码，是大模型生成的，该怎么改？让大模型改？改完还是报错怎么办？更危险的是，就算程序没报错，运行完毕了，结果输出了，你怎么知道结果是对的还是中间有出错？大模型幻觉是无法避免的，大模型生成的代码是一定要经过审查和测试的。所以，我们必须知道一些最基本的程序开发知识，要能够大致看得懂 Python 代码，要掌握调试 (debug) 技能，能够检查代码运行时的内部状态是否符合我们的预期 —— 这样才能自己改代码。[第 4 周 (初级)](https://gitcode.com/cueb-fintech/courses/blob/main/01-beginner/04.tutorial.md) 教你的就是这。

    可以看到，这门课的设计本身就是尽可能简单直接的。不像其他课程，你可能需要选修很多，才能开始 (或一直无法？) 实践/实战；我们的课 **综合凝练** 了各方面的知识，致力于帮助任何新人，经过最简单直接的学习培训，在最短的时间内拥有 **实践/实战** 能力。

1. **打卡交作业居然还要用 Git 操作，至于搞这么复杂吗？我不做行吗？我就看看录播不行吗？**

    你只能通过游泳学会游泳。只观看不实践就纯粹是浪费时间。Python 是由许多开源社区共同建设起来的，所谓社区 (community) 就是围绕着各种 Git 仓库在做贡献的一群人。Git 的意义不仅是提供了版本管理，更重要的是让人们的贡献留痕，让人们可以拥有自己创造的知识的产权 (而未必是要申请著作权或专利)。我们得益于社区要靠 Git (下载/学习别人的代码)，我们向社区提交贡献更是要靠 Git (上传/分享自己的代码)。只有通过 **练习** 学会 **贡献**，才能真正融入社区，成为社区中的一员。说不定，这就是未来数字社会最基本的生存/生产方式呢。

    通过 Git 提交作业并量化评分，正是我们课程的 **特色亮点**，欢迎尝试🌹

## 课程说明

技术飞速进步，信息爆炸。互联网、大模型已随手可及，知识获取已变得前所未有地便捷。所以，我们的最新课程把 **任务**、**行动**、**考核** 放在首位，要求学生在观摩演示的基础上，能够尝试独立解决遇到的问题，按需自学，自我教育，每周完成任务，把学习过程以 “笔记 + 截图” 的形式做成 PDF 报告 (最低要求)，提交以供考核。希望这种督促 “行动” 的教学能够切实提升同学们的技能，实现更好的教育。

<p align="center"><img src="images/teaching.drawio.svg" alt="Teaching Way" /></p>

在考察评估多种可选方案的基础上，我们目前决定在国内的 `GitCode` 平台上托管我们的 [课程资料](https://gitcode.com/cueb-fintech/courses)。对应每一个教学周 (共 16 周)，我们都建立了一个代码仓库，通过 PR (Pull Requests) 机制来接收同学们提交的 PDF 报告 (但不合并)。通过这种开源代码平台协作的方式，我们师生的 “行动” 都在平台上公开记录，并可以借助平台提供的 [GitCode API](https://docs.gitcode.com/docs/apis) 功能，以编程的方式把 “行动” 数据下载存储到本地，进而自动计分、呈现报表，甚至还可以利用 AI 辅助评阅，减轻教师负担。

<p align="center"><img src="images/working.drawio.svg" alt="Working Way" /></p>

## 教学大纲

教学设计有两个维度：一是技术专题，二是技术深度。每周一个专题，是教学进度强制要求的，但每周的技术深度允许同学根据自己的情况选择。

|周次|专题|学习报告提交|任务/教程/录播/参考资料|
|:--:|---|:----:|:------:|
|1|准备开发环境|[仓库](https://gitcode.com/cueb-fintech/week01/pulls)|[初级](01-beginner/01.tutorial.md) · [中级]() · [高级]()|
|2|命令行与文件系统|[仓库](https://gitcode.com/cueb-fintech/week02/pulls)|[初级](01-beginner/02.tutorial.md) · [中级]() · [高级]()|
|3|Python 项目|[仓库](https://gitcode.com/cueb-fintech/week03/pulls)|[初级](01-beginner/03.tutorial.md) · [中级]() · [高级]()|
|4|Python 程序开发|[仓库](https://gitcode.com/cueb-fintech/week04/pulls)|[初级](01-beginner/04.tutorial.md) · [中级]() · [高级]()|
|5|Python 对象类型|[仓库](https://gitcode.com/cueb-fintech/week05/pulls)|[初级](01-beginner/05.tutorial.md) · [中级]() · [高级]()|
|6|Python 代码组织|[仓库](https://gitcode.com/cueb-fintech/week06/pulls)|[初级](01-beginner/06.tutorial.md) · [中级]() · [高级]()|
|7|数据可视化与交互|[仓库](https://gitcode.com/cueb-fintech/week07/pulls)|[初级](01-beginner/07.tutorial.md) · [中级]() · [高级]()|
|8|数据清洗与计算|[仓库](https://gitcode.com/cueb-fintech/week08/pulls)|[初级](01-beginner/08.tutorial.md) · [中级]() · [高级]()|
|9|网页爬取文本图片|[仓库](https://gitcode.com/cueb-fintech/week09/pulls)|[初级](01-beginner/09.tutorial.md) · [中级]() · [高级]()|
|10|调用 HTTP API|[仓库](https://gitcode.com/cueb-fintech/week10/pulls)|[初级](01-beginner/10.tutorial.md) · [中级]() · [高级]()|
|11|SQL 数据库的连接与查询|[仓库](https://gitcode.com/cueb-fintech/week11/pulls)|[初级](01-beginner/11.tutorial.md) · [中级]() · [高级]()|
|12|SQL 数据库的创建与写入|[仓库](https://gitcode.com/cueb-fintech/week12/pulls)|[初级](01-beginner/12.tutorial.md) · [中级]() · [高级]()|
|13|编写 Web App|[仓库](https://gitcode.com/cueb-fintech/week13/pulls)|[初级](01-beginner/13.tutorial.md) · [中级]() · [高级]()|
|14|回归分析应用|[仓库](https://gitcode.com/cueb-fintech/week14/pulls)|[初级](01-beginner/14.tutorial.md) · [中级]() · [高级]()|
|15|机器学习应用|[仓库](https://gitcode.com/cueb-fintech/week15/pulls)|[初级](01-beginner/15.tutorial.md) · [中级]() · [高级]()|
|16|大模型应用|[仓库](https://gitcode.com/cueb-fintech/week16/pulls)|[初级](01-beginner/16.tutorial.md) · [中级]() · [高级]()|

## 参与贡献

**对社会 (比如开源项目) 做出贡献才是有效果的学习**。而且这种行动是留痕的，是能够得到社会认可的 (比如招聘时)。但很多学生很难 (甚至一直不能) 做到从 **学习** 到 **贡献** 的跨越，所以我们设计了从易到难、从强制到可选的多种贡献方式，帮助学生突破自我。

- (必选，较容易) 向每周仓库提交 **学习报告**，内容自由，不要有任何顾虑，能提交就好，可以多次提交，只要不作弊 (因为仓库是公开的，所以 _不要实名_)
- (可选，最容易) 在课程仓库的 [**讨论区**](https://gitcode.com/cueb-fintech/courses/discussion) 发帖/回帖，欢迎提问 (提问规范可以参考: [CSDN](https://bbs.csdn.net/topics/603291003)、[StackOverflow](https://stackoverflow.com/help/how-to-ask))，欢迎互助，只要是与课程学习相关的内容都可以发，但要注意保护隐私
- (可选，较容易) 在课程仓库的 [**Issues 区**](https://gitcode.com/cueb-fintech/courses/issues) 报告问题，从书写错误 (typo)、链接失效，到内容过时、改进建议等等，都可以报告，也可以参与回复和讨论，报告的问题会得到解决 (解决后问题会关闭)
- (可选，最有价值) 向课程仓库 (注意不是每周打卡仓库) 发起 PR (Pull Requests) 提交贡献代码，帮助改正错误、增加内容等等 (有益的贡献会被合并进仓库)

## 从这里开始

金融等财经背景的学生，要同时成为面向未来的软件开发人员 (数据工程师、数据分析师、数据科学家、数据决策者、量化投资人)，还有很长的路要走。只上一个学期的课，根本是不够的，这仅仅只是开始。只输入、只学习，根本是不够的，要积累经验，要做事，要输出。世界上的开源项目有很多很多，但对于不知从哪里来的初学者，未必都那么友好。但至少，这里可以成为我们自己的家。我们有足够的权限，我们可以模拟开源社区的一切，我们对同学们的行为尽可能地开放和包容 (只要不违法)，我们保留一切客观记录，同学们在这里留下的一切 (比如作业、展示、问答、尤其是贡献) 我们都可以用 **学院官方** 的身份提供背书和认证。
