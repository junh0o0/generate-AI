import sqlite3
import reviews

def update_score(feature, weight, table, tablescore):
    conn = sqlite3.connect('./use/location.db')
    cursor = conn.cursor()
    sql_query = f"""
    UPDATE {tablescore}
    SET score = score + ? * (
        SELECT value
        FROM {table}
        WHERE feature = ? AND {table}.name = {tablescore}.name
    )
    """
    cursor.execute(sql_query, (weight, feature))
    conn.commit()
    conn.close()

#사용자 요구사항을 입력받아 GPTAPI가 생성한 text에 관광지마다의 리뷰데이터와 겹치는 내용이 있는지 확인 후 각각의 가중치를 곱해 score에 반영하는 함수입니다.
def update_preference(text):
    for i, feature in enumerate(reviews.feature_eng_cafe):
        if feature in text:
            update_score(reviews.feature_kor_cafe[i], 200, "cafe", "cafescore")
    for i, feature1 in enumerate(reviews.feature_eng_attraction):
        if feature1 in text:
            update_score(reviews.feature_kor_attraction[i], 200, "attraction", "attractionscore")
    for i, feature2 in enumerate(reviews.feature_eng_restaurant):
        if feature2 in text:
            update_score(reviews.feature_kor_restaurant[i], 300, "restaurant", "restaurantscore")
    
     