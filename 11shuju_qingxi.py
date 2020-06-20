import pandas as pd

df=pd.Dataframe()
#--------1.完整性------
#缺失值
df['Age'].fillna(df['Age'].mean(), inplace=True)

age_maxf = train_features['Age'].value_counts().index[0]
train_features['Age'].fillna(age_maxf, inplace=True)
#空行

# 删除全空的行
df.dropna(how='all',inplace=True) 

#------2.全面性-------

# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
# 将 lbs转换为 kgs, 2.2lbs=1kgs
for i,lbs_row in df[rows_with_lbs].iterrows():
  # 截取从头开始到倒数第三个字符之前，即去掉lbs。
  weight = int(float(lbs_row['weight'][:-3])/2.2)
  df.at[i,'weight'] = '{}kgs'.format(weight) 

#-----3.合理性------

# 删除非 ASCII 字符
df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
df['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)


#------4.唯一性----

#一列多参数
# 切分名字，删除源数据列
df[['first_name','last_name']] = df['name'].str.split(expand=True)
df.drop('name', axis=1, inplace=True)

#重复数据

# 删除重复数据行
df.drop_duplicates(['first_name','last_name'],inplace=True)