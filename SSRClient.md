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

    脚本首先切换到SSR安装目录(示例均为绝对路径)；然后在SSR安装目录下运行相应的配置文件(包含网络端口，加密，混淆等信息)；只需根据自己的实际路径更改上述脚本中的路径即可。

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



