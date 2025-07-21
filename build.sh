# 安装依赖
sudo apt update
sudo apt install -y python3 git g++ pkg-config ninja-build

# 克隆 GN 仓库
mkdir -p ~/tools && cd ~/tools
git clone https://gn.googlesource.com/gn
cd gn

# 生成 Ninja 构建文件
python3 build/gen.py

# 构建 GN
ninja -C out

# 软链接到系统路径（可选）
sudo ln -sf "$(pwd)/out/gn" /usr/local/bin/gn
