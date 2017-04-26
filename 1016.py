#python3
#1016.程序运行时间
#测试通过
C1_str, C2_str = input().split()
C1 = int(C1_str)
C2 = int(C2_str)
diff = C2 - C1
seconds = int(diff / 100 + 0.5)
print(seconds)
second = seconds % 60
minute = (seconds // 60) % 60
hour = (seconds // 3600) 
print("%d:%d:%d" % (hour, minute, second))