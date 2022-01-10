import logging

from NotionDump.Dump.block import Block
from NotionDump.Notion.Notion import NotionQuery

TOKEN_TEST = "secret_WRLJ9xyEawNxzRhVHVWfciTl9FAyNCd29GMUvr2hQD4"
TABLE_ID = "13b914160ef740dcb64e55c5393762fa"
RER_LIST_ID = "d32db4693409464b9981caec9ef11974"


# 页面表格测试
def test_get_table_block(query):
    block_handle = Block(block_id=TABLE_ID, query_handle=query, export_child_pages=True)
    block_handle.page_to_md()

    # 输出样例
    print("page table test")
    print(block_handle.get_pages_detail())


# 递归列表测试
def test_get_rer_list(query):
    print("page rer list test")
    block_handle = Block(block_id=RER_LIST_ID, query_handle=query, export_child_pages=True)
    block_handle.page_to_md()

    # 输出样例
    print(block_handle.get_pages_detail())


if __name__ == '__main__':
    query_handle = NotionQuery(token=TOKEN_TEST)
    if query_handle is None:
        logging.exception("query handle init error")
        exit(-1)
    # 获取数据库原始数据测试
    test_get_table_block(query_handle)

    # 解析数据库内容测试
    test_get_rer_list(query_handle)
