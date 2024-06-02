import sqlite3
import reviews

def update_score(feature, weight, table, tablescore):
    print("updatescore")
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

def update_preference(text):
    for i, feature in enumerate(reviews.feature_eng_cafe):
        if feature in text:
            update_score(reviews.feature_kor_cafe[i], 10, "cafe", "cafescore")
    for i, feature1 in enumerate(reviews.feature_eng_attraction):
        if feature1 in text:
            update_score(reviews.feature_kor_attraction[i], 10, "attraction", "attractionscore")
    for i, feature2 in enumerate(reviews.feature_eng_restaurant):
        if feature2 in text:
            update_score(reviews.feature_kor_restaurant[i], 10, "restaurant", "restaurantscore")
    
     
print(str(reviews.feature_eng_cafe) + ", " + str(reviews.feature_eng_attraction) + "," + str(reviews.feature_eng_restaurant))