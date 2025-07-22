#!/bin/bash

#pip install conan
#conan remote add myremote https://api.bintray.com/conan/myuser/myrepo

# 构建项目
gn gen out/debug
ninja -C out/debug

# Conan 打包和上传
if [ "$1" == "upload" ]; then
    # 创建 Conan 包
    conan create .
    
    # 上传到远程仓库
    conan upload hello/1.0.0 -r myremote --all
fi
