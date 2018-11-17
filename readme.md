# ST-SOL

## 简介
ST-SOL是一个sublime插件，用于编写Solidity代码，主要是一些代码片段和语法高亮支持。

语法高亮来自于SublimeEthereum插件，还不够完善，有兴趣的朋友可以，修改为YAML格式的，也就是以sublime-syntax结尾的文件。

插件现在只有一个命令，就是创建一个新的合约文件，快捷键ctrl+shift+o,可以在对应系统中的keymap文件中修改。

## 怎样安装
可以把ST-SOL目录直接拷贝到，<sublime安装目录\>/Data/Packages目录中，也可以只将ST-SOL.sublime-package拷贝到<sublime安装目录\>/Data/Install Packages目录中。


## 怎样添加代码片段
直接在ST-SOL目录下的Snippets目录下添加sublime-snippet文件就可以了，格式可以参数已经存在的代码片段。

```
<snippet>
    <content><![CDATA[

assert (${1:address(msg.sender) != 0});

]]></content>
    <tabTrigger>ass</tabTrigger>
    <description>address不为0</description>
    <scope>source.solidity</scope>
</snippet>
```

如上所示，content标签是代码片段，内容位置要注意，`<![CDATA[具体内容]]`。tabTrigger是设置触发条件，description是代码片段说明。对于这个插件scope固定是source.solidity。

***${num：default}是占位符，num是表示光标位置,从1开始，添加完成之后按tab键在这些位置上跳转，default为默认值***
