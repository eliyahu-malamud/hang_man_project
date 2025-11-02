import random
words_list_hebrew = ["בננה", "תפוח", "חציל", "עגבניה", "מלפפון", "מחשב", "עכבר", "מקלדת", "מסך", "טלפון"
,"חלון", "דלת", "קיר", "שולחן", "כיסא", "מחברת", "עט", "עיפרון", "תיק", "ספר"
,"אוטובוס", "מכונית", "מטוס", "סירה", "אופניים", "רכבת", "כביש", "מפה", "עיר", "כפר"
,"מדבר", "יער", "ים", "הר", "שלג", "גשם", "שמש", "ירח", "כוכב", "שמיים"
,"חולצה", "מכנסיים", "נעליים", "גרביים", "מעיל", "כובע", "צעיף", "מטריה", "שעון", "משקפיים"
,"חתול", "כלב", "דג", "ציפור", "סוס", "כבשה", "עז", "פרה", "תרנגולת", "ברווז"
,"נמר", "פיל", "קוף", "אריה", "דוב", "גמל", "שועל", "זאב", "תן", "ינשוף"
,"פרח", "עלה", "עץ", "שיח", "דשא", "אבן", "נהר", "אגם", "מפלים", "מדורה"
,"מים", "חול", "אדמה", "שמיים", "רוח", "ברק", "ענן", "סערה", "קשת", "שלולית"
,"רופא", "מורה", "נהג", "כבאי", "שוטר", "חייל", "טבח", "חקלאי", "אופה", "מנקה"
,"צייר", "מוזיקאי", "נגר", "חשמלאי", "מדען", "סופר", "מהנדס", "צלם", "תלמיד", "מאמן"
,"שמחה", "עצב", "פחד", "אהבה", "כעס", "התרגשות", "שעמום", "תקווה", "דאגה", "שלווה"
,"לחם", "גבינה", "ביצה", "חמאה", "שוקולד", "עוגה", "גלידה", "קפה", "תה", "פיצה"
,"סוכר", "מלח", "פלפל", "בצל", "שום", "קמח", "אורז", "מרק", "חלב", "עוף"
,"אוניה", "רכב", "אופנוע", "מסוק", "מטען", "נמל", "תחנה", "כביש", "מחלף", "מנהרה"
"בית", "בניין", "מדרגות", "קומה", "גג", "חדר", "מטבח", "אמבטיה", "שירותים", "סלון"]
words_list_english = [
    "banana", "apple", "eggplant", "tomato", "cucumber", "computer", "mouse", "keyboard", "screen", "phone",
    "window", "door", "wall", "table", "chair", "notebook", "pen", "pencil", "bag", "book",
    "bus", "car", "airplane", "boat", "bicycle", "train", "road", "map", "city", "village",
    "desert", "forest", "sea", "mountain", "snow", "rain", "sun", "moon", "star", "sky",
    "shirt", "pants", "shoes", "socks", "coat", "hat", "scarf", "umbrella", "watch", "glasses",
    "cat", "dog", "fish", "bird", "horse", "sheep", "goat", "cow", "chicken", "duck",
    "tiger", "elephant", "monkey", "lion", "bear", "camel", "fox", "wolf", "jackal", "owl",
    "flower", "leaf", "tree", "bush", "grass", "stone", "river", "lake", "waterfall", "campfire",
    "water", "sand", "earth", "sky", "wind", "lightning", "cloud", "storm", "rainbow", "puddle",
    "doctor", "teacher", "driver", "firefighter", "policeman", "soldier", "cook", "farmer", "baker", "cleaner",
    "painter", "musician", "carpenter", "electrician", "scientist", "writer", "engineer", "photographer", "student", "coach",
    "happiness", "sadness", "fear", "love", "anger", "excitement", "boredom", "hope", "worry", "calm",
    "bread", "cheese", "egg", "butter", "chocolate", "cake", "ice cream", "coffee", "tea", "pizza",
    "sugar", "salt", "pepper", "onion", "garlic", "flour", "rice", "soup", "milk", "chicken",
    "ship", "vehicle", "motorcycle", "helicopter", "cargo", "port", "station", "road", "interchange", "tunnel",
    "house", "building", "stairs", "floor", "roof", "room", "kitchen", "bathroom", "toilet", "living room"
]

def choose_secret_word(words: list[str]) -> str:
    return words[random.randint(0, len(words) - 1)]




