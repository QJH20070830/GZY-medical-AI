# 环境自检：运行 python env_check.py
import sys, platform
print("Python:", sys.version.split()[0], "->", sys.executable)
try:
    import numpy, pandas, sklearn, matplotlib
    print("numpy", numpy.__version__, "| pandas", pandas.__version__,
          "| sklearn", sklearn.__version__)
except ImportError as e:
    print("缺少包:", e)
try:
    import torch
    print("torch", torch.__version__, "| CUDA:", torch.cuda.is_available())
except ImportError:
    print("torch 未安装")
try:
    import pydicom, SimpleITK
    print("pydicom", pydicom.__version__, "| SimpleITK", SimpleITK.__version__)
except ImportError:
    print("医学影像包未安装")
