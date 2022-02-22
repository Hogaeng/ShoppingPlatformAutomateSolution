import pandas as pd
filepath='\\\\sangsanghoo1\\일본\\+++상품\\++yahoo\\5070\\이미지파일명_5070.xlsx'
key="변경전";value="변경후"
mapping={}
mapping_common={}
sheet_names = pd.ExcelFile(filepath).sheet_names
for sheet in sheet_names:
    df=pd.read_excel(filepath,sheet_name=sheet)
    if sheet == "공통":
        print("common")
        for i,e in enumerate(df[key]):
            mapping_common[e]=df[value][i]
    else:
        print(sheet)
        for i,e in enumerate(df[key]):
            mapping[e]=df[value][i]
print(mapping)
print(mapping_common)