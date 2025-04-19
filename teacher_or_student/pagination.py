# pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyCustomPagination(PageNumberPagination):
    page_size = 20  # 每页显示的数据条数
    page_query_param = 'page'  # 查询参数：页码的参数名
    page_size_query_param = 'page_size'  # 查询参数：每页数量的参数名
    max_page_size = 100  # 每页最大数量

    # 自定义分页响应结构（可选）
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
