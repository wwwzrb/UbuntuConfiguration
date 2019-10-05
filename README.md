# SSR Client Configuration
This tutorial present the usage of SSR client under Ubuntu 18.04!

１. Install Python Client.

    git clone -b manyuser https://github.com/shadowsocksr-backup/shadowsocksr.git

    执行完毕后会在当前目录新建一个shadowsocksr目录。

    参考链接:　https://github.com/shadowsocksr-backup/shadowsocks-rss/wiki/Python-client-setup-(Mult-language)

２. Build Executable Script.

    (1). 桌面新建run_ssr.sh, 内容如下:

    #!/bin/bash

    cd ~/software/shadowsocksr/shadowsocks

    sudo python local.py -c ~/software/shadowsocksr/shadowsocks/shadowsocks.json -d start

    简单解释下脚本功能：
    脚本首先切换到SSR安装目录(示例均为绝对路径)；
    然后在SSR安装目录下运行相应的配置文件(包含网络端口，加密，混淆等信息)；
    只需根据自己的实际路径更改上述脚本中的路径即可。

    (2). 桌面新建stop_ssr.sh, 内容如下:

    #!/bin/bash

    cd ~/software/shadowsocksr/shadowsocks

    sudo python local.py -c ~/software/shadowsocksr/shadowsocks/shadowsocks.json -d stop

    (3). 切换到脚本文件所在目录, 使用脚本

    sudo ./run_ssr.sh 启用代理

    sudo ./stop_ssr.sh 关闭代理

３. Add Proxy Agent in Explorer.

    (1). SwitchOmega for Chrome.
![avatar](https://github.com/wwwzrb/UbuntuConfiguration/blob/SSRConfig/ChromeSwitchOmega.png)

    (2). Firefox.
    注意Firefox配置代理后可能会导致无法访问https网页，可以尝试把手动代理关闭，然后重启浏览器再次打开手动代理!
![avatar](https://github.com/wwwzrb/UbuntuConfiguration/blob/SSRConfig/FirefoxProxy.png)

４．Generate shadowsocks.json

    运行代理服务需要可用的服务器和网络端口，这些信息都可以在shadowsocks.json中以key-value字段的形式保存。
    
    这里给大家提供一份用喵帕(https://xn--i2ru8q2qg.com/user)提供的所有端口配置，
    生成单独配置文件的python脚本(https://github.com/wwwzrb/UbuntuConfiguration/blob/SSRConfig/AutoGenerate.py)。
    
    (1) 首先下载python脚本文件，和喵帕斯提供的gui-config.json文件，放在同一目录下
    
    (2) 在脚本运行目录下新建ShadowsSocksR文件夹
    
    (3) 运行AutoGenerate.py, 在ShadowsSocksR文件夹下生成独立的配置文件
    
        注意如果gui-config.json和指定生成配置文件的目录更改，在python代码中相应更改即可！
    
    (4) 选择需要的配置文件重命名为shadowsocks.json，放到run_ssr.sh指定的配置文件目录下(需包含文件名，参考3中的示例)
    
    (5) 运行run_ssr.sh, 浏览器中配置好代理模式，即可。
 
![avatar](https://github.com/wwwzrb/UbuntuConfiguration/blob/SSRConfig/GenerateConfig.PNG)







