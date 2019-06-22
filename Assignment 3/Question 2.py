from nltk.chunk import *
import nltk

en1 = "The other area of conflict is more difficult."
en1 = nltk.word_tokenize(en1)
en2 = "He has delivered excellent work under pressure both from his colleagues and from the car industry."
en2 = nltk.word_tokenize(en2)
en3 = "It is, to a large extent, a principle of justice that imbues both health and pension schemes as well as social assistance, where, in particular, strategic coordination by the public authority is essential, even though it has been modernised."
en3 = nltk.word_tokenize(en3)

sp1 = "El otro terreno de discordia es más difícil."
sp1 = nltk.word_tokenize(sp1)
sp2 = "Ha hecho un buen trabajo bajo la presión de sus colegas, y también bajo la presión de la industria automovilística."
sp2 = nltk.word_tokenize(sp2)
sp3 = "Éste es, en definitiva, un principio de justicia que afecta a la sanidad y a los regímenes de pensiones, así como a la asistencia en que sigue siendo ineludible la coordinación estratégica, aunque renovada, del sujeto público."
sp3 = nltk.word_tokenize(sp3)

sw1 = "Det andra området där det finns risk för kollisioner är svårare."
sw1 = nltk.word_tokenize(sw1)
sw2 = "Han har under tryck, inte bara från sina kolleger utan också från bilindustrin, gjort ett gott arbete."
sw2 = nltk.word_tokenize(sw2)
sw3 = "Detta är, i allt väsentligt, en fråga om rättvisa och gäller sjukvården, pensionerna och även de fall där det krävs en strategisk samordning, och förnyelse , av den offentliga myndigheten."
sw3 = nltk.word_tokenize(sw3)

google_sp1 = "La otra área de conflicto es más difícil."
google_sp1 = nltk.word_tokenize(google_sp1)
google_sp2 = "Ha realizado un excelente trabajo bajo presión tanto de sus colegas como de la industria automotriz."
google_sp2 = nltk.word_tokenize(google_sp2)
google_sp3 = "Es, en gran medida, un principio de justicia que impregna los planes de salud y de pensiones, así como la asistencia social, donde, en particular, la coordinación estratégica por parte de la autoridad pública es esencial, a pesar de que se ha modernizado."
google_sp3 = nltk.word_tokenize(google_sp3)

google_sw1 = "Det andra området av konflikt är svårare."
google_sw1 = nltk.word_tokenize(google_sw1)
google_sw2 = "Han har levererat utmärkt arbete under press både från sina kollegor och från bilindustrin."
google_sw2 = nltk.word_tokenize(google_sw2)
google_sw3 = "Det är i stor utsträckning en princip av rättvisa som bjuder in både hälso- och pensionssystem samt socialt bistånd, där särskilt den strategiska samordningen av den offentliga myndigheten är nödvändig, trots att den har moderniserats."
google_sw3 = nltk.word_tokenize(google_sw3)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
print(chunk_parser.parse(nltk.pos_tag(sp3)))
print(chunk_parser.parse(nltk.pos_tag(google_sp3)))
print(chunk_parser.parse(nltk.pos_tag(sw3)))
print(chunk_parser.parse(nltk.pos_tag(google_sw3)))

