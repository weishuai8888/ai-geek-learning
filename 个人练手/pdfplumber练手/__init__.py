import pdfplumber
import pandas as pd


# 加载PDF文件
def get_pdf():
    # open方法将返回一个pdfplumber.PDF类的实例
    pdf = pdfplumber.open("The_Old_Man_of_the_Sea.pdf")

    # 一个由PDF的 Info 尾部信息中的元数据键/值对组成的字典。通常包括 "CreationDate," "ModDate," "Producer," 等等。
    print(pdf.metadata)

    # 包含每个已加载页面的 pdfplumber练手.Page 实例的列表。
    pdfpages = pdf.pages
    print(pdfpages)

    # 获取pdfplumber.Page类，pdfplumber练手.Page 类是 pdfplumber练手 的核心，表示PDF文件中一页单独的内容。
    print(type(pdfpages[0]))

    # 顺序页码，从第一页开始为 1，第二页为 2，以此类推。
    num0 = pdfpages[0].page_number
    print(num0)

    # 页面的宽度。页面的高度。
    print(pdfpages[0].width, pdfpages[0].height)

    # 可视化第一页（在PyCharm中不能够可视化展示）
    pdfpages[0].to_image()
    # 可视化第二页（在PyCharm中不能够可视化展示）
    pdfpages[1].to_image()

    # 获取单页的文本
    p1_text = pdfpages[1].extract_text()
    print(p1_text)

    p1_text = pdfpages[1].extract_text(layout=True)
    print(p1_text)


# 提取单页表格
def get_table():
    pdf = pdfplumber.open("test.pdf")
    pages = pdf.pages
    # 获取单页表格。返回从页面上 最大 的表格中提取的文本。表示为一个列表的列表，结构为 row -> cell。
    p1_table = pages[0].extract_table()
    print(p1_table)

    # 获取单页所有表格。返回从页面上找到的 所有 表格中提取的文本，表示为一个列表的列表的列表，结构为 table -> row -> cell。
    tables = pages[0].extract_tables()
    print(tables)
    print(len(tables))

    # 返回 TableFinder 类的一个实例，可以访问 .edges，.intersections，.cells，和 .tables 属性
    p1_debug_table = pages[0].debug_tablefinder()
    print(type(p1_debug_table))
    print(p1_debug_table.tables)

    # 使用Pandas.DataFrame来展示和存储表格
    df = pd.DataFrame(p1_table[1:], columns=p1_table[0])
    print(df)

    # 可视化第一页（在PyCharm中不能够可视化展示）
    pages[0].to_image()

    # 从PageImage中获取页面图像分辨率
    print(pages[1].images)

    img = pages[1].images[0]
    print(img)
    # 裁剪第二页
    bbox = (img["x0"], img["top"], img["x1"], img["bottom"])
    cropped_page = pages[1].crop(bbox)
    # 可视化展示裁剪后的第二页
    cropped_page.to_image()
    # 可视化展示裁剪后的第二页 + 抗锯齿
    cropped_page.to_image(antialias=True)
    # 可视化展示裁剪后的第二页 + 1080P
    cropped_page.to_image(resolution=1080)
    # 可视化展示裁剪后的第二页 + 抗锯齿，并保存
    im = cropped_page.to_image(antialias=True)
    im.save("pdf_image_test.png")


if __name__ == '__main__':
    get_pdf()
    get_table()
