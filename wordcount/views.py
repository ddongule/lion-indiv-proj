from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')
  # render는 세 개의 인자까지 받을 수 있음
  # 첫 번째는 거의 request를 받고,
  # 두 번째는 템플릿의 이름을 인자로 받고,
  # 세 번째 인자는 선택적으로 받아줄 수 있는데, 사전형 객체를 받을 수 있음.
  # 즉, 딕션어리 형 자료형을 넣을 수 있다.


def about(request):
  return render(request, 'about.html')  


def result(request):
  text = request.GET['fulltext']
  
  # 단어는 공백을 기준으로 나누어서 리스트로 저장해주면 셀 수 있당
  words = text.split()
  # 총 단어수 = len(words)

  # 빈 사전의 이름을 지어준다
  word_dict = {}
  
  for w in words:
    if w in word_dict:
      # increase
      word_dict[w]+=1
    else: 
      # add to dictionary
      word_dict[w]=1
  # word_dict는 이렇게 구성이 되어 있을 것이다. <단어 : 몇번, 단어 : 몇번 >
  # 사전형 자료형에서 쌍을 보내주는 문법이 바로 .items()이다.

  return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary' : word_dict.items()})
  
  


