# About SIFT&ORB

源代码见main.py，项目内容及结果如下。

## 图像匹配

基于以下特征，实现两幅相似图像匹配，提交源码

- SIFT
- ORB

## 帮助

```shell
./sift.py -h
SIFT.

Use SIFT to match two pictures.

usage: sift.py [-hV] [-r <ratio>] [-o <output>] <image1> <image2>

options:
    -h, --help                  Show this screen.
    -V, --version               Show version.
    -r, --ratio <ratio>         Lowes ratio. [default: 0.5]
    -o, --output <output>       Output to an image file.
    -n, --dry-run               Without an image in a window.
    
./sift.py -ofigures/sift.pngfigures/input0.png figures/input1.png
# A window will be opened with an image file saved.
# It takes about 753.301 seconds in my PC. (Intel i9-13900H)
./sift.py -nofigures/sift.png figures/input0.png figures/input1.png
# No window will be opened, but an image file will be saved.
```

## 结果展示

根据资料, Lowe推荐ratio的阈值为0.8, 但经过多次尝试, 结果表明
ratio 取值在0.4~0.6之间最佳, 小于0.4的很少有匹配点, 大于0.6的存在大量错误匹配点。

因此代码中分别尝试运行了三种模式:
more-tolerant: ratio = 0.6;
default: ratio =0.5;
more-extreme: ratio = 0.4

最终结果如下图所示：

<procedure title="生成图像" id="sift">
    <step>
        <p>ratio = 0.4 :</p>
        <img src="match_e.png" alt="more tolerant" border-effect='line'/>
        <p>严格的筛选阈值，可以看到匹配的特征较稀疏，但非常准确</p>
    </step>
    <step>
        <p>ratio = 0.5 :</p>
        <img src="match_d.png" alt="default" border-effect='line'/>
        <p>默认的筛选阈值，特征数量多且准确率高</p>
    </step>
    <step>
        <p>ratio = 0.6 :</p>
        <img src="match_t.png" alt="default" border-effect='line'/>
        <p>宽松的筛选阈值，特征数量非常多但出现了少量错误匹配</p>
    </step>
</procedure>
