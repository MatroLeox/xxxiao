# 左右消消消求解

## 介绍
这是一个左右消消消游戏（微信小程序）的求解命令行程序。
这款游戏有12行9列，玩家通过左右移动方块，使一行被方块占满，使得此行被消除，当棋盘超过12行，游戏结束，类似俄罗斯方块。

我用正数代表方块，负数代表空缺的位置，来进行命令行输入；举个例子，如果一个行中，第一个空2列，第二个是长为3的方块，第三个空1列，第四个长为2的方块，第五个空1列；那么就是：

```
-2 3 -1 2 -1
```

图形类似：

```
    ▤▤▤  ▥▥  
```

## 用法

在命令行在执行`python xxxiao_solve.py`，进入初始化行输入。

### 1. 输入初始化行

进入初始化行输入，会像这样显示：

```
init> 
```

以下图为例：

![左右消消消图例](x.jpg)

输入初始化行则为：
```
init> 2 -3 3 1
init> 1 -2 2 1 -1 2
init> ^C
▤▤      ▥▥▥▧
▤    ▥▥▧  ▨▨

xxxiao> 
```

注意：从上往下依次输入，以`Ctrl`+`C`结束初始化。

### 2. 输入预置行进行求解

这个游戏会一直会提示下一个出现的行（最底行下灰色间断的线），所以要进行求解，则要输入这个预置行。

再以图片为例：

![左右消消消图例](x.jpg)

输入预置行进行求解则为：

```
xxxiao> 1 -2 1 3 2
 1: 第 1行，第 4列，移-2下，可消1层，再移可消0层，共消1层
 2: 第 2行，第 1列，移 1下，可消1层，再移可消0层，共消1层
 3: 第 1行，第 4列，移-1下，可消0层，再移可消1层，共消1层
 4: 第 1行，第 6列，移 1下，可消0层，再移可消1层，共消1层
 5: 第 1行，第 8列，移-1下，可消0层，再移可消1层，共消1层
 6: 第 2行，第 1列，移 2下，可消0层，再移可消1层，共消1层
 7: 第 2行，第 1列，移 3下，可消0层，再移可消1层，共消1层
 8: 第 2行，第 6列，移-1下，可消0层，再移可消1层，共消1层
 9: 第 2行，第 6列，移-2下，可消0层，再移可消1层，共消1层
10: 第 2行，第 6列，移-3下，可消0层，再移可消1层，共消1层
move>
```

### 3. 有解与无解

当有多个解时，则会类似这样显示：

```
 1: 第 1行，第 4列，移-2下，可消1层，再移可消0层，共消1层
 2: 第 2行，第 1列，移 1下，可消1层，再移可消0层，共消1层
 3: 第 1行，第 4列，移-1下，可消0层，再移可消1层，共消1层
 4: 第 1行，第 6列，移 1下，可消0层，再移可消1层，共消1层
 5: 第 1行，第 8列，移-1下，可消0层，再移可消1层，共消1层
 6: 第 2行，第 1列，移 2下，可消0层，再移可消1层，共消1层
 7: 第 2行，第 1列，移 3下，可消0层，再移可消1层，共消1层
 8: 第 2行，第 6列，移-1下，可消0层，再移可消1层，共消1层
 9: 第 2行，第 6列，移-2下，可消0层，再移可消1层，共消1层
10: 第 2行，第 6列，移-3下，可消0层，再移可消1层，共消1层
```

而你则只须要输入开头的编号，继续求解，比如想用第一种，则：

```
move> 1
```

当无解时，只会提示`move> `，则要按格式输入，第几行，第几列，移动几下（负数左移，正数右移），举个例子，若你要第1行，第4列，向左移2下，则为：

```
move> 1 4 -2
```

### 4. 其它

#### 1. 替换行

替换第1行为`3 3 -3`

```
xxxiao> x 1 3 3 -3
```

#### 2. 插入行

插入第1行为`3 3 -3`

```
xxxiao> i 1 3 3 -3
```

#### 3. 删除行

删除第1行

```
xxxiao> d 1
```