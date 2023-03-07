"""
对比Webstorm设置里CSS属性名顺序和自定义顺序是否有遗漏的属性名

QuainK
2023.03.07
"""

if __name__ == '__main__':
    # webstorm的css顺序的本地文件路径
    webstorm_path = './webstorm.txt'
    # 自定义css顺序的本地文件路径
    template_path = './template.txt'
    # 以字符串只读方式，打开文件
    webstorm_file = open(webstorm_path, mode='r', encoding='utf-8')
    template_file = open(template_path, mode='r', encoding='utf-8')
    # 不管操作哪个文件，都要记得最后执行close方法
    try:
        # 获取字符串流
        webstorm_str = webstorm_file.read()
        template_str = template_file.read()
        # 按行转换成列表
        webstorm_arr = webstorm_str.splitlines()
        template_arr = template_str.splitlines()
        # 遍历列表
        for index, value in enumerate(webstorm_arr):
            # 移除每行首尾空格
            webstorm_arr[index] = value.strip()
        for index, value in enumerate(template_arr):
            # 移除每行首尾空格
            temp_str = value.strip()
            # 更新列表
            template_arr[index] = temp_str
            # 对比模板和Webstorm是否有遗漏
            if webstorm_arr.index(temp_str) > -1:
                template_arr[index] = ''
            # 重复的显示空字符串，比如 ''
            # 遗漏的显示属性名，比如 'font'

        # print(webstorm_arr)
        print(template_arr)
    finally:
        webstorm_file.close()
        template_file.close()
