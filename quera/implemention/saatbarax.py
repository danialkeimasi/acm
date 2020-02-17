hour, mi = map(int, input().split())
print(f"{0 if hour == 0 else 12 - hour:02d}:{0 if mi == 0 else 60 - mi:02d}")
