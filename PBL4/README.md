# 한국어 혐오데이터 세트 분류 모델 만들기
- 아래 데이터로 분류모델을 학습하고 평가한다. 모델끼리 정확도를 비교해본다.
- https://github.com/kocohub/korean-hate-speech/tree/master/labeled

## 모델 종류
- word2vec and text-cnn(or MLP)
    - 한국어 word2vec(PBL3)
    - text-cnn: 텍스트에 대한 cnn이 어려우면 MLP 사용.
- huggingface 한국어 BERT
    - https://huggingface.co/klue/bert-base