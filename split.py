from pydub import AudioSegment

def FileRead(file_name,format):
    List=[]
    with open(file_name,'r', encoding="utf8") as f:
        for i in f.readlines():
            if format=="start":
                time = i[:-1].split(' ')[0]
                name = i[len(i[:-1].split(' ')[0]):-1].strip().strip('-').strip()
                List.append((TimeParse(time),name))
            elif format=="end":
                time = i[:-1].split(' ')[-1]
                name = i[:len(i[:-1].split(' ')[-1])].strip().strip('-').strip()
                List.append((TimeParse(time),name))

    return List


def TimeParse(time):
    split=time.split(":")
    if len(time.split(":")) == 3:
        return int(ToNormal(split[0]))*60*60*1000+int(ToNormal(split[1]))*60*1000+int(ToNormal(split[2]))*1000
    elif len(time.split(":")) == 2:
        return int(ToNormal(split[0]))*60*1000+int(ToNormal(split[1]))*1000
    else:
        exit("Timestamp is flawed")

def ToNormal(string):
    if string[0]=="0":
        string=string[-1]
    return string

def Cut(song,startTime,endTime,track_name):
    extract = song[startTime:endTime]
    extract.export( track_name+'.mp3', format="mp3")

def main(timestamps,file_name):
    read = FileRead(timestamps,"start")
    for i in range(len(read)):
        if i==len(read)-1:
            Cut(file_name,read[i][0],None,read[i][1])
        else:
            Cut(file_name,read[i][0],read[i+1][0],read[i][1])

def Song(file_name):
    return AudioSegment.from_mp3( file_name )

if __name__ == '__main__':
    song=Song('song.mp3')
    main('timestamps.txt',song)