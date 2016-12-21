import io

f = io.open('bangla.txt','wt', encoding='utf-8')

f.write(u"জঙ্গিবাদ নির্মূলে রাজনৈতিক ঐক্য জরুরি")
f.close()

text = io.open('bangla.txt',encoding='utf-8').read()

print(text)

