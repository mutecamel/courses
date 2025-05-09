import my_utils.str_util
from my_utils import file_util
print(my_utils.str_util.str_reverse('331是一个团结友爱的大家庭'))
print(my_utils.str_util.substr('331是一个团结友爱的大家庭',4,7))

file_util.append_to_file("D:/test1.txt","我很爱你的")
file_util.print_file_info("D:/test1.txt")