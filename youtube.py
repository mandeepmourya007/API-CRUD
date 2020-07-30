import csv
from googleapiclient.discovery import build

#  we neeed to install  google-api-python-client    
#  pip install google-api-python-client   


 

def get_video_detail(api_key,_id):
  youtube = build('youtube', 'v3', developerKey=api_key)
  #snippet contain  title desc   etc
  #statitics contain  like dislike views
  #this will return httprequest 
  request = youtube.videos().list(part=['statistics','snippet'],id=_id)

  response = request.execute()
  # here we get dict and   we need snippet and statistics
  data = response['items'][0]
  snippet =data['snippet']
  rows=[]
  #to get title
  rows.append( snippet['title'])
  #to get desc
  # rows.append(snippet['description'])
  print(snippet['description'][2984])
  rows.append('description')
  
   
  statistics=data['statistics']
  # to get views
  rows.append(statistics['viewCount'])
  #to  get likes
  rows.append(statistics['likeCount'])
  #to get dislikes
  rows.append(statistics['dislikeCount'])
  details ={'fields':['title','description', 'viewst','likes','dislikes'],'rows':[rows]}
  # print(rows)
  return details

def save_to_csv(fields,rows,file_name):

  # # writing to csv file  
  
  with open(file_name, 'w',encoding="utf-8") as csvfile:  
      # creating a csv writer object  
      csv_writer = csv.writer(csvfile)  
          
      # writing the fields  
      csv_writer.writerow(fields)  
      
      # writing the data rows  
      csv_writer.writerows(rows)




def search(api_key,query):
  youtube = build('youtube', 'v3', developerKey=api_key)
  #snippet contain  title desc   etc
  
  #this will return httprequest 
  
  request = youtube.search().list(part=['snippet'],maxResults=10,q=query)
  response = request.execute()
  data = response['items']
  # print(data)

  rows =[]
  for item in data:
      rows.append( [item['snippet']['title'], item['snippet']['description']] )
      # rows.append(  item['snippet']['description'] )
      
  print(rows)
  return {'fields':['title','description'],'rows':[rows]}

# this api key we get from 
# https://console.developers.google.com/apis/dashboard
api_key = 'AIzaSyBJbOnt6HHIkb8lR8755a6kC1h2sYID5BU'



''' uncomment this to test get_video_detail function  '''
# id='PzmNssVLcLQ'
# data =get_video_detail(api_key,id)

# save_to_csv(data['fields'],data['rows'],'ttt2.csv')





''' uncomment this to test search function  '''
_search=search(api_key,"yo yo")
# save_to_csv(_search['fields'],_search['rows'],'search.csv')

# field=['a','b']
# rows =[['aa','bb'],['cc','dd']]
# save_to_csv(field,rows,'hi.csv')


