str_1 = input()
text_box = ["eraser","erase","dreamer","dream"]
for i in range(len(text_box)):
  str_1 = str_1.replace(text_box[i],'').strip()
if str_1 == '':
  print("YES")
else:
  print("NO")