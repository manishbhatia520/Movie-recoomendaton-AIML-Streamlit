from database import CATALOGUE
def run_inference_engine(type_p, genre_p, mood_p, pace_p):
    recs=[]
    for item in CATALOGUE:
        score=0
        trace=[]
        if item["type"].lower()!=type_p.lower(): continue
        score+=3
        trace.append(f"Matched type: {item['type']}")
        if item["genre"].lower()==genre_p.lower():
            score+=4
            trace.append(f"Matched genre: {item['genre']}")
        if item["target_mood"].lower()==mood_p.lower():
            score+=3
            trace.append(f"Matched mood: {item['target_mood']}")
        if item["pace"].lower()==pace_p.lower():
            score+=2
            trace.append(f"Matched pace: {item['pace']}")
        if score>=7:
            recs.append({"title":item["title"],"genre":item["genre"],"score":score,"rating":item["rating"],"trace":trace})
    recs.sort(key=lambda x:(x["score"],x["rating"]),reverse=True)
    return recs