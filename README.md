﻿# aichatWithFlask
 [AI X ART 공모전 장관상 기사](https://www.aitimes.kr/news/articleView.html?idxno=23653)
# 제목: < Let's be ALICE. > 또는 < AI ris : Alice>

## 부제: AI를 적용한 인터렉티브 스토리 메타버스 

이상한 나라의 앨리스를 모티브로 하여 현대인을 대표하는 관람자인‘앨리스’와‘채셔캣’과의 대화를 통해‘앨리스’가 진정한 자아를 찾아가는 과정을 표현하였다.


## AI 챗봇으로, 트랜스포머(Transformer) 신경망 모델을 기반으로 구현
자체 스토리로 진행되기 때문에 스토리상의 질문 내에서 사용자와 상황에 맞는 문답을 할 수 있도록 학습데이터를 만들어야 했다. 이를 위해 많은 사용자 응답 예시들을 설문조사를 통해 모으고, 부족한 부분은 자체 제작하여 축적한 데이터를 기반으로 학습시켰다. 자연어 처리 부분에서 RNN과 seq2seq모델의 한계를 극복해 성능을 높이기 위해서 Transformer 아키텍처를 기반으로 한 트랜스포머를 활용하여 딥러닝 ai 챗봇을 구현하였다. 서브워드텍스트인코더를 활용하여 질문과 답변 데이터로부터 단어 집합을 생성하여 인코딩, 디코딩을 진행하였다. 그 후 하이퍼파라미터와 학습률 옵티마이저를 조정하면서 최적의 학습 결과가 나오도록 학습하였다. 

출처 : 인공지능신문(https://www.aitimes.kr)

1- ‘이상한 나라의 앨리스‘ 는 영국의 수학자 루이스 캐럴이 1865년 발표한 소설이다.

2- 7살 여자아이 앨리스가 토끼굴에 들어가 도착한 이상한 나라에서 겪는 모험담을 담고 있다.

3- 1865년 당시, 여자아이들이 호기심을 갖는 건 이상한, 금지된 일이었다.
   이상한 나라의 앨리스 는 결국 모든 기묘한 일들이 앨리스의 꿈이었던 걸로 끝난다.

   하지만 2021년, 이 모든 게 꿈이 아니라면?

4- 2021년, 앨리스의 꿈이 실현된다! 바로 유다움의 메타버스에서!!!

### 작품소개

당신은 본인이 선택해서, 우리의 프로그램, ’앨리스‘(가칭) 을 다운받고, 접속한다.
접속하는 순간, 끝없이 추락한다.
-> 앨리스 느낌을 주는 가상공간에 캐릭터 등장!

▶ 모든 선택에는 예상치 못한 결과가 따르고, 자유에는 그에 대한 책임과 결과가 있음
정신없이 추락한 뒤에는, ’체셔캣’을 만나게 된다. 그가 묻는 첫 질문은, WHO R U? 이다.
(인공지능 넣어서, 간단한 대화, 채팅. 대화에 맞춰서 체셔캣이 사라지는 상황과 존재하는 상황 구분, )

➀ 이름으로 대답하면, 그는 화를낸다.
   - 그니깐! 그게 누구냐고! 이름같은건 중요하지 않아!

➁ ~~에 사는 / ~~의 아들 . 딸 . 막내, 장녀 등으로 대답하면
   - 나는 그런 환경이 궁금한게 아니야 너가 궁금하지

③ 신체 사이즈 등을 이야기하면
   - 정말 못 들어주겠군

등등
(이상적인 답변 – 자유 / 사랑 / 모험 / 여유 , 감정 등이 표현된 답변)
(대화는 추가 및 수정예정)
참고: 앨리스 대사
who r u? 
what is real? 
- 뭐 잃어버렸니? 
- 어디로 가야하죠
- 그건 네가 어디에 가고 싶어하는가 달렸어
- 그건 정말 상관없어요, 
- 그럼 정말 상관없네
- 여기 대부분의 사람들이 미쳤어.



네 번정도의 질문 끝에 체셔캣은 말한다
넌 너가 누군지 전혀 모르고 있어
당장 눈앞에 있는 것도 제대로 보지 못하는걸!
꽃들과 이야기를 나눠봐.

하고 몸이 사라지고 눈알만 깜빡이다가
발자국 소리만 들리며 사라진다.

선택지 – MAD HATTER / FLOWER / 등등 여러 선택지


## 구체적 
traing.py, StartData.csv가 첫 번째 스토리 진행 ai

training2.py, NextData.csv가 두번째 스토리 진행 ai

- 한번에 같이 학습하면 답이 겹쳐서 둘이 분리함.

- 스토리 진행에 따라 데이터 변경해줘야함.

- 재학습함에 따라 답변이 다르게 나올수도

- 아쉬운점: 직접 데이터를 만들어 학습하였으며, train 데이터가 너무 작아 성능이 좋지 못함.




