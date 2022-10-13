import os
import xlwings as xw


def batch_change_file_content(count=1):
    path = r"views"
    files = os.listdir(path)
    for filename in files:
        cur_path = os.path.join(path, filename)
        if os.path.isdir(cur_path):
            cur_dirs = os.listdir(cur_path)
            for cur_dir in cur_dirs:
                cur_full_dir = os.path.join(cur_path, cur_dir)
                if os.path.isdir(cur_full_dir):
                    the_files = os.listdir(cur_full_dir)
                    for the_file in the_files:
                        file_path = os.path.join(cur_full_dir, the_file)
                        if the_file == "dataview.jsp":
                            count = alter(file_path, "执行董事", "董事长", count)
                        # fi = open(os.path.join(cur_full_dir, the_file), "w")
                        elif the_file.find(".xls") > -1:
                            count = alter_excel(file_path, "执行董事", "董事长", count)


def alter(file, old_str, new_str, count):
    """
    替换文件中的字符串
    :param count: 统计
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:

    """
    file_data = ""
    is_need_change = False
    with open(file, "r", encoding="gbk") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
                is_need_change = True
            file_data += line
    if is_need_change is True:
        print(str(count) + "：" + file)
        count += 1
        with open(file, "w", encoding="gbk") as f:
            f.write(file_data)
    return count


def alter_excel(file, old_str, new_str, count):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(file)
    is_need_change = False
    for sheet in wb.sheets:
        # print(sheet.used_range.shape)
        row, col = sheet.used_range.shape
        # 此方法难以定位单元格，难以修改值并保存
        # print(sheet.range((1, 1), sheet.used_range.shape).value)
        # if sheet.used_range.shape != (1, 1):
        #     for values in sheet.range((1, 1), sheet.used_range.shape).value:
        #         for index, value in enumerate(values):
        #             if type(value) == str and value.find(old_str) > -1:
        #                 values[index] = value.replace(old_str, new_str)
        #                 is_need_change = True
        #                 print("修改的文件路径：" + file)
        #                 print(values)
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                value = sheet.range(i, j).value
                if type(value) == str and value.find(old_str) > -1 and value.find("$Audit." + old_str) == -1:
                    sheet.range(i, j).value = value.replace(old_str, new_str)
                    is_need_change = True
                    print(str(count) + "：" + file)
                    count += 1
                    # print(sheet.range(i, j).value)
    if is_need_change is True:
        wb.save()
    wb.close()
    app.quit()
    return count


# for cell in sheet.range((1, 1), sheet.used_range.shape):
#     print(cell)


if __name__ == '__main__':
    batch_change_file_content()
