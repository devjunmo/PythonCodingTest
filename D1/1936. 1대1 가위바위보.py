T = int(input())
print(T)
# def rsp(a, b):
#     if a == 1:
#         if b == 2:
#             return "B"
#         elif b == 3:
#             return "A"

rsp_dict = {(1,2):"B", (1,3):"B", (2,1):"A", (2,3):"B", (3,1):"B", (3,2):"A"}

print(rsp_dict[tuple(T)])