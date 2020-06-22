# 系统资源管理
import resource

import os

# 资源限制
def resource_setrlimit_nofile():
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)  # 获得可打开文件数量的软硬限制
    print('soft starts as :', soft)
    print('hard starts as :', hard)

    resource.setrlimit(resource.RLIMIT_NOFILE, (4,hard))
    file_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
    print('soft limit change to :', file_limit[0])


if __name__ == "__main__":
    resource_setrlimit_nofile()