cpu, memory, disk, temperature = map(int, input().split())

if temperature > 90 or (cpu > 95 and memory > 95 and disk > 95):
    print("Shut Down")

elif ((cpu > 85 and memory > 85) or
      (cpu > 85 and disk > 85) or
      (memory > 85 and disk > 85) or
      temperature > 80):
    print("Restart")

elif cpu > 75 or memory > 75 or disk > 75:
    print("Warning")

else:
    print("Stable")