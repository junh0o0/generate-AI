#해당 페이지는 각 카페, 식당, 관광명소가 가진 리뷰에 대해 한글, 영어로 저장한 파일입니다.
#GPTAPI는 영어 prompt를 분석하는 성능이 더 뛰어나다고 판단해 영어로 번역한 리뷰를 사용하였습니다.
feature_kor_cafe = [
    "친절해요", "인테리어가 멋져요", "매장이 청결해요", "디저트가 맛있어요", "커피가 맛있어요", 
    "특별한 메뉴가 있어요", "사진이 잘 나와요", "선물하기 좋아요", "주차하기 편해요", 
    "주문제작을 잘해줘요", "가성비가 좋아요", "특별한 날 가기 좋아요", "음료가 맛있어요", 
    "비싼 만큼 가치있어요", "매장이 넓어요", "뷰가 좋아요", "포장이 깔끔해요", "빵이 맛있어요", 
    "아늑해요", "음식이 맛있어요", "재료가 신선해요", "메뉴 구성이 알차요", "차분한 분위기에요", 
    "컨셉이 독특해요", "대화하기 좋아요", "좌석이 편해요", "집중하기 좋아요", "화장실이 깨끗해요", 
    "음악이 좋아요", "단체모임 하기 좋아요", "오래 머무르기 좋아요", "야외 공간이 멋져요", 
    "차가 맛있어요", "종류가 다양해요", "읽을만한 책이 많아요", "아이와 가기 좋아요", "건강한 맛이에요", 
    "혼밥하기 좋아요", "양이 많아요", "술이 다양해요", "음식이 빨리 나와요", "반려동물과 가기 좋아요", 
    "혼술하기 좋아요", "룸이 잘 되어있어요", "기본 안주가 좋아요"
]
feature_kor_attraction = [
    "붐비지 않아요", "사진이 잘 나와요", 
    "볼거리가 많아요", "주차하기 편해요", "가격이 합리적이에요", "설명이 잘 되어있어요", 
    "관리가 잘 되어있어요", "아이와 가기 좋아요", "근처에 갈 곳이 많아요", "야경이 멋져요", 
    "체험 프로그램이 다양해요", "경관이 독특해요", "유익해요", "전시 구성이 알차요", 
    "전시 테마가 재밌어요", "공간이 넓어요", "뷰가 좋아요", "산책로가 잘 되어있어요", 
    "대중교통이 편해요", "방문객이 많아요", "규모가 커요", "화장실이 깨끗해요", "편의시설이 잘 되어있어요", 
    "반려동물과 가기 좋아요", "컨셉이 독특해요", "먹거리가 풍부해요", "자연 경관이 좋아요", 
    "친절해요", "초보자에게도 적합해요", "시설이 깔끔해요", "원데이 클래스가 알차요", 
    "수업 시간이 충분해요", "설명이 자세해요", "선물하기 좋아요", "프라이빗해요", "디자인이 멋져요", 
    "맞춤 수업을 잘해줘요", "품질이 좋아요", "단체로 가기 좋아요", "피크닉하기 좋아요", 
    "조용히 쉬기 좋아요", "동물 관리가 잘 되어있어요", "놀이기구가 다양해요", "대기시간이 짧아요", 
    "안전하게 관리해요", "셔틀버스가 잘 되어있어요"
]
feature_kor_restaurant = [
    "친절해요", "상품이 다양해요", 
    "즉석조리 식품이 맛있어요", "매장이 넓어요", "매장이 청결해요", "신상품이 많아요", 
    "배달 시스템이 편리해요", "행사 상품이 다양해요", "할인/적립을 잘 챙겨줘요", "과채가 신선해요", 
    "고기 질이 좋아요", "취식 공간이 잘 되어있어요", "주차하기 편해요", "음식이 맛있어요", 
    "양이 많아요", "가성비가 좋아요", "인테리어가 멋져요", "특별한 메뉴가 있어요", "재료가 신선해요", 
    "단체모임 하기 좋아요", "직접 잘 구워줘요", "특별한 날 가기 좋아요", "화장실이 깨끗해요", 
    "뷰가 좋아요", "혼밥하기 좋아요", "잡내가 적어요", "메뉴 구성이 알차요", "아늑해요", 
    "반찬이 잘 나와요", "음식이 빨리 나와요", "건강한 맛이에요", "차분한 분위기에요", "좌석이 편해요", 
    "컨셉이 독특해요", "오래 머무르기 좋아요", "룸이 잘 되어있어요", "샐러드바가 잘 되어있어요", 
    "대화하기 좋아요", "환기가 잘 돼요", "비싼 만큼 가치있어요", "아이와 가기 좋아요", 
    "현지 맛에 가까워요", "음악이 좋아요", "포장이 깔끔해요", "코스요리가 알차요", "사진이 잘 나와요", 
    "야외 공간이 멋져요", "기본 안주가 좋아요", "술이 다양해요", "혼술하기 좋아요", 
    "향신료가 강하지 않아요", "음료가 맛있어요"
]
feature_eng_cafe = [
    "The staff is friendly", "The interior is stylish", "The store is clean", "The desserts are tasty", "The coffee is delicious",
    "There are special menus", "It's photogenic", "Great for gifts", "Easy to park",
    "They do custom orders well", "Good value for money", "Good for special occasions", "The drinks are tasty",
    "Worth the price", "The store is spacious", "The view is nice", "The packaging is neat", "The bread is tasty",
    "It's cozy", "The food is delicious", "The ingredients are fresh", "The menu is well-composed", "The atmosphere is calm",
    "The concept is unique", "Good for conversations", "The seats are comfortable", "Good for focusing", "The restroom is clean",
    "The music is nice", "Good for group gatherings", "Good to stay for a long time", "The outdoor space is nice",
    "The tea is tasty", "There is a wide variety", "There are many books worth reading", "Good for kids", "The taste is healthy",
    "Good for dining alone", "Generous portions", "A variety of alcohol available", "The food comes out quickly", "Pet-friendly",
    "Good for drinking alone", "Well-equipped private rooms", "Good basic side dishes",
]
feature_eng_attraction = [
    "It's not crowded", "It's photogenic",
    "There are many attractions", "Easy to park", "The prices are reasonable", "Well-explained",
    "Well-maintained", "Good for kids", "There are many places to visit nearby", "The night view is spectacular",
    "There is a variety of experience programs", "The scenery is unique", "Informative", "The exhibit layout is well-composed",
    "The exhibit themes are interesting", "The space is spacious", "The view is nice", "The walking paths are well-maintained",
    "Public transportation is convenient", "There are many visitors", "It's large in scale", "The restrooms are clean", "The facilities are well-equipped",
    "Pet-friendly", "The concept is unique", "There is a rich variety of food", "The natural scenery is beautiful",
    "The staff is friendly", "Suitable for beginners", "The facilities are clean", "The one-day classes are well-organized",
    "The class duration is sufficient", "The explanations are detailed", "Great for gifts", "It's private", "The design is stylish",
    "They do custom classes well", "The quality is high", "Good for groups", "Great for picnics",
    "Good for a quiet rest", "The animal care is well-managed", "There is a variety of amusement rides", "The waiting time is short",
    "Safely managed", "The shuttle bus service is well-organized"
]
feature_eng_restaurant = [
    "The staff is friendly", "There is a wide variety of products",
    "The ready-to-eat food is delicious", "The store is spacious", "The store is clean", "There are many new products",
    "The delivery system is convenient", "There is a variety of promotional items", "They handle discounts/loyalty points well", "The fruits and vegetables are fresh",
    "The quality of the meat is good", "The dining area is well-arranged", "Easy to park", "The food is tasty",
    "Generous portions", "Good value for money", "The interior is stylish", "There are special menus", "The ingredients are fresh",
    "Good for group gatherings", "They grill the food well for you", "Good for special occasions", "The restroom is clean",
    "The view is nice", "Good for dining alone", "Minimal gamey taste", "The menu is well-composed", "It's cozy",
    "The side dishes are well-prepared", "The food comes out quickly", "The taste is healthy", "The atmosphere is calm", "The seats are comfortable",
    "The concept is unique", "Good to stay for a long time", "The private rooms are well-equipped", "The salad bar is well-maintained",
    "Good for conversations", "Well-ventilated", "Worth the price", "Good for kids",
    "Close to local taste", "The music is nice", "The packaging is neat", "The set courses are well-prepared", "It's photogenic",
    "The outdoor space is nice", "Good basic side dishes", "A variety of alcohol available", "Good for drinking alone",
    "The spices are not overpowering", "The drinks are tasty"
]

