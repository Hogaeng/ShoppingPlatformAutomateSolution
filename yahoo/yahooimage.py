from os import listdir,mkdir,rename
from os.path import isfile,join,isdir
import shutil
import pandas as pd
# input_names을 수정해주세요.
# input_names="샤워커튼,쉬폰90125,아치형액자,쿠션,그래픽도어"
input_names="+2022 봄"
subfolder="기존에추가,명화,대,중,소"
for input_name in input_names.split(","):
    print(input_name)
    input_output_root_path="\\\\sangsanghoo1\\일본\\+++상품\\++yahoo\\쿠션\\"
    input_path=input_output_root_path+input_name+"\\썸네일"
    input_path_common=input_output_root_path+input_name+"\\썸네일_공통"
    output_path=input_path+"_output"
    output_path_common=input_path_common+"_output"
    if not isdir(output_path):
        mkdir(output_path)
    if not isdir(output_path_common):
        mkdir(output_path_common)
    #onlyfiles=[]
    onlyfiles=[join(input_path,f) for f in listdir(input_path) if isfile(join(input_path,f))]
    onlyfiles_common=[join(input_path_common,f) for f in listdir(input_path_common) if isfile(join(input_path_common,f))]
    
    for subfoldername in subfolder.split(","):
        if isdir(input_path+"\\"+subfoldername):
            #onlyfiles=[join(input_path+"\\명화",f) for f in listdir(input_path+"\\명화") if isfile(join(input_path+"\\명화",f))]
            onlyfiles_fimages=[join(input_path+"\\"+subfoldername,f) for f in listdir(input_path+"\\"+subfoldername) if isfile(join(input_path+"\\"+subfoldername,f))]
            onlyfiles+=onlyfiles_fimages
    #filepath=input_output_root_path+input_name+"\\이미지파일명_"+input_name+".xlsx"
    filepath=input_output_root_path+input_name+"\\이미지파일명_쿠션_봄.xlsx"
    key="변경전";value="변경후"
    mapping={}
    mapping_chek={}
    setting=set()
    mapping_common={}
    sheet_names = pd.ExcelFile(filepath).sheet_names

    for sheet in sheet_names:
        df=pd.read_excel(filepath,sheet_name=sheet)
        if sheet == "공통":
            print("common")
            for i,e in enumerate(df[key]):
                mapping_common[e]=df[value][i].replace("\t","")
        else:
            print(sheet)
            for i,e in enumerate(df[key]):
                mapping[e]=df[value][i].replace("\t","")
                mapping_chek[e]=False
                setting.add(mapping[e].split("_")[0])
    for f in onlyfiles_common:
        key=f.split("\\")[-1].split('.')[0]
        if key in mapping_common:
            mmap=mapping_common[key]
            print(mmap)
            for s in setting:
                mmap_num=mmap.split("_")[1]
                mmap.replace("상품번호",s)
                print(f,output_path_common+"\\"+s+"_"+mmap_num+".jpg")
                shutil.copy(f,output_path_common+"\\"+s+"_"+mmap_num+".jpg")
        else:
            print(f)
            shutil.copy(f,output_path_common)
    for f in onlyfiles:
        key=f.split("\\")[-1].split('.')[0]
        if key in mapping:
            mmap=mapping[key]
            print(f,output_path+"\\"+mmap+".jpg")
            shutil.copy(f,output_path+"\\"+mmap+".jpg")
        else:
            print(f)
            shutil.copy(f,output_path)