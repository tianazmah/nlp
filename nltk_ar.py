from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from spacy.lang.ar import Arabic

nlp = Arabic()
doc_file=nlp("""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا. و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل""")
#tokenazition and pos tagging
for token in doc_file:
    print(token.text,token.pos_, token.tag_)

wnl = WordNetLemmatizer()
ps = PorterStemmer()
for token in doc_file:
    print(wnl.lemmatize(str(token)), ps.stem(str(token)))