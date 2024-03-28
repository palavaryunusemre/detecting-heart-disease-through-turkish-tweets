## TÜRKÇE TWEETLER ÜZERİNDEN KALP HASTALIĞI TESPİTİ ÜZERİNE BİR ÇALIŞMA

### 1.	GİRİŞ

Kalp yapı bakımından incelendiğinde yetişkin bir kadın için ortalama olarak 200-280 gram ağırlığında, yetişkin bir erkek için 250-390 gram ağırlığındadır. Halk arasında ise yaygın görüş herkesin kalbinin kendi yumruğu kadar olduğudur. Kalp boyut olarak bakıldığında organlarımız arasında küçük organlarımızdan birisidir. Kalp boyut olarak küçük olmasına rağmen işlevi bakımında oldukça hayati bir organdır. Kalbimizde oluşabilecek herhangi bir bozulma ve deformasyon ciddi sonuçlara sebep olabilir. Kalp hastalıkları olarak adlandırabileceğimiz bu bozulma ve deformasyonlara birçok faktör etki edebilmektedir. Bu faktörler arasında kalıtımsal hastalıklar, alkol kullanımı, sigara kullanımı, çeşitli uyuşturucu madde kullanımları, yaş, cinsiyet ve beslenme hastalıları gösterilebilir. Kalp hastalıkları dünya da yaşanan ölümlerin en büyük sebepleri arasındadır [1-2].

Veri madenciliği basit ve temel bir tanımla, veriler hakkında örtük, daha önce bilinmeyen ve potansiyel yararlı bilgilerin önemsiz bir şekilde çıkarılmasıdır. Veri madenciliğinde temel adımlar şu şekildedir. Veri madenciliğinde ilk önce hedef veri kümesi tespit edilir. Daha sonra verinin saklanacağı veri tabanı sistemi seçilir. Veri tabanına alınan veri içirişinde alakasız veri temizlemesi, eksik veri tamamlaması gibi veri ön işleme işlemleri gerçekleştirilir. İşlenen veriler çalışma kapsamında çeşitli işlemlerden geçirilir ve sonuçlar elde edilir. Veri madenciliği pazarlama, bankacılık, e-ticaret, telekomünikasyon, eğitim, tıbbi araştırmalar vb. gibi alanlarda kullanılır [3].

Veri madenciliği yöntemleri tıbbi araştırmalar altında çeşitli alanlarda kullanılmıştır. Büyük verilerin işlenmesi ile oluşan veri tabanlarından elde edilen bilgiler ile insanların kalp hastalıklarına yakalanma ihtimalleri saptanabilmiştir [3]. Taşçı ve Şamlı’nın yapmış oldukları çalışmada yüzlerce bilginin bulunduğu kalp veri setinden, WEKA programı kullanılarak, çeşitli algoritmalar uygulayarak kişilere kalp hastalığı teşhisi koymaya çalışılmıştır [3]. Çalışma kapsamında Naive Bayes, J48 Karar Ağacı, Rastgele Orman gibi toplamda 9 farklı sınıflandırma algoritması kullanılmıştır [3]. Algoritmalar Kaggle veri setinden 303 hastaya uygulanmıştır. Çalışma sonucunda en doğru sonucu veren sınıflandırma algoritması k-NN algoritması olarak saptanmıştır [3]. Bulut’un yapmış olduğu çalışmada AdaBoost ile kalp krizi tespiti yapılmaya çalışılmıştır. Bu çalışmada ölüm nedeni olan ve yaşam standartlarını düşüren kalp damar hastalıkları nedenleri şu şekilde sıralanmıştır; Düşük iyi kolesterol (HDL),Yüksek kötü kolesterol (LDL ve trigliserit), Hipertansiyon, Damar tıkanıklığı ve buna benzer hastalıklar, Ritim bozukluğu ve senkop olayı gibi çeşitli kalp hastalıkları, Daha önceden geçirilmiş kalp krizi, İleri yaş (kadınlarda 50, erkelerde ise 40 yaş üstü), Diyabet, Obezite, Aşırı alkol tüketimi, Sigara, Uyuşturucu, Stres, Yoğun yaşam temposu. Bu sıralanan sebepler ışığında anket oluşturulmuştur [4]. Ankette kalp hastalığına sebep olan etmenler altı ana gruba bölünmüştür. Bunlar; temel demografik özellikler, bireysel ve yaşamsal alışkanlıklar, genel sağlık durumu, spor ve hareketlilik, beslenme alışkanlıkları, psikolojik durumu. Bu eksende oluşturulan anketler Manisa Merkezefendi Devlet Hastanesi ve İzmir Ege Üniversitesi Hastanesindeki Kardiyoloji bölümlerindeki 62 hastaya uygulanmıştır [4]. 
Toplanan veriler değerlendirilirken bazı sorulara verilen cevap “hayır” ise veri setine 0 olarak; “evet” ise 1 olarak kaydedilmiştir. Bazı çoktan seçmeli sorularda bulunan a, b, c ve d şıkları ise veri setine sırasıyla 1, 2, 3 ve 4 tam sayısı olarak kaydedilmiştir [4]. Ayrıca bazı çoktan seçmeli sorular ise harf olarak kaydedilmiştir. Yeterince cevap alınamayan sorular eğitim setine dahil edilmemiştir. Verilere min-max normalizasyonu uygulanmıştır [4]. Bu çalışmada temel öğrenici olarak kural tabanlı bir sınıflandırıcı olan CART karar ağaçları tercih edilmiştir [5]. Adaboost algoritması ile sınıflandırılma yapılmıştır. Adaboost algoritmasının I=100 için seçildiğinde hastaların gerçek kalp krizi geçirme yaşları ile hesaplanan kalp krizi geçirme yaşı doğrusallık göstermektedir [4].
Vatansever, Aydın ve Çetinkaya yapmış oldukları çalışmada genetik algoritmaları kullanarak öznitelik seçimi yapmışlardır. Makine öğrenimi algoritmaları ile kalp hastalığı tahmin etmeye çalışmışlardır. Bu çalışmada Vatansever ve diğerleri Kaggle’dan elde edilen kalp veri setini kullanmışlardır. Çalışma kapsamında verilerin %20 si test, %80 i eğitim verisi olarak kullanılmıştır. Çalışma kapsamında K-EYK, LR, KA, RO, NB, DVM ve GA algoritmaları kullanılmıştır. Veri seti bu algoritmalar ile test edilmiştir. Bu algoritmalardan en başarılısı GA ile yapılan tahminlemedir [5].
Solmaz, Tiren ve Özkaya’nın yapmış oldukları çalışmada kalp hastalıkları tespiti için Destek Vektör Makineleri (DVM), K-En Yakın Komşuluk (K-EYK) ve Yapay Sinir Ağları (YSA) kullanılmıştır. Bu çalışmada kullanılan veri seti Cleveland veri seti kullanılmıştır. Çalışma kapsamında veri setinden 14 parametre kullanılmıştır. Bu parametreler DVM, K-EYK ve YSA makine öğrenimi metotları ile test edilmiştir. Çalışmanın performans metrikleri sırasıyla; duyarlılık, özgüllük, doğruluk, kesinlik, F1-Skoru ve MKK’dır. Bu metriklere göre en başarılı sonuç gösteren yöntem YSA’dır [6].
Özcan, Taşar, Tatar ve Yakut yapmış oldukları çalışmada Support Vector Machine algoritması ve İleri Yayılımlı Yapay Sinir Ağları ile kalp hastalıklarını tahmini üzerine çalışmışlardır. Çalışma kapsamında UCI Machine Learnig Repository veri bankasına ait Statlog (Heart) Data Set veri tabanından kalp hastalığı ile ilgili bir tıbbi veri kümesi kullanılmıştır. Cleveland veri tabanı, kişileri iki sınıfa ayırmak için kullanılmıştır. Bu sınıflandırma yapılırken normal (0) ve kalp hastası (1) olarak değerlendirilmiştir. Çalışma kapsamında YSA algoritması başarısı literatür ile örtüşürken, DVM algoritması kayda değer oranda başarılı olmuştur [7]. 
Ahmed ve diğerlerinin yapmış oldukları çalışmada kalp hastalığını tespit etmek için gerçek zamanlı bir sistemin eğitilmesi desteklenmesi için 4 tür makine öğrenmesi algoritması karşılaştırılmıştır. Bu algoritmalar karar ağacı, destek vektör mimarisi, rastgele orman sınıflandırıcısı ve lojistik regresyon sınıflandırıcısıdır. Çalışma kapsamında Cleveland kalp hastalığı veri seti kalp hastalığını tahmin etmeye yönelik makine öğrenimi algoritmalarını test etmek ve eğitmek amaçlı kullanılmıştır. Çalışma kapsamında Twitter verilerinden yararlanılmıştır. Veriler toplanırken Cleveland modelindeki anahtar kelimelerden yararlanılmıştır. Toplanan veriler veri ön işlemeye tabi tutulmuştur. Çalışma sonuçları rastgele orman sınıflandırıcı algoritmasının en başarılı algoritma olduğunu göstermektedir. Çalışma kapsamın da apache spark ve apache kafka kullanılmıştır. Spark yapılandırılmamış veriler ile çalışabilmektedir. Spark kütüphanelerinden olan spark streaming tweetleri okur ve gerçek zamanlı işler. Spark’ın makine öğrenimi kitaplığı MLlib makine öğrenimi sınıflandırma algoritmalarını uygular. Çalışma kapsamın da apache kafka gerçek zamanlı veri ardışık düzenleri ve akış uygulamaları oluşturmak için kullanılmıştır. Veri seti detaylarında özellik olarak 13 bağımsız değişkenden ve kalp hastalığını tahmin etmek için kullanılan sınıf etiketi olarak bir bağımlı değişkenden oluşmaktadır. Sınıf etiketi, kalp hastalığının yokluğunu temsil eden 0 sınıf etiketi olan beş değere sahiptir; 1, 2, 3 ve 4 değerleri ise bazı kalp problemlerinin varlığını temsil eder. Bu çalışma ikili bir sınıflandırmadır. Kalp hastalığı olan kişi için 1 ve kalp hastalığı olmayan kişi için 0.  Cleveland kalp hastalığı veri seti özellikleri sırasıyla; yaş, cinsiyet, göğüs ağrısı türü, dinlenme kan basıncı, serum kolestrolü, açlık kan şekeri, dinlenme elektrokardiyografik sonuçları, maksimum kalp atış hızı, egzersize bağlı angına, eski zirve dinlenmeye göre egzersizin neden olduğu st depresyonu, zirve egzersiz st segmentinin eğimi, floroskopi ile renklendirilen büyük damar sayısı (0-3), talyum taraması. Kalp hastalığı tahmin sistemi çevrimdışı model oluşturma, akış işleme hattı ve çevrimiçi tahmin olmak üzere üç ana bileşen içerir. Bu bileşenin temel amacı, deneyler boyunca mümkün olan en yüksek doğruluğa ulaşan makine öğrenimi modelini geliştirmektir. Çevrimdışı modeli oluşturmak için kullanılan sınıflandırma algoritmaları DT, SVM, RF ve LR. Veri ön işleme aşamasında minmax scalar kullanılmıştır. Özellik seçim algoritmaları Özellik seçim algoritmalarını kullanmanın temel avantajları, veri tabanındaki önemli özellikleri belirlemektir ve sistemin başarılı olabilmesi için mevcut olması gereken bu önemli özellikleri belirtmek için tek değişkenli özellik seçimi ve Rölyef olmak üzere iki tür algoritma kullanılmıştır. Makine öğrenimi algoritmalarının değerlendirilmesi ve modeller için en iyi doğruluğu elde etmek için K-Fold Cross-validation (CV) yöntemi ve hiperparametre ayarlaması kullanılmıştır. Bu aşama, modeli gerçek zamanlı olarak değerlendirmek için kullanılan ana aşamalardan biri olarak kabul edilir. Sistem tweetleri “hrtdis” başlık kelimesiyle alır. Bu tweet, eğitim veri setinde aynı sırayla AGE, SEX, CPT, RBP, SCH, FBS, RES, MHR, EIA, OPK, PES, VCA ve THA gibi bir dizi özellik değeri içerir. Aşama, verilerin Twitter'dan alınıp Kafka Topic'e gönderildiği birçok adımdan oluşur. Bundan sonra Spark, Kafka Konusundaki akış verilerini okur. Toplanan veriler metin biçimindedir. Bu nedenle, sağlıkla ilgili önemsiz verilerin çıkarılması ve ardından verilerin çıkarılması gibi bazı adımlar uygulanmalıdır. Daha sonra bu verileri bir vektöre dönüştürür ve geliştirilen Random Forest Classifier'a eğitim setindeki öznitelik vektörü ile aynı sırada gönderir. Veri kümesinden önemli özellikleri seçmek için kullanılan Tek Değişkenli ve Rölyef olan iki özellik seçme tekniğine odaklanmaktadır.  Univariate tarafından seçilen özellikler incelendiğinde MHR ve OPK'nın en yüksek puanlara sahip olduğunu ve model eğitimi ve testi üzerinde önemli bir etkiye sahip olduklarını görebiliriz. FBS ve RES sırasıyla 2 ve 2,97 ile en düşük puana sahiptir. Rölyef tarafından seçilen özellikler incelendiğinde THA'nın 0.275 ile en yüksek sıraya, SCH ve FBS, sırasıyla 0.005 ve 0.002 ile en küçük sıralamaya sahiptir. Tasarlanan sistemin akış işleme hattı bileşeninde, tweet akışları "hrtdis" başlık sözcüğü kullanılarak Twitter'dan alınır ve Kafka konusuna gönderilir; ardından Spark akışı, Kafka konusundaki verileri okur ve bundan sağlık özniteliklerini çıkarır ve ardından bunu çevrimiçi tahmin bileşenine iletir. Çevrimiçi tahmin, nitelikleri eğitim veri kümesindeki sıra ile aynı sırada bir özellik vektörü olarak alır; daha sonra tweetin kalp hastalığı belirtileri içerip içermediğini tahmin etmek için geliştirilen makine öğrenme modelini uygular. Sonuçlar, tam özelliklere sahip RF doğruluğunun, rekabetçi çalışmaya kıyasla doğruluğu %11 oranında iyileştirdiğini kanıtlamıştır [8]. 
##### 2.	LİTERATÜR İNCELEMESİ

Literatürde yapılan çalışmalar Twitter verileri üzerinden kişilerin depresyon sevileri ölçülen çalışmalar mevcuttur. Bu çalışmaların yanında kaggle kalp veri seti üzerinde yapılan çalışmalar mevcuttur. Bu veri seti üzerinde yapılan çalışmalar daha çok sınıflandırma algoritmalarının performansını değerlendirmek, parametrelerinin hangilerinin daha etkin olduğunu belirlemeye yönelik yapılan çalışmalardır. 
Jain ve diğerlerinin yapmış olduğu çalışma da makine öğrenim teknikleri ile depresyon tespiti yapılmıştır. Çalışma kapsamın da anket hazırlanmış ve katılımcılardan bu anketleri doldurmaları beklenilmiştir. Eş zamanlı olarak twitter veri toplanılmıştır. Anket oluşturulurken dünya çapındaki anket araştırmalarına dayanarak, yaygın olarak kabul edilen birçok yol ve kriter geliştirilmiştir. Örneğin, Lenore Sawyer Radloff'un ilgili çalışmalarından birinde, CES-D Ölçeği, kullanıcıların kötü duyguları ve uyku koşulları gibi zihinsel durumlar hakkında 20 soru içermektedir. Sorular ya farklı puanlarla uyumlu birkaç seçeneğe sahiptir ya da kullanıcıların durumlarının derecesi hakkında geri bildirimde bulunmalarını gerektirir. Depresyon düzeyi, toplam puan ölçeğine göre teşhis edilir. Başka bir örnekte, Becks Depresyon Envanteri'nde kullanıcıların zihinsel ve fizyolojik durumları hakkında ruh hali, başarısızlık duygusu, tatminsizlik, sinirlilik, suçluluk duygusu, ceza duygusu, kendinden nefret etme, kendini suçlama ve çalışmayı engelleme gibi 21 kategori vardır. Richardson'ın bir başka çalışması, ergenler arasında depresyon için bir araç olarak Hasta Sağlığı Anketi -9 maddesinin (PHQ-9) performans özelliklerini ve geçerliliğini incelemiştir. Çalışma, depresyona yol açan tüm yönleri veya faktörleri ve semptomları kapsayan gelişmiş bir versiyonu olan PHQ-9'a benzer bir anket kullanır. Anketler, herhangi bir düzeyde depresyon yaşayan bir öğrencide gözlemlenen belirtiler ve ebeveynlerin bu senaryoya ne düzeyde dahil olduğu dikkate alınarak hazırlanmıştır. Ayrıca, veri setimizi depresyonun şiddetini belirlemede mümkün olduğunca etkili kılmak için çeşitli danışmanlara danıştık. Eksik veriler, mümkün olan en yüksek cevapla boşluklar doldurularak ele alınır. Anketin hazırlanması sırasında odaklanılan birkaç özellik; yaş, cinsiyet, okulda/kolejde düzenlilik, yorgun hissetmek / az enerjiye sahip olmak, karamsar veya umutsuz hissetmek, uykusuzluk derecesi, iştahsızlık, bir şeylere konsantre olma sorunu, ölme düşünceleri, kasıtlı olarak aşırı dozda uyuşturucu, herhangi bir fiziksel/zihinsel istismara maruz kalmış Bu veri seti için toplam 18 özellik ve yanıtın kaydedildiği zaman olan zaman damgasını ve öğrencilerin buna ilişkin ek bilgi verebilecekleri yorumlar bölümünü içeren dokümantasyon amaçlı 5 özellik kullanılmıştır. Formu çeşitli okullarda ve kolejlerde dağıtılmış sonra, 619 yanıt kaydedilmiş ve bunlar daha sonra eksik değerlerin ele alınması gibi ön işlemlerden geçirilmiş ve veri kümesine dönüştürülmüştür. Twitter gönderileri (olumlu ve olumsuz duygular içeren ancak intihar veya depresyonla ilgili olmayan) mevcut veri setinden toplanmıştır. yrıca, Kaggle'dan olumlu ve olumsuz duygular (intiharla ilgili kelime içermez) etiketli veri seti aldık. Reddit ve Twitter'dan gönderileri topladıktan sonra, fazla beyaz alanı kaldırdık ve ardından metni küçük harfle değiştirilmiştir. Ardından veri temizliği yapılır, bunun için aşağıdaki prosedürü uygulanmış. İlk adım, alfabetik olmayan tüm karakterlerin kaldırılmasını içerir. Engellenen sözcükleri kaldırılmış, bunun için NLTK engelleyici sözcükler külliyatını kullanılmıştır. Daha sonra kelimelerin köklenmesi ile veri seti oluşturuldu (öncelikli olarak özellik indirgeme için yapıldı), görev için porter stemmer kullanılmıştır. Toplanan veriler veri ön işlemeye tabi tutulmuştur. Verilerin az bir kısmı test çoğunluğu eğitim amaçlı olmak üzere veri ikiye ayrılmıştır. Veri setinde intihar düşüncesini belirlemek için duygu analizi yönteminden yararlanılmıştır. Sonuçlar farklı sınıflandırma algoritmaları ile test edilmiştir [9].
Bhadrashetty ve diğerlerinin yapmış olduğu çalışmada Twitter verileri üzerinden insanların stres dereceleri ölçülmesi, saptanması amaçlanmıştır. Çalışma kapsamın 3 aşamalı bir yol izlenmiştir. İlk aşamada belirli anahtar kelimeleri barındıran twitlerin toplanması, ikinci aşamada toplanan twitler üzerinde duygu analizi yapılması, son aşamada anahtar kelimelere atanan yoğunluk değerlerine dayalı puan hesabı. Duygu analizi kapsamında twitlerin ne anlama geldiği 3 grup halinde incelenmiştir. Bu gruplar poztif, negatif ve nötrdür. Puanlama yapılırken veriler grup olarak ele alınmıştır. Bu gruplar sakin, gergin ve streslidir. En yüksek puan relax grubuna aittir. Gergin grubu orta puanlı kullanıcılara aittir. En düşük puanlı grup stresli grubudur.  Kişilerin twitleri değerlendirilirken çeşitli gruplara ayrıştırılmıştır. Bu gruplar kişilerin arkadaşları ile olan etkinlikleri, kişilerin beğenilmek için olan etkinlikleri olarak 2 gruba ayrılmıştır. Çalışma kapsamında kullanıcıların tweet'lerinin hem içerik hem de sosyal etkileşim bilgilerinden tam olarak yararlanmak için, faktör grafiği modelini (FGM) evrişimli bir sinir ağı (CNN) ile birleştiren bir hibrit model önerilmiştir. Bu çalışmada ayrıca birkaç ilginç stres fenomeni keşfedilmişitir. Stresli kullanıcıların seyrek bağlantılı (yani delta bağlantısı olmayan) sosyal yapılarının sayısının, stresli olmayan kullanıcılarınkinden yaklaşık %14 daha fazla olduğu bulunmuştur, bu da stresli kullanıcıların arkadaşlarının sosyal yapısının daha az bağlantılı olma eğiliminde olduğunu ve stresli olmayan kullanıcılardan daha az karmaşıktır [10].
Alotaibi ve diğerlerinin yapmış olduğu çalışmada Sehaa isimli uygulama kalp hastalıklar, hipertansiyon, deri hastalıkları, kanser ve diyabet hastalıkları için twitterdan veri analizi yolu ile tespit amaçlı önerilmiştir. Bu çalışma arapça twitler üzerinde yapıldığından türü bakımdan ilk çalışmadır. Önerilen sehaa aracı belirlenen anahtar kelimeler ışığında twitleri toplar. Veriler veri ön işleme, veri temizleme işlemlerine tabi tutulur. Bu verilerin %60’lık kısmı eğitim verisi olarak ayrılmıştır. %40’lık kısım test verisidir. Toplanan veriler Suudi Arabistan sınırları içerisinde sınırlandırılmıştır. Toplanan twitler ilgili veya ilgisiz olarak etiketlenmiştir. Twitler 2. aşamada farkındalık amaçlı twitler ve gerçek vaka bildiren twitler olarak ayrılmıştır. Veriler işlenmiş sonuçlar grafikler ile gösterilmiştir. Çalışmada karşılaşılan zorluklar twetlerin arapça kaynaklı olmasından dolayı etiketlemenin manuel yapılmasıdır. Bu uzun ve maliyetli bir süreçtir. Yarı denetimli veya denetimsiz öğrenim mekanizması önerilmektedir. Bu mekanizmaların doğruluk oranı az olduğunda bu da ayrı bir zorluktur [11].
Al Asad ve diğerlerinin yapmış olduğu çalışmada Twitter ve facebook verilerinden yararlanılarak kişilerin depresyon dereceleri saptanmaya çalışılmıştır. Depresyon seviyesi 6 farklı sınıfta makine öğrenimi modeli ile sınıflandırılmıştır. Bu sınıflar normal, hafif, orta, sınırda, şiddetli, aşırıdır. Model tahmin yaparken naive bayes sınıflandırıcısını esas alır. Kullanıcı verilerini duygu durumlarını içeren dosya birlikte sistem modelleyerek verilerin depresyon derecesini saptamaktadır [12]. 
Joshi ve diğerlerinin yapmış olduğu çalışma da akut hastalıkların twitter verileri ile tespiti amaçlanmıştır. Twitter yapı bakımından çok miktarda veriye sahip olduğunda veri bataklığına neden olabilmektedir. Çalışmada 4 aşamalı bir model önerilmiştir. İlk 3 adım twitlerin alaka düzeyini saptarken 4. Adım olaylar arası süreye dayalı izleme algoritması sunar [13].
Özmen ve diğerleri yapmış oldukları çalışmada sınıflandırıcı modellerinin kalp hastalığı verileri üzerinde performans karşılaştırmaları yapmışlardır. Bu sınıflandırıcı modelleri; Support Vector Machine (SVM), Naive Bayes, J48, Random Forest, Adaboost, Logistic Regression, Single Layer Perceptron, Multi Layer Perceptron, Bagging and Decision Trees. Çalışma kapsamında kullanılan veri seti UCI’den alınan Heart Disease Data Set isimli veri setidir. Her algoritma için iki farklı test yöntemi belirlenmiş ve kullanılmıştır. Bu yöntemlerden ilki 10 kat çapraz geçerlilik, ikincisi eğitim veri seti için %75 ve test veri için %25 paylaştırarak kullanmak. Çalışma sonucunda en iyi performansı gösteren SVM sınıflandırma algoritması olmuştur [14]. 
Ali yapmış olduğu çalışmada Twitter aramasından “yakın zamanda teşhis edilmiş” ve “diyabet” sorgusu kullanılarak toplanan Twitter kimliklerinin bir örneğini kullanarak bireysel düzeyde bir diyabet tespit aracı geliştirmeyi hedeflemiştir. Herhangi bir tıbbi ayar olmaksızın, Fisher'in kesin testi kullanılarak sosyal medya gönderilerinin metin analizine dayanan bu tez, makine öğrenimi teknikleri, Naive Bayes ve Random Forest sınıflandırıcıları aracılığıyla diyabet teşhisinin ve sınıflandırılmasının fizibilitesini araştırıyor. Bahsedilen örneklemdeki kullanıcıların yarısından fazlasının (20/30 ≈ %67) diyabet testinin pozitif çıktığı, kullanıcıların yaklaşık %27'sinin (8/30) semptomlardan bahsettiği ve diyabetle ilgili tartışmalara katıldığı tespit edildi, ancak testin pozitif olduğundan bahsetmedi ve geri kalan %4'ü semptom veya diyabetten bahsetmemiştir [15].
Chulis yapmış olduğu çalışmada amacı büyük bir yapılandırılmamış hastalıkla ilgili tweet koleksiyonunun daha fazla analiz edilmek üzere yapılandırılmış verilere dönüştürülebileceği süreçleri karşılaştırmaktır. Bu, Twitter'daki hastalığa özgü iletişimlerle ilişkili içerik ve davranış kalıpları hakkında fikir edinmek amacıyla yapılmıştır. 34 milyondan fazla tweet içeren bir temel veri seti oluşturmak için kanser, diyabet ve astımla ilgili on iki aylık Twitter verileri toplanmıştır. Twitter verilerinin ham haliyle yönetilmesi zor olacağından, analiz dosyaları oluşturmak için bir yöntem belirlemek, sınıflandırma hassasiyetini ve veri saklamayı en üst düzeye çıkarmak için üç ayrı veri azaltma yöntemi karşılaştırılmıştır. Daha sonra hastalık dosyalarının her biri, kullanıcı davranışı iç görülerinin hastalığa göre nasıl değiştiğini göstermek için bir CHAID (ki-kare otomatik etkileşim dedektörü) analizinden geçirilmiştir. Ki-kare Otomatik Etkileşim Dedektörü (CHAID), 1980 yılında Gordon V. Kass tarafından oluşturulmuş bir tekniktir. CHAID, değişkenler arasındaki ilişkiyi keşfetmek için kullanılan bir araçtır. Bu çalışma, standart CRISP-DM veri madenciliği yaklaşımını izlenmiş ve Twitter verileri madenciliği uygulamasının bu altı aşamalı yinelemeli çerçeveye nasıl uyduğunu gösteriyor. Çalışma, değerli bir sağlık hizmeti veri kaynağı olarak sahip olduğu potansiyel Twitter verilerine ve verilerle çalışmanın içerdiği nüanslara yeni bir bakış açısı sağlayan içgörüler üretmiştir [16].
Saravia ve diğerleri yapmış oldukları çalışmada yeni bir veri toplama mekanizması öneriyor ve bir kullanıcının zihinsel bir bozukluktan muzdarip olup olmadığını belirlemek için özellikle Twitter'da kullanılan dil ve davranış kalıplarından yararlanan tahmin modelleri oluşturmaktadırlar. Tahmine dayalı modelleri eğittikten sonra, gösterim MIDAS için arka uç olarak hizmet etmek üzere önceden eğitilmiştir. MIDAS, akıl hastalıklarıyla ilgili olarak, kullanıcının sosyal medyadaki dilsel ve davranışsal kalıplarına ilişkin çeşitli özellikleri keşfetmek için bir analitik web hizmeti sunar. Model eğitilirken 2 farklı kullanıcı tipi belirlenmiştir. Bu tipler hastalar ve hasta olmayanlardır. Hasta türündeki kullanıcılar için veriler toplanırken hasta oldukları beyanında bulunanlar ele alınmıştır. Ne hasta ne de hasta olmadığını belirtmeyenler ise rastgele aktif Twitter kullanıcıları olarak ele alınır. Genel olarak, bir kullanıcının iki belirli zihinsel bozuklukla ilgili çeşitli özelliklerinin araştırılmasına izin veren çevrimiçi bir sistem kurulmuştur. Bu sistem, çevrimiçi bir kullanıcı davranışını daha iyi anlamak için daha karmaşık sistemler oluşturmak için kullanılabilecek minimum sonuçlar sağlar. Ayrıca sistem, geri bildirim sağlama yolu sağlayarak daha fazla hasta verisi toplamak için kullanılabilir. Geri bildirim, öğrenme modellerinde ince ayar yapmak ve daha da geliştirmek için önemlidir [17].


##### 3.	MATERYAL VE METOT

Çalışma kapsamın 2022 yılı mayıs ayı itibari ile geri dönük 5 yıllık tweetter verilerinden yararlanılmıştır. Bu veriler elde edilirken konu ile alakadar önceki çalışmalardan çıkarımla anahtar kelimleler belirlenmiş bu anahtar kelimeler ışığında tweetterdan veri kazıma işlemi gerçekleştirilmiştir. Anahtar kelimeler; “kan basıncı”, “kan şekeri”, “göğüs ağrısı”, “kalp AND yaş”, “kalp AND anjina”, “kalp AND ekg”, “kalp AND cinsiyet”, “kalp AND kolesterol”, “kalp ritmi” ve “serum kolesterol” dür. Bu çalışmada veri kazıma aşamasında twint aracından yararlanılmıştır. Çekilen veriler veri ön işlemeye tabii tutulmuştur. Veri ön işleme aşamasında python’a ait regex kütüphanesinden yararlanılmıştır. Temizlenen verilerin görselleştirilmesi aşamasında kelime bulutu yönteminden yararlanılmıştır.

###### 3.1.	Twint

Twitter üzerinden veri elde etmek için tasarlanmış bir kazıma aracıdır. Twitter üzerindeki arama operatörleri kullanılarak belirli bir hesap, tarih aralığı veya metin hakkındaki tweetleri elde etmek için kullanılır. Şekil 1 ‘de Twitter üzerinden çekilen örnek bir veri seti gösterilmektedir.

![](https://i.hizliresim.com/59wetcs.png)
Şekil 1 Kan şekeri anahtar kelimesine ait veri seti
###### 3.2.	Veri Ön İşleme

Özellikle yanıt niteliği taşıyan tweetlerde verilerin analiz edilmesini zorlaştıran pek çok yazım ve noktalama yanlışı bulunmaktadır. Bu yanlışların temizlenebilmesi için düzenli ifadelerden faydalanılmış ve veriler üzerindeki; noktalama işaretleri, “@”,”#” gibi twitter operatörleri, numara içeren kelimeler, birden fazla bırakılmış boşluklar ve internet adreslerine verilen bağlantılar kaldırılmış ve elde edilen veriler excel formatında saklanmıştır. Şekil 2’de örnek bir veri ön işlemine tabi tutulmuş veri seti verilmiştir.
![](https://i.hizliresim.com/j8c5fvg.png)
Şekil 2 Kan Şekeri Veri Setinin Veri Önişlemeye Tabi Tutulması

###### 3.3.	Kelime Bulutu ile Veri Görselleştirme
Kelime bulutu ya da etiket bulutu, metin verilerini görselleştirmenin eğlenceli ve anlaşılır bir yoludur. Bir kelime bulutuna bakan gözlemci, metnin yoğunluğu, sıklığı ve dağılımı konusunda kolaylıkla çıkarım yapabilir. Kelime bulutu python üzerinde WordCloud kütüphanesi kullanılarak gerçekleştirilmiştir. Şekil 3’te örnek bir kelime bulutu verilmiştir.
![](https://i.hizliresim.com/1q93xdj.png)

Şekil 3 Kan Şekeri Veri Setinin Tweetlerinden Oluşan Kelime Bulutu

##### 4.	SONUÇLAR
Çalışma kapsamında Twitter üzerinde belli anahtar kelimeler ışığında veri kazıma işlemi gerçekleştirilmiştir. Bu elde edilen veriler veri önişlemeye tabii tutulmuştur. Veri önişleme işlemi sonrasında veriler kelime bulutu yöntemi ile görselleştirilmiştir. Bu görselleştirme sonucunda veriler arasında örneğin “kalp AND yaş” anahtar kelimesi için Türkçenin anlam zenginliğinden kaynaklı anlamsız verilerde yer almaktadır. Örneğin yaş kelimesi mana itibari ile hem nemli, ıslak hem insan yaşı, hem de gözyaşında ki yaş manasında gelebilmektedir. Çalışmanın devamında kelime bulutu yöntemi ile elde edilen veriler grafiklere dökülerek kelime yoğunluğu tespit edilebilir. Bu tespit ışığında gerçekten kalp hastalığı ile alakalı tweetleri tespit edebilmemizi sağlayacak anahtar kelime grupları tespit edilebilir. Bu anahtar kelime grupları ile tweetlerden gerçekten kalp hastalığına sahip veya değil kanısına ulaşılabilir.
 
##### KAYNAKLAR

[1]	 M. Pavithra, A. M. Sindhana, T. Subajanaki, and S. Mahalakshmi, 2021. “Effective Heart Disease Prediction Systems Using Data Mining Techniques”, Annals of the Romanian Society for Cell Biology, 6566-6571. 

[2]	 L. Tokgozoglu, M. Kayikcioglu, and B. Ekinci, 2021. “The Landscape of Preventive Cardiology in Turkey: Challenges and successes”, American Journal of Preventive Cardiology, 100184.

[3]	TAŞÇI, Merve Esra; ŞAMLI, Rüya. Veri madenciliği ile kalp hastalığı teşhisi. Avrupa Bilim ve Teknoloji Dergisi, 2020, 88-95.

[4]	BULUT, Faruk. Determining Heart Attack Risk Ration Through AdaBoost/AdaBoost ile Kalp Krizi Risk Tespiti. Celal Bayar University Journal of Science, 2016, 12.3: 459-472.

[5]	Vatansever, B., AYDIN, H., & Çetinkaya, A. Genetik Algoritma Yaklaşımıyla Öznitelik Seçimi Kullanılarak Makine Öğrenmesi Algoritmaları ile Kalp Hastalığı Tahmini. Journal of Scientific, Technology and Engineering Research, 2(2), 67-80.

[6]	SOLMAZ, A. H., TİREN, Y., & ÖZKAYA, U. Kalp Hastalıklarının Tahmin Edilmesi Karşılaştırmalı Analiz.

[7]	OZCAN, İ., TASAR, B., TATAR, A. B., & YAKUT, O. (2019). Destek Vektör Makinasi Algoritması İle Kalp Hastalıklarının Tahmini. Computer Science, 4(2), 74-79.

[8]	AHMED, Hager, et al. Heart disease identification from patients’ social posts, machine learning solution on Spark. Future Generation Computer Systems, 2020, 111: 714-722.

[9]	JAIN, Swati, et al. A machine learning based depression analysis and suicidal ideation detection system using questionnaires and twitter. In: 2019 IEEE Students Conference on Engineering and Systems (SCES). IEEE, 2019. p. 1-6.

[10]	Bhadrashetty, Sudhir Anakal1 Chandrasekhar Uppin2 Ambresh. Discovering Stress Based on Social Interaction on Social Networking Sites. 2019.

[11]	ALOTAIBI, Shoayee, et al. Sehaa: A big data analytics tool for healthcare symptoms and diseases detection using Twitter, Apache Spark, and Machine Learning. Applied Sciences, 2020, 10.4: 1398.

[12]	AL ASAD, Nafiz, et al. Depression detection by analyzing social media posts of user. In: 2019 IEEE International Conference on Signal Processing, Information, Communication & Systems (SPICSCON). IEEE, 2019. p. 13-17.

[13]	JOSHI, Aditya, et al. Harnessing tweets for early detection of an acute disease event. Epidemiology (Cambridge, Mass.), 2020, 31.1: 90.

[14]	ÖZMEN, Ö., Ahmad, K. H. D. R., & Engin, A. V. C. I. (2018). Sınıflandırıcıların kalp hastalığı verileri üzerine performans karşılaştırması. Fırat Üniversitesi Mühendislik Bilimleri Dergisi, 30(3), 153-159.

[15]	Ali, F. (2015). Online diagnosis of diabetes with Twitter data. Missouri University of Science and Technology.

[16]	Chulis, K. (2016). Data mining Twitter for cancer, diabetes, and asthma insights (Doctoral dissertation, Purdue University).

[17]	Saravia, E., Chang, C. H., De Lorenzo, R. J., & Chen, Y. S. (2016, August). MIDAS: Mental illness detection and analysis via social media. In 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM) (pp. 1418-1421). IEEE.


