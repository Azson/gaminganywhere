
data_file = "bin/run_5_31.log"
data = [[], [], []]
columns = ["audio", "video", "control"]

with open(data_file, 'r') as f:
    for line in f.readlines():
        tmp = line.split(' ')
        # print(tmp)
        col = None
        if "audio frame copy" in line:
            col = 0
        elif "encoder pkt" in line:
            col = 1
        elif "ubuntu sdl1 ctl msg size" in line:
            col = 2
        if col != None:
            data[col].append([tmp[2], tmp[-1]])
# print(data[0])
for col in range(3):
    pre_time = None
    with open("%s.csv" % (columns[col]), 'w') as f:
        for line in data[col]:
            if pre_time == None:
                pre_time = float(line[0])
            # tmp = float(line[0])
            line[0] = str(float(line[0]) - pre_time)
            # pre_time = tmp
            f.write(','.join(line))