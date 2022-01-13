import datetime


#print(datetime.datetime.now())
#2022-01-06 11:33:00.051614  ←now()はこんな感じの出力をする

sampletime = [2022, 1, 12, 20]

# tasktime1 = str(sampletime[0]) + ':' + str(sampletime[1]) + ':' + str(sampletime[2]) + ':' + str(sampletime[3])
# tasktime2 = datetime.datetime.strptime(tasktime1, '%Y:%m:%d:%H').date()
tasktime = datetime.datetime(sampletime[0],sampletime[1],sampletime[2],sampletime[3])
print(tasktime)

