from conan import ConanFile
from conan.tools.files import copy
import os

class HelloConan(ConanFile):
    name = "hello"
    version = "1.0.0"
    description = "A simple hello library built with GN"
    
    # 添加选项来控制库类型
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }
    
    # # 设置构建要求
    # build_requires = "gn/latest"
    
    # 导出相关文件
    exports_sources = (
        "BUILD.gn",
        "build/*",
        "include/*",
        "src/*",
        "toolchains/*",
        ".gn",
        "main.cpp"
    )
    
    def build(self):
        # 执行 GN 构建
        self.run("gn gen out/debug")
        self.run("ninja -C out/debug")
    
    def package(self):
        # 复制头文件
        copy(self, "*.h", src=os.path.join(self.source_folder, "include"),
             dst=os.path.join(self.package_folder, "include"))
             
        # 复制静态库
        copy(self, "*.a", src=os.path.join(self.source_folder, "out/debug/lib"),
             dst=os.path.join(self.package_folder, "lib"))
             
        # 复制动态库
        copy(self, "*.so", src=os.path.join(self.source_folder, "out/debug/lib"),
             dst=os.path.join(self.package_folder, "lib"))
    
    def package_info(self):
        self.cpp_info.libs = ["hello"]