# course_management_project/utils.py



import requests
from django.core.cache import cache
# def get_student(student_id):
#     url = f'http://localhost:8000/permission/search/{student_id}/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None
def get_student(query_params):
    url = 'http://localhost:8000/permission/search'
    response = requests.post(url, json=query_params)
    if response.status_code == 200:
        data = response.json()
        # 确保返回的是一个有效的 student_id
        return data.get('student_id')
    return None

# def get_student(student_id,token):
#     # student_data = cache.get(f"student_{student_id}")
#     # url = f'http://localhost:8000/permission/search/{student_id}/'
#     # if not student_data:
#     #     headers = {'Authorization': f'Bearer {token}'}
#     #     response = requests.get(url, headers=headers)
#     #     if response.status_code == 200:
#     #         student_data = response.json()
#     #         cache.set(f"student_{student_id}", student_data, timeout=3600)  # 缓存1小时
#     #     else:
#     #         raise Exception("Failed to fetch student data")
#     # return student_data
#     pass
def get_teacher(teacher_id):
    url = f'http://127.0.0.1:8000/permission/teachers/{teacher_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        # return response.json()
        return response.json().get('teacher_id')
    return None



# def get_teacher(teacher_id,token):
#     # teacher_data = cache.get(f"teacher_{teacher_id}")
#     # if not teacher_data:
#     #     url = f"http://127.0.0.1:8000/permission/teachers/{teacher_id}/"
#     #     try:
#     #         headers = {'Authorization': f'Bearer {token}'}
#     #         response = requests.get(url, headers=headers)
#     #         response = requests.get(url, timeout=5)
#     #         if response.status_code == 200:
#     #             teacher_data = response.json()
#     #             cache.set(f"teacher_{teacher_id}", teacher_data, timeout=3600)
#     #         else:
#     #             raise Exception(f"Failed to fetch teacher data: {response.status_code}")
#     #     except requests.RequestException as e:
#     #         print(f"Error fetching teacher data: {e}")
#     #         return {"teacher_name": "Unknown Teacher"}
#     # return teacher_data
#     pass
