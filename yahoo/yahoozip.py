import zipfile
import os
#input_names="샤워커튼,쉬폰90125,아치형액자,쿠션,그래픽도어"
input_names="+2022 봄"
for input_name in input_names.split(","):
    print(input_name)
    input_output_root_path="\\\\sangsanghoo1\\일본\\+++상품\\++yahoo\\쿠션\\"
    input_path=input_output_root_path+input_name+"\\썸네일_output"
    input_path_common=input_output_root_path+input_name+"\\썸네일_공통_output"
    output=input_output_root_path+input_name+"\\썸네일_ZIP"
    if not os.path.isdir(output):
        os.mkdir(output)
    onlyfiles=[os.path.join(input_path,f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path,f))]
    onlyfiles+=[os.path.join(input_path_common,f) for f in os.listdir(input_path_common) if os.path.isfile(os.path.join(input_path_common,f))]
    maxsize = 1024*1024*20
    maxfilenum=len(onlyfiles)
    curfilenum=0
    cnt=1
    notwhlieend=True
    while notwhlieend:
        zipf=zipfile.ZipFile(output+"\\"+str(cnt)+'.zip','w')
        zipcnt=0
        for i in range(curfilenum,maxfilenum):
            zipf.write(onlyfiles[i],os.path.basename(onlyfiles[i]), compress_type=zipfile.ZIP_DEFLATED)
            size = os.path.getsize(output+"\\"+str(cnt)+'.zip')
            zipcnt+=1
            if size>=maxsize:
                print(output+"\\"+str(cnt)+'.zip',size/1024/1024,zipcnt)
                curfilenum=i+1
                break
            if i+1==maxfilenum:
                print(output+"\\"+str(cnt)+'.zip',size/1024/1024,zipcnt)
                notwhlieend=False
                break
        cnt+=1